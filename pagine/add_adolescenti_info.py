from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import PazienteAdolescente, PazienteAdulto
from ponteflask import app

# Funzione per generare il layout della pagina per aggiungere un paziente adolescente
def layout_add_adolescenti_info():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Aggiungi Paziente Adolescente"),
                    dbc.Form([
                        # Campo per il Codice Fiscale
                        dbc.Label("Codice Fiscale"),
                        dbc.Input(id="input-cf", type="text", placeholder="Inserisci il CF"),
                        
                        # Campo per il nome
                        dbc.Label("Nome"),
                        dbc.Input(id="input-nome", type="text", placeholder="Inserisci il nome"),

                        # Campo per il cognome
                        dbc.Label("Cognome"),
                        dbc.Input(id="input-cognome", type="text", placeholder="Inserisci il cognome"),

                        # Campo per la data di nascita
                        dbc.Label("Data di Nascita"),
                        dbc.Input(id="input-data-nascita", type="date"),

                        # Campo per il luogo di nascita
                        dbc.Label("Luogo di Nascita"),
                        dbc.Input(id="input-luogo-nascita", type="text", placeholder="Inserisci il luogo di nascita"),

                        # Campo per l'email del tutor
                        dbc.Label("Email Tutor"),
                        dbc.Input(id="input-mail-tutor", type="email", placeholder="Inserisci l'email del tutor"),

                        # Campo per scegliere il tutor adulto
                        dbc.Label("Seleziona il Tutor (Adulto)"),
                        dcc.Dropdown(id='dropdown-tutor', options=[], placeholder="Seleziona il tutor adulto"),

                        # Pulsante per inviare il form
                        dbc.Button("Aggiungi Adolescente", id="submit-adolescente", color="primary", className="mt-3"),
                        html.Div(id="output-message", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown dei tutor adulti dal database
@app.callback(
    Output('dropdown-tutor', 'options'),
    Input('dropdown-tutor', 'value')
)
@db_session
def populate_tutor_dropdown(value):
    adulti = PazienteAdulto.select()[:]
    options = [{'label': f"{adulto.nome} {adulto.cognome}", 'value': adulto.id} for adulto in adulti]
    return options

# Callback per gestire l'inserimento di un nuovo paziente adolescente
@app.callback(
    Output('output-message', 'children'),
    Input('submit-adolescente', 'n_clicks'),
    [State('input-cf', 'value'),
     State('input-nome', 'value'),
     State('input-cognome', 'value'),
     State('input-data-nascita', 'value'),
     State('input-luogo-nascita', 'value'),
     State('input-mail-tutor', 'value'),
     State('dropdown-tutor', 'value')]
)
@db_session
def add_paziente_adolescente(n_clicks, cf, nome, cognome, data_nascita, luogo_nascita, mail_tutor, tutor_id):
    if n_clicks is not None:
        if all([cf, nome, cognome, data_nascita, luogo_nascita, mail_tutor, tutor_id]):
            # Creiamo il nuovo record per il paziente adolescente
            tutor = PazienteAdulto.get(id=tutor_id)
            PazienteAdolescente(
                id=cf,
                CF=cf,
                nome=nome,
                cognome=cognome,
                data_nascita=data_nascita,
                luogo_nascita=luogo_nascita,
                mail_tutor=mail_tutor,
                tutor=tutor
            )
            commit()  # Salviamo i cambiamenti nel database
            return "Paziente Adolescente aggiunto con successo!"
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
