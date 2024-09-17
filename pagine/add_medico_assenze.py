from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import Medico, Assenze, Sostituzione
from ponteflask import app
from datetime import date

# Funzione per generare il layout della pagina per la gestione delle assenze
def layout_gestione_assenze_medico():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Gestione Assenze Medico"),
                    dbc.Form([

                        # Campo per selezionare il medico assente
                        dbc.Label("Seleziona Medico Assente"),
                        dcc.Dropdown(id='dropdown-medico-assente', options=[], placeholder="Seleziona un medico"),

                        # Campo per selezionare il medico sostituto
                        dbc.Label("Seleziona Medico Sostituto"),
                        dcc.Dropdown(id='dropdown-medico-sostituto', options=[], placeholder="Seleziona un medico sostituto (opzionale)", multi=False),

                        # Campo per la data dell'assenza
                        dbc.Label("Data dell'Assenza"),
                        dbc.Input(id="input-data", type="date"),

                        # Campo per il motivo dell'assenza
                        dbc.Label("Motivo"),
                        dbc.Input(id="input-motivo", type="text", placeholder="Inserisci il motivo dell'assenza"),

                        # Pulsante per inviare il form
                        dbc.Button("Aggiungi Assenza", id="submit-assenza", color="primary", className="mt-3"),
                        html.Div(id="output-message-assenza", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per popolare i dropdown dei medici dal database
@app.callback(
    [Output('dropdown-medico-assente', 'options'), Output('dropdown-medico-sostituto', 'options')],
    Input('dropdown-medico-assente', 'value')
)
@db_session
def populate_medico_dropdowns(value):
    medici = Medico.select()[:]
    options = [{'label': f"{medico.nome} {medico.cognome}", 'value': medico.id} for medico in medici]
    return options, options

# Callback per gestire l'inserimento di una nuova assenza e sostituzione
@app.callback(
    Output('output-message-assenza', 'children'),
    Input('submit-assenza', 'n_clicks'),
    [State('dropdown-medico-assente', 'value'),
     State('dropdown-medico-sostituto', 'value'),
     State('input-data', 'value'),
     State('input-motivo', 'value')]
)
@db_session
def add_assenza_medico(n_clicks, medico_id, sostituto_id, data_assenza, motivo):
    if n_clicks is not None:
        if all([medico_id, data_assenza, motivo]):
            # Aggiungiamo l'assenza
            medico = Medico.get(id=medico_id)
            Assenze(medico=medico, data=date.fromisoformat(data_assenza), motivo=motivo)

            # Aggiungiamo la sostituzione se presente
            if sostituto_id:
                sostituto = Medico.get(id=sostituto_id)
                Sostituzione(medico_sostituito=medico, medico_sostituto=sostituto)

            commit()  # Salviamo i cambiamenti nel database
            return "Assenza e sostituzione aggiunte con successo!"
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
