from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import CredenzialiPersonale, Infermiere
from ponteflask import app

# Funzione per generare il layout della pagina per aggiungere le credenziali dell'infermiere
def layout_add_infermiere_creds():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Aggiungi Credenziali Infermiere"),
                    dbc.Form([
                        # Campo per l'infermiere (dropdown per selezionare l'infermiere esistente)
                        dbc.Label("Seleziona Infermiere"),
                        dcc.Dropdown(id='dropdown-infermiere', options=[], placeholder="Seleziona l'infermiere"),

                        # Campo per il nome utente
                        dbc.Label("Nome Utente"),
                        dbc.Input(id="input-username-infermiere", type="text", placeholder="Inserisci il nome utente"),

                        # Campo per la password
                        dbc.Label("Password"),
                        dbc.Input(id="input-password-infermiere", type="password", placeholder="Inserisci la password"),

                        # Pulsante per inviare il form
                        dbc.Button("Aggiungi Credenziali", id="submit-creds-infermiere", color="primary", className="mt-3"),
                        html.Div(id="output-message-creds-infermiere", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown degli infermieri dal database
@app.callback(
    Output('dropdown-infermiere', 'options'),
    Input('dropdown-infermiere', 'value')
)
@db_session
def populate_infermiere_dropdown(value):
    infermieri = Infermiere.select()[:]
    options = [{'label': f"{infermiere.nome} {infermiere.cognome}", 'value': infermiere.id} for infermiere in infermieri]
    return options

# Callback per gestire l'inserimento di nuove credenziali per l'infermiere
@app.callback(
    Output('output-message-creds-infermiere', 'children'),
    Input('submit-creds-infermiere', 'n_clicks'),
    [State('dropdown-infermiere', 'value'),
     State('input-username-infermiere', 'value'),
     State('input-password-infermiere', 'value')]
)
@db_session
def add_credenziali_infermiere(n_clicks, infermiere_id, username, password):
    if n_clicks is not None:
        if all([infermiere_id, username, password]):
            # Trova l'infermiere selezionato
            infermiere = Infermiere.get(id=infermiere_id)
            if infermiere:
                # Crea le credenziali per l'infermiere
                CredenzialiPersonale(
                    username=username,
                    password=password,
                    infermiere=infermiere
                )
                commit()  # Salviamo i cambiamenti nel database
                return "Credenziali aggiunte con successo!"
            else:
                return "Errore: Infermiere non trovato."
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
