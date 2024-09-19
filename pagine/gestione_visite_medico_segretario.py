from dash import html, dcc, Input, Output, State, callback, ALL
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import Visita, EsitoVisitaMedica, Medico
from ponteflask import app

# Funzione per generare il layout delle visite mediche per il segretario
def layout_gestione_visite_medico_segretario():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Gestione Visite Medico"),
                    
                    # Dropdown per selezionare un medico
                    dbc.Label("Seleziona un Medico"),
                    dcc.Dropdown(
                        id="medico-dropdown",
                        options=[],  # Le opzioni saranno popolati nel callback
                        placeholder="Seleziona un medico",
                    ),

                    # Sezione per mostrare le visite
                    html.Div(id='visite-lista')
                ], width=8)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown dei medici
@app.callback(
    Output('medico-dropdown', 'options'),
    Input('medico-dropdown', 'value')
)
@db_session
def populate_medico_dropdown(value):
    medici = Medico.select()[:]
    options = [{'label': f"Dr. {medico.nome} {medico.cognome}", 'value': medico.id} for medico in medici]
    return options

# Callback per mostrare le visite del medico selezionato
@app.callback(
    Output('visite-lista', 'children'),
    [Input('medico-dropdown', 'value')]
)
@db_session
def mostra_visite_medico(medico_id):
    if medico_id:
        visite = Visita.select(lambda v: v.medico.id == medico_id)[:]
        if not visite:
            return html.Div("Nessuna visita trovata per questo medico.")

        # Creiamo una lista di card per ogni visita
        visite_cards = []
        for visita in visite:
            paziente_nome = "Paziente sconosciuto"
            if visita.paziente_adulto:
                paziente_nome = f"{visita.paziente_adulto.nome} {visita.paziente_adulto.cognome}"
            elif visita.paziente_minore:
                paziente_nome = f"{visita.paziente_minore.nome} {visita.paziente_minore.cognome} (Minore)"
            elif visita.paziente_adolescente:
                paziente_nome = f"{visita.paziente_adolescente.nome} {visita.paziente_adolescente.cognome} (Adolescente)"

            esito = EsitoVisitaMedica.get(visita=visita)
            descrizione = esito.descrizione if esito else ""
            referto = esito.referto if esito else ""

            visita_card = dbc.Card([
                dbc.CardBody([
                    html.H5(f"Visita con {paziente_nome}", className="card-title"),
                    html.P(f"Data: {visita.data}", className="card-text"),
                    dbc.Label("Descrizione"),
                    dbc.Textarea(id={'type': 'descrizione-input-medico', 'index': visita.id}, value=descrizione),
                    dbc.Label("Referto"),
                    dbc.Textarea(id={'type': 'referto-input-medico', 'index': visita.id}, value=referto),
                    dbc.Button("Salva Referto", id={'type': 'salva-referto-btn-medico', 'index': visita.id}, color="primary"),
                    html.Div(id={'type': 'referto-output-medico', 'index': visita.id})
                ])
            ], className="mb-4")
            visite_cards.append(visita_card)

        return visite_cards

    return html.Div("Seleziona un medico per visualizzare le visite.")

# Callback per salvare il referto e la descrizione delle visite
@app.callback(
    Output({'type': 'referto-output-medico', 'index': ALL}, 'children'),
    [Input({'type': 'salva-referto-btn-medico', 'index': ALL}, 'n_clicks')],
    [State({'type': 'descrizione-input-medico', 'index': ALL}, 'value'),
     State({'type': 'referto-input-medico', 'index': ALL}, 'value'),
     State({'type': 'salva-referto-btn-medico', 'index': ALL}, 'id')]
)
@db_session
def salva_referto_medico(n_clicks, descrizioni, referti, ids):
    output = ['' for _ in range(len(n_clicks))]

    if any(n_clicks):
        for i, n_click in enumerate(n_clicks):
            if n_click and i < len(descrizioni) and i < len(referti):
                visita_id = ids[i]['index']
                descrizione = descrizioni[i]
                referto = referti[i]

                visita = Visita.get(id=visita_id)
                if visita:
                    esito = EsitoVisitaMedica.get(visita=visita)
                    if not esito:
                        EsitoVisitaMedica(id=visita.id, visita=visita, medico=visita.medico, descrizione=descrizione, referto=referto, data=visita.data)
                    else:
                        esito.descrizione = descrizione
                        esito.referto = referto
                    commit()

                    output[i] = f"Referto salvato per la visita con ID: {visita_id}"

    return output





