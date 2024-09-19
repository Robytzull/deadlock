from dash import html, dcc, Input, Output, callback, State
import dash_bootstrap_components as dbc
from flask import session, has_app_context, has_request_context
from pony.orm import db_session, select
from entities import models
from entities.models import init_db
from ponteflask import app, server
#from entities.riempimento import CredenzialiPersonale

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
init_db()
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
    [Output('login-output', 'children'), Output('url', 'pathname')],
    [Input('login-button', 'n_clicks')],
    [State('login-username', 'value'), State('login-password', 'value')]
    
)

def handle_login(n_clicks, username, password):
    print(f"Has app context: {has_app_context()}")
    print(f"Has request context: {has_request_context()}")
    
    if not has_request_context():
        return "Session not available. No request context.", ''
    
    if n_clicks is None:
        return '', '/LOG-IN'
    with db_session:
        # Stampa i valori di username e password per verificarli nel terminale
        #print(f"Username inserito: {username}, Password inserita: {password}")

        # Cerca l'utente nel database
        #from entities.riempimento import CredenzialiPersonale
        #from entities.riempimento import CredenzialiPersonale
        #cerca il paziente adulto nel db
        paziente_adulto = models.CredenzialiPazienteAdulto.get(CF=username, password=password)
        if paziente_adulto:
            session['logged_in'] = True
            session['paziente_id'] = paziente_adulto.paziente.id  # Salva l'ID del paziente adulto nella sessione
            session['role'] = 'paziente_adulto'
            return f"Login effettuato come paziente adulto.", '/accesso-paziente'
        
        #cerca il paziente adolescente nel db
        paziente_adolescente = models.CredenzialiAdolescente.get(CF=username, password=password)
        if paziente_adolescente:
            session['logged_in'] = True
            session['paziente_adolescente_id'] = paziente_adolescente.paziente.id  # Salva l'ID del paziente adolescente nella sessione
            session['role'] = 'paziente_adolescente'
            return f"Login effettuato come paziente adolescente.", '/accesso-paziente'





        user = models.CredenzialiPersonale.get(username=username)
        if user and user.password == password:
            # Infer the role from the relationship
            if user.medico:
                role = 'medico'
                session['medico_id']=user.medico.id
            elif user.infermiere:
                role = 'infermiere'
                session['infermiere_id']=user.infermiere.id
            elif user.segreteria:
                role = 'segreteria'
                session['segretario_id']=user.segreteria.id
            else:
                role = 'ruolo sconosciuto'

            # Set user session and redirect to the appropriate page
            session['logged_in'] = True
            session['username'] = username
            session['role'] = role

            if role == 'medico':
                return f"Login effe ttuato come {role}.", '/accesso-medico'
            # You can add more redirects for infermiere, segreteria, etc.
            elif role == 'infermiere':
                return f"Login effettuato come {role}.", '/accesso-infermiere'
            elif role == 'segreteria':
                return f"Login effettuato come {role}.", '/accesso-segreteria'
            else:
                return f"Login effettuato come {role}.", '/home'
        else:
            return 'Nome utente o password errati.', '/login'
        
            
    
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

    
