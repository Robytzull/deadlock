from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import Medico, CredenzialiPersonale
from ponteflask import app

# Funzione per generare il layout della pagina per creare le credenziali del medico
def layout_add_medico_creds():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Crea Credenziali Medico"),
                    dbc.Form([

                        # Campo per selezionare il medico
                        dbc.Label("Seleziona Medico"),
                        dcc.Dropdown(id='dropdown-medico', options=[], placeholder="Seleziona un medico"),

                        # Campo per il nome utente
                        dbc.Label("Username"),
                        dbc.Input(id="input-username-medico", type="text", placeholder="Inserisci il nome utente"),

                        # Campo per la password
                        dbc.Label("Password"),
                        dbc.Input(id="input-password-medico", type="password", placeholder="Inserisci la password"),

                        # Pulsante per inviare il form
                        dbc.Button("Crea Credenziali", id="submit-medico-creds", color="primary", className="mt-3"),
                        html.Div(id="output-message-medico-creds", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown dei medici dal database
@app.callback(
    Output('dropdown-medico', 'options'),
    Input('dropdown-medico', 'value')
)
@db_session
def populate_medico_dropdown(value):
    medici = Medico.select()[:]
    options = [{'label': f"{medico.nome} {medico.cognome}", 'value': medico.id} for medico in medici]
    return options

# Callback per gestire l'inserimento delle credenziali del medico
@app.callback(
    Output('output-message-medico-creds', 'children'),
    Input('submit-medico-creds', 'n_clicks'),
    [State('dropdown-medico', 'value'),
     State('input-username-medico', 'value'),
     State('input-password-medico', 'value')]
)
@db_session
def add_medico_creds(n_clicks, medico_id, username, password):
    if n_clicks is not None:
        if all([medico_id, username, password]):
            # Creiamo il nuovo record per le credenziali del medico
            medico = Medico.get(id=medico_id)
            CredenzialiPersonale(
                username=username,
                password=password,
                medico=medico
            )
            commit()  # Salviamo i cambiamenti nel database
            return "Credenziali del Medico create con successo!"
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
