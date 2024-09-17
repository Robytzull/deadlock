from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import PazienteAdulto
from ponteflask import app

# Funzione per generare il layout della pagina per aggiungere un paziente adulto
def layout_add_adulti_info():
    return html.Div([
        dbc.Container([

            dbc.Row([
                dbc.Col([
                    html.H2("Aggiungi Paziente Adulto"),

                    # Form per l'inserimento delle informazioni del paziente adulto
                    dbc.Form([
                        dbc.Label("Codice Fiscale"),
                        dbc.Input(id="input-cf-adulto", type="text", placeholder="Inserisci il CF"),

                        dbc.Label("Nome"),
                        dbc.Input(id="input-nome-adulto", type="text", placeholder="Inserisci il nome"),

                        dbc.Label("Cognome"),
                        dbc.Input(id="input-cognome-adulto", type="text", placeholder="Inserisci il cognome"),

                        dbc.Label("Data di Nascita"),
                        dbc.Input(id="input-data-nascita-adulto", type="date"),

                        dbc.Label("Luogo di Nascita"),
                        dbc.Input(id="input-luogo-nascita-adulto", type="text", placeholder="Inserisci il luogo di nascita"),

                        dbc.Label("Email"),
                        dbc.Input(id="input-email-adulto", type="email", placeholder="Inserisci l'email"),

                        # Pulsante per inviare il form
                        dbc.Button("Aggiungi Paziente Adulto", id="submit-adulto", color="primary", className="mt-3"),

                        html.Div(id="output-message-adulto", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")

        ])
    ])

# Callback per gestire l'inserimento di un nuovo paziente adulto
@app.callback(
    Output('output-message-adulto', 'children'),
    Input('submit-adulto', 'n_clicks'),
    [State('input-cf-adulto', 'value'),
     State('input-nome-adulto', 'value'),
     State('input-cognome-adulto', 'value'),
     State('input-data-nascita-adulto', 'value'),
     State('input-luogo-nascita-adulto', 'value'),
     State('input-email-adulto', 'value')]
)
@db_session
def add_paziente_adulto(n_clicks, cf, nome, cognome, data_nascita, luogo_nascita, email):
    if n_clicks is not None:
        if all([cf, nome, cognome, data_nascita, luogo_nascita, email]):
            # Controlliamo se il paziente esiste già
            if PazienteAdulto.get(CF=cf):
                return "Errore: Paziente con questo CF esiste già."
            
            # Creiamo il nuovo record per il paziente adulto
            PazienteAdulto(
                id =cf, 
                CF=cf,
                nome=nome,
                cognome=cognome,
                data_nascita=data_nascita,
                luogo_nascita=luogo_nascita,
                mail=email
            )
            commit()  # Salviamo i cambiamenti nel database
            return "Paziente Adulto aggiunto con successo!"
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""
