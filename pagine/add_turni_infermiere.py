from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import TurniInfermiere, Infermiere
from ponteflask import app
import uuid

# Funzione per generare il layout della pagina per aggiungere i turni degli infermieri
def layout_add_turni_infermiere():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Aggiungi Turni Infermiere"),
                    dbc.Form([
                        # Dropdown per selezionare l'infermiere
                        dbc.Label("Seleziona Infermiere"),
                        dcc.Dropdown(id='dropdown-infermiere-turno', options=[], placeholder="Seleziona l'infermiere"),

                        # Campo per la data di inizio
                        dbc.Label("Data Inizio"),
                        dbc.Input(id="input-data-inizio", type="date"),

                        # Campo per la data di fine
                        dbc.Label("Data Fine"),
                        dbc.Input(id="input-data-fine", type="date"),

                        # Campo per l'orario di inizio
                        dbc.Label("Orario Inizio"),
                        dbc.Input(id="input-orario-inizio", type="text", placeholder="Inserisci l'orario di inizio (es. 08:00)"),

                        # Campo per l'orario di fine
                        dbc.Label("Orario Fine"),
                        dbc.Input(id="input-orario-fine", type="text", placeholder="Inserisci l'orario di fine (es. 16:00)"),

                        # Pulsante per inviare il form
                        dbc.Button("Aggiungi Turno", id="submit-turno-infermiere", color="primary", className="mt-3"),
                        html.Div(id="output-message-turno-infermiere", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown degli infermieri dal database
@app.callback(
    Output('dropdown-infermiere-turno', 'options'),
    Input('dropdown-infermiere-turno', 'value')
)
@db_session
def populate_infermiere_dropdown_turno(value):
    infermieri = Infermiere.select()[:]
    options = [{'label': f"{infermiere.nome} {infermiere.cognome}", 'value': infermiere.id} for infermiere in infermieri]
    return options

# Callback per gestire l'inserimento di nuovi turni per l'infermiere
@app.callback(
    Output('output-message-turno-infermiere', 'children'),
    Input('submit-turno-infermiere', 'n_clicks'),
    [State('dropdown-infermiere-turno', 'value'),
     State('input-data-inizio', 'value'),
     State('input-data-fine', 'value'),
     State('input-orario-inizio', 'value'),
     State('input-orario-fine', 'value')]
)
@db_session
def add_turno_infermiere(n_clicks, infermiere_id, data_inizio, data_fine, orario_inizio, orario_fine):
    if n_clicks is not None:
        if all([infermiere_id, data_inizio, data_fine, orario_inizio, orario_fine]):
            # Trova l'infermiere selezionato
            infermiere = Infermiere.get(id=infermiere_id)
            if infermiere:
                # Crea un nuovo turno per l'infermiere
                TurniInfermiere(
                    id=str(uuid.uuid4()),  # Generiamo un ID univoco per il turno
                    infermiere=infermiere,
                    data_inizio=data_inizio,
                    data_fine=data_fine,
                    orario_inizio=orario_inizio,
                    orario_fine=orario_fine
                )
                commit()  # Salviamo i cambiamenti nel database
                return "Turno aggiunto con successo!"
            else:
                return "Errore: Infermiere non trovato."
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
