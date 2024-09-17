from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import Medico
from ponteflask import app

# Funzione per generare il layout della pagina per aggiungere un medico
def layout_add_medico_info():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Aggiungi Medico"),
                    dbc.Form([
                        # Campo per il Codice Fiscale (che sarà anche l'ID)
                        dbc.Label("Codice Fiscale (CF)"),
                        dbc.Input(id="input-cf-medico", type="text", placeholder="Inserisci il CF (ID)"),
                        
                        # Campo per il nome
                        dbc.Label("Nome"),
                        dbc.Input(id="input-nome-medico", type="text", placeholder="Inserisci il nome"),

                        # Campo per il cognome
                        dbc.Label("Cognome"),
                        dbc.Input(id="input-cognome-medico", type="text", placeholder="Inserisci il cognome"),

                        # Campo per la data di nascita
                        dbc.Label("Data di Nascita"),
                        dbc.Input(id="input-data-nascita-medico", type="date"),

                        # Campo per il luogo di nascita
                        dbc.Label("Luogo di Nascita"),
                        dbc.Input(id="input-luogo-nascita-medico", type="text", placeholder="Inserisci il luogo di nascita"),

                        # Campo per l'email
                        dbc.Label("Email"),
                        dbc.Input(id="input-email-medico", type="email", placeholder="Inserisci l'email"),

                        # Campo per la specialità (opzionale)
                        dbc.Label("Specialità"),
                        dbc.Input(id="input-specialita-medico", type="text", placeholder="Inserisci la specialità (opzionale)"),

                        # Pulsante per inviare il form
                        dbc.Button("Aggiungi Medico", id="submit-medico", color="primary", className="mt-3"),
                        html.Div(id="output-message-medico", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per gestire l'inserimento di un nuovo medico
@app.callback(
    Output('output-message-medico', 'children'),
    Input('submit-medico', 'n_clicks'),
    [State('input-cf-medico', 'value'),
     State('input-nome-medico', 'value'),
     State('input-cognome-medico', 'value'),
     State('input-data-nascita-medico', 'value'),
     State('input-luogo-nascita-medico', 'value'),
     State('input-email-medico', 'value'),
     State('input-specialita-medico', 'value')]
)
@db_session
def add_medico(n_clicks, cf, nome, cognome, data_nascita, luogo_nascita, email, specialita):
    if n_clicks is not None:
        if all([cf, nome, cognome, data_nascita, luogo_nascita, email]):
            # Creiamo il nuovo record per il medico
            Medico(
                id=cf,
                CF=cf,
                nome=nome,
                cognome=cognome,
                data_nascita=data_nascita,
                luogo_nascita=luogo_nascita,
                mail=email,
                specialita=specialita
            )
            commit()  # Salviamo i cambiamenti nel database
            return "Medico aggiunto con successo!"
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
