from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import CredenzialiAdolescente, PazienteAdolescente
from ponteflask import app

# Funzione per generare il layout della pagina per aggiungere credenziali per l'adolescente
def layout_add_adolescenti_creds():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Crea Credenziali per Adolescente"),
                    dbc.Form([
                        # Campo per il Codice Fiscale (CF) del paziente adolescente
                        dbc.Label("Codice Fiscale Adolescente"),
                        dcc.Dropdown(id='dropdown-adolescente', options=[], placeholder="Seleziona un adolescente"),

                        # Campo per la password
                        dbc.Label("Password"),
                        dbc.Input(id="input-password", type="password", placeholder="Inserisci la password"),

                        # Pulsante per inviare il form
                        dbc.Button("Crea Credenziali", id="submit-creds-adolescente", color="primary", className="mt-3"),
                        html.Div(id="output-message-creds", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown con gli adolescenti dal database
@app.callback(
    Output('dropdown-adolescente', 'options'),
    Input('dropdown-adolescente', 'value')
)
@db_session
def populate_adolescente_dropdown(value):
    adolescenti = PazienteAdolescente.select()[:]
    options = [{'label': f"{adolescente.nome} {adolescente.cognome} ({adolescente.CF})", 'value': adolescente.CF} for adolescente in adolescenti]
    return options

# Callback per creare nuove credenziali per un adolescente
@app.callback(
    Output('output-message-creds', 'children'),
    Input('submit-creds-adolescente', 'n_clicks'),
    [State('dropdown-adolescente', 'value'),
     State('input-password', 'value')]
)
@db_session
def add_adolescenti_creds(n_clicks, cf_adolescente, password):
    if n_clicks is not None:
        if all([cf_adolescente, password]):
            # Verifica se esistono già credenziali per questo adolescente
            credenziali_exist = CredenzialiAdolescente.get(CF=cf_adolescente)
            if credenziali_exist:
                return "Errore: Credenziali già esistenti per questo adolescente."
            
            # Otteniamo l'oggetto del paziente adolescente
            adolescente = PazienteAdolescente.get(CF=cf_adolescente)
            if adolescente:
                # Creiamo il nuovo record per le credenziali
                CredenzialiAdolescente(CF=cf_adolescente, password=password, paziente=adolescente)
                commit()  # Salviamo i cambiamenti nel database
                return "Credenziali create con successo!"
            else:
                return "Errore: Adolescente non trovato."
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
