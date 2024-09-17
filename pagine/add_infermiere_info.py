from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import Infermiere
from ponteflask import app

# Funzione per generare il layout della pagina per aggiungere un infermiere
def layout_add_infermiere_info():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Aggiungi Infermiere"),
                    dbc.Form([
                        # Campo per il Codice Fiscale (che sarà anche l'ID)
                        dbc.Label("Codice Fiscale (CF)"),
                        dbc.Input(id="input-cf-infermiere", type="text", placeholder="Inserisci il CF (ID)"),
                        
                        # Campo per il nome
                        dbc.Label("Nome"),
                        dbc.Input(id="input-nome-infermiere", type="text", placeholder="Inserisci il nome"),

                        # Campo per il cognome
                        dbc.Label("Cognome"),
                        dbc.Input(id="input-cognome-infermiere", type="text", placeholder="Inserisci il cognome"),

                        # Campo per la data di nascita
                        dbc.Label("Data di Nascita"),
                        dbc.Input(id="input-data-nascita-infermiere", type="date"),

                        # Campo per il luogo di nascita
                        dbc.Label("Luogo di Nascita"),
                        dbc.Input(id="input-luogo-nascita-infermiere", type="text", placeholder="Inserisci il luogo di nascita"),

                        # Campo per l'email
                        dbc.Label("Email"),
                        dbc.Input(id="input-email-infermiere", type="email", placeholder="Inserisci l'email"),

                        # Pulsante per inviare il form
                        dbc.Button("Aggiungi Infermiere", id="submit-infermiere", color="primary", className="mt-3"),
                        html.Div(id="output-message-infermiere", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per gestire l'inserimento di un nuovo infermiere
@app.callback(
    Output('output-message-infermiere', 'children'),
    Input('submit-infermiere', 'n_clicks'),
    [State('input-cf-infermiere', 'value'),
     State('input-nome-infermiere', 'value'),
     State('input-cognome-infermiere', 'value'),
     State('input-data-nascita-infermiere', 'value'),
     State('input-luogo-nascita-infermiere', 'value'),
     State('input-email-infermiere', 'value')]
)
@db_session
def add_infermiere(n_clicks, cf, nome, cognome, data_nascita, luogo_nascita, email):
    if n_clicks is not None:
        if all([cf, nome, cognome, data_nascita, luogo_nascita, email]):
            # Creiamo il nuovo record per l'infermiere
            Infermiere(
                id=cf,
                CF=cf,
                nome=nome,
                cognome=cognome,
                data_nascita=data_nascita,
                luogo_nascita=luogo_nascita,
                mail=email
            )
            commit()  # Salviamo i cambiamenti nel database
            return "Infermiere aggiunto con successo!"
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
