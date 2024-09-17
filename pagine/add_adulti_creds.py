from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import PazienteAdulto, CredenzialiPazienteAdulto
from ponteflask import app

# Funzione per generare il layout della pagina per creare credenziali paziente adulto
def layout_add_adulti_creds():
    return html.Div([
        dbc.Container([

            dbc.Row([
                dbc.Col([
                    html.H2("Crea Credenziali per Paziente Adulto"),

                    # Form per l'inserimento delle credenziali del paziente adulto
                    dbc.Form([

                        dbc.Label("Codice Fiscale Paziente"),
                        dcc.Dropdown(id="dropdown-cf-adulto", placeholder="Seleziona CF Paziente Adulto"),

                        dbc.Label("Password"),
                        dbc.Input(id="input-password-adulto", type="password", placeholder="Inserisci la password"),

                        # Pulsante per inviare il form
                        dbc.Button("Crea Credenziali", id="submit-adulto-creds", color="primary", className="mt-3"),

                        html.Div(id="output-message-adulto-creds", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")

        ])
    ])

# Callback per popolare il dropdown con i CF dei pazienti adulti
@app.callback(
    Output('dropdown-cf-adulto', 'options'),
    Input('dropdown-cf-adulto', 'value')
)
@db_session
def populate_adult_cf_dropdown(value):
    adulti = PazienteAdulto.select()[:]
    options = [{'label': f"{adulto.nome} {adulto.cognome} - {adulto.CF}", 'value': adulto.CF} for adulto in adulti]
    return options

# Callback per gestire l'inserimento delle credenziali
@app.callback(
    Output('output-message-adulto-creds', 'children'),
    Input('submit-adulto-creds', 'n_clicks'),
    [State('dropdown-cf-adulto', 'value'),
     State('input-password-adulto', 'value')]
)
@db_session
def create_adult_creds(n_clicks, selected_cf, password):
    if n_clicks:
        if not selected_cf or not password:
            return "Errore: Seleziona un CF e inserisci una password."
        
        # Trova il paziente adulto
        paziente = PazienteAdulto.get(CF=selected_cf)
        if not paziente:
            return f"Errore: Paziente con CF {selected_cf} non trovato."
        
        # Controlla se le credenziali esistono già
        if CredenzialiPazienteAdulto.get(CF=selected_cf):
            return f"Errore: Credenziali per {selected_cf} esistono già."
        
        # Crea le credenziali
        CredenzialiPazienteAdulto(CF=selected_cf, password=password, paziente=paziente)
        commit()  # Salviamo i cambiamenti nel database
        return f"Credenziali create per {selected_cf}."
    return ""
