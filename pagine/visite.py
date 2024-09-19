from dash import html, dcc, callback, Input, Output, State, ALL
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import  Visita, EsitoVisitaMedica
from ponteflask import app
from flask import session


# Funzione per generare il layout delle visite
def layout_visite():
    # Recupera l'ID del medico dalla sessione
    medico_id = session.get('medico_id')

    if not medico_id:
        return html.Div("Errore: ID del medico non trovato nella sessione.")

    with db_session:
        # Estrazione delle visite del medico dal database
        visite = Visita.select(lambda v: v.medico.id == medico_id)[:]

        # Creiamo una lista di card per ogni visita
        visite_cards = []
        for visita in visite:
            # Controlliamo se la visita è associata a un paziente adulto, minore o adolescente
            if visita.paziente_adulto:
                paziente_nome = f"{visita.paziente_adulto.nome} {visita.paziente_adulto.cognome}"
            elif visita.paziente_minore:
                paziente_nome = f"{visita.paziente_minore.nome} {visita.paziente_minore.cognome} (Minore)"
            elif visita.paziente_adolescente:
                paziente_nome = f"{visita.paziente_adolescente.nome} {visita.paziente_adolescente.cognome} (Adolescente)"
            else:
                paziente_nome = "Paziente sconosciuto"

            # Estrazione dell'esito della visita
            esito = EsitoVisitaMedica.get(visita=visita)
            descrizione = esito.descrizione if esito else ""
            referto = esito.referto if esito else ""

            # Creazione della card per la visita
            visita_card = dbc.Card([
                dbc.CardBody([
                    html.H5(f"Visita con {paziente_nome}", className="card-title"),
                    html.P(f"Data: {visita.data}", className="card-text"),
                    # Input per descrizione e referto
                    dbc.Label("Descrizione"),
                    dbc.Textarea(id={'type': 'descrizione-input', 'index': visita.id}, value=descrizione, placeholder="Inserisci la descrizione"),
                    dbc.Label("Referto"),
                    dbc.Textarea(id={'type': 'referto-input', 'index': visita.id}, value=referto, placeholder="Inserisci il referto"),
                    # Pulsante per salvare
                    dbc.Button("Salva Referto", id={'type': 'referto-btn', 'index': visita.id}, color="primary", className="me-2 mt-2"),
                    html.Div(id={'type': 'referto-output', 'index': visita.id})
                ])
            ], className="mb-4")
            visite_cards.append(visita_card)

    return html.Div([
        html.H2("Visite", style={'textAlign': 'center', 'marginTop': '20px'}),
        *visite_cards  # Aggiungiamo tutte le card delle visite
    ])

# Callback per gestire l'inserimento dei referti per ogni visita
@app.callback(
    Output({'type': 'referto-output', 'index': ALL}, 'children'),
    [Input({'type': 'referto-btn', 'index': ALL}, 'n_clicks')],
    [State({'type': 'descrizione-input', 'index': ALL}, 'value'),
     State({'type': 'referto-input', 'index': ALL}, 'value'),
     State({'type': 'referto-btn', 'index': ALL}, 'id')]
)
@db_session
def handle_referto_inserimento(n_clicks, descrizioni, referti, ids):
    # Se uno dei pulsanti è stato cliccato
    if any(n_clicks):
        for i, n_click in enumerate(n_clicks):
            if n_click:
                visita_id = ids[i]['index']
                descrizione = descrizioni[i]
                referto = referti[i]
                
                # Trova la visita e salva il referto e la descrizione
                visita = Visita.get(id=visita_id)
                if visita:
                    esito = EsitoVisitaMedica.get(visita=visita)
                    if not esito:
                        # Se non esiste un esito, creiamone uno
                        EsitoVisitaMedica(id=visita.id, visita=visita, medico=visita.medico, descrizione=descrizione, referto=referto, data=visita.data)
                    else:
                        # Altrimenti aggiorniamo i campi esistenti
                        esito.descrizione = descrizione
                        esito.referto = referto
                    commit()  # Salviamo i cambiamenti nel database
                    
                    return [f"Referto salvato per la visita con ID: {visita_id}" if j == i else "" for j in range(len(n_clicks))]
    return ['' for _ in n_clicks]


