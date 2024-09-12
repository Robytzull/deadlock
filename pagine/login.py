from dash import html, dcc, Input, Output, callback, State
import dash_bootstrap_components as dbc
from flask import session
from pony.orm import db_session, select
from entities.riempimento import CredenzialiPersonale

#from pagine.ponteflask import app  # Importa l'istanza dell'app Flask-Dash


# Layout per la pagina di login
layout = html.Div([
    dbc.Container([
        # Sezione del modulo di login
        dbc.Row([
            dbc.Col([
                html.H2("Login"),
                dbc.Card([
                    dbc.CardBody([
                        # Modulo di login con centratura del pulsante
                        html.Div([
                            dbc.Label("Username"),
                            dbc.Input(id="login-username", type="text"),
                            dbc.Label("Password"),
                            dbc.Input(id="login-password", type="password"),
                            html.Div([
                                dbc.Button("LOGIN", id="login-button", color="#7bb372", className="mt-2"),
                            ], style={
                                "display": "flex",
                                "justifyContent": "center",
                                "marginTop": "20px"
                            })
                        ], style={"textAlign": "center"})
                    ])
                ])
            ], width=6)
        ], justify="center"),
        # Messaggio di errore o successo del login
        html.Div(id="login-output", style={"marginTop": "20px", "textAlign": "center", "color": "red"})
    ], className="mt-4")
])

# Funzione per verificare le credenziali nel database
'''@db_session
def verify_credentials(username, password):
    #from entities.models import CredenzialiPersonale, CredenzialiPazienteAdulto
    # Verifica se le credenziali corrispondono nel database
    user = CredenzialiPersonale.get(username=username, password=password)
    if user:
        return 'medico'
    
    # Verifica per pazienti adulti
    user = CredenzialiPazienteAdulto.get(CF=username, password=password)
    if user:
        return 'paziente'
    
    return None'''

# Callback per il login
@callback(
    Output('login-output', 'children'),
    Input('login-button', 'n_clicks'),
    State('login-username', 'value'),
    State('login-password', 'value')
)
def handle_login(n_clicks, username, password):
    if n_clicks is None:
        return ''
    with db_session:
        # Stampa i valori di username e password per verificarli nel terminale
        #print(f"Username inserito: {username}, Password inserita: {password}")

        # Cerca l'utente nel database
        #from entities.riempimento import CredenzialiPersonale

        user = CredenzialiPersonale.get(username=username)
        if user:
            print(f"Utente trovato: {user.username}, Ruolo: {user.ruolo}")
        else:
            print("Utente non trovato")

        # Verifica credenziali nel database
        if user and user.password == password:
            print("Login riuscito")
            #return f"Login effettuato come {user.ruolo}."
        else:
            print("Credenziali errate")
            #return 'Nome utente o password errati.'
    
    ''' # Verifica delle credenziali
    role = verify_credentials(username, password)
    
    if role:
        # Se il login è corretto, crea la sessione dell'utente
        session['logged_in'] = True
        session['username'] = username
        session['role'] = role
        return f'Login effettuato come {role}.'
    
    return 'Nome utente o password errati.'

# Funzione per controllare se l'utente è loggato
def is_logged_in():
    return session.get('logged_in', False)'''

    
