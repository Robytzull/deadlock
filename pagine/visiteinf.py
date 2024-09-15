from dash import html, dcc, callback, Input, Output, State, ALL
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import Visitainf, EsitoVisitaInfermieristica
from ponteflask import app
from flask import session

# Funzione per generare il layout delle visite dell'infermiere
def layout_visite_infermiere():
    # Recupera l'ID dell'infermiere dalla sessione
    infermiere_id = session.get('infermiere_id')

    if not infermiere_id:
        return html.Div("Errore: ID dell'infermiere non trovato nella sessione.")

    with db_session:
        # Estrazione delle visite dell'infermiere dal database
        visiteinf = Visitainf.select(lambda v: v.infermiere.id == infermiere_id)[:]

        # Creiamo una lista di card per ogni visita
        visiteinf_cards = []
        for visitainf in visiteinf:
            paziente_nome = "Paziente sconosciuto"
            if visitainf.paziente_adulto:
                paziente_nome = f"{visitainf.paziente_adulto.nome} {visitainf.paziente_adulto.cognome}"
            elif visitainf.paziente_minore:
                paziente_nome = f"{visitainf.paziente_minore.nome} {visitainf.paziente_minore.cognome} (Minore)"
            elif visitainf.paziente_adolescente:
                paziente_nome = f"{visitainf.paziente_adolescente.nome} {visitainf.paziente_adolescente.cognome} (Adolescente)"

            esito = EsitoVisitaInfermieristica.get(visitainf=visitainf)
            descrizione = esito.descrizione if esito else ""
            referto = esito.referto if esito else ""

            visitainf_card = dbc.Card([
                dbc.CardBody([
                    html.H5(f"Visita con {paziente_nome}", className="card-title"),
                    html.P(f"Data: {visitainf.data}", className="card-text"),
                    dbc.Label("Descrizione"),
                    dbc.Textarea(id={'type': 'descrizione-input-infermiere', 'index': visitainf.id}, value=descrizione),
                    dbc.Label("Referto"),
                    dbc.Textarea(id={'type': 'referto-input-infermiere', 'index': visitainf.id}, value=referto),
                    dbc.Button("Salva Referto", id={'type': 'referto-btn-infermiere', 'index': visitainf.id}, color="primary"),
                    html.Div(id={'type': 'referto-output-infermiere', 'index': visitainf.id})
                ])
            ], className="mb-4")
            visiteinf_cards.append(visitainf_card)

    return html.Div([
        html.H2("Visite Infermiere", style={'textAlign': 'center', 'marginTop': '20px'}),
        *visiteinf_cards  # Aggiungiamo tutte le card delle visite
    ])

# Callback per gestire l'inserimento dei referti per ogni visita dell'infermiere
@app.callback(
    Output({'type': 'referto-output-infermiere', 'index': ALL}, 'children'),
    [Input({'type': 'referto-btn-infermiere', 'index': ALL}, 'n_clicks')],
    [State({'type': 'descrizione-input-infermiere', 'index': ALL}, 'value'),
     State({'type': 'referto-input-infermiere', 'index': ALL}, 'value'),
     State({'type': 'referto-btn-infermiere', 'index': ALL}, 'id')]
)
@db_session
def handle_referto_infermiere_inserimento(n_clicks, descrizioni, referti, ids):
    # Se uno dei pulsanti è stato cliccato
    if any(n_clicks):
        for i, n_click in enumerate(n_clicks):
            if n_click:
                visitainf_id = ids[i]['index']
                descrizione = descrizioni[i]
                referto = referti[i]

                # Trova la visita e salva il referto e la descrizione
                visitainf = Visitainf.get(id=visitainf_id)
                if visitainf:
                    esito = EsitoVisitaInfermieristica.get(visitainf=visitainf)
                    if not esito:
                        # Se non esiste un esito, creiamone uno
                        EsitoVisitaInfermieristica(visitainf=visitainf, infermiere=visitainf.infermiere, descrizione=descrizione, referto=referto)
                    else:
                        # Altrimenti aggiorniamo i campi esistenti
                        esito.descrizione = descrizione
                        esito.referto = referto
                    commit()  # Salviamo i cambiamenti nel database

                    return [f"Referto salvato per la visita con ID: {visitainf_id}" if j == i else "" for j in range(len(n_clicks))]
    return ['' for _ in n_clicks]