from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import PazienteMinore, PazienteAdulto
from ponteflask import app

# Funzione per generare il layout della pagina per aggiungere un paziente minore
def layout_add_minori_info():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Aggiungi Paziente Minore"),
                    dbc.Form([

                        # Campo per il Codice Fiscale (che sarà anche l'ID)
                        dbc.Label("Codice Fiscale (CF)"),
                        dbc.Input(id="input-cf-minore", type="text", placeholder="Inserisci il CF (ID)"),
                        
                        # Campo per il nome
                        dbc.Label("Nome"),
                        dbc.Input(id="input-nome-minore", type="text", placeholder="Inserisci il nome"),

                        # Campo per il cognome
                        dbc.Label("Cognome"),
                        dbc.Input(id="input-cognome-minore", type="text", placeholder="Inserisci il cognome"),

                        # Campo per la data di nascita
                        dbc.Label("Data di Nascita"),
                        dbc.Input(id="input-data-nascita-minore", type="date"),

                        # Campo per il luogo di nascita
                        dbc.Label("Luogo di Nascita"),
                        dbc.Input(id="input-luogo-nascita-minore", type="text", placeholder="Inserisci il luogo di nascita"),

                        # Dropdown per selezionare l'adulto responsabile
                        dbc.Label("Seleziona l'Adulto Responsabile"),
                        dcc.Dropdown(id='dropdown-adulto', options=[], placeholder="Seleziona l'adulto responsabile"),

                        # Campo per l'email del responsabile (che verrà compilato automaticamente)
                        dbc.Label("Email del Responsabile"),
                        dbc.Input(id="input-email-responsabile", type="email", placeholder="Email del responsabile", disabled=True),

                        # Pulsante per inviare il form
                        dbc.Button("Aggiungi Minore", id="submit-minore", color="primary", className="mt-3"),
                        html.Div(id="output-message-minore", className="mt-3")  # Output per i messaggi di successo/errore
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown degli adulti dal database e aggiornare l'email
@app.callback(
    [Output('dropdown-adulto', 'options'), Output('input-email-responsabile', 'value')],
    Input('dropdown-adulto', 'value')
)
@db_session
def populate_adulto_dropdown(adulto_id):
    adulti = PazienteAdulto.select()[:]
    options = [{'label': f"{adulto.nome} {adulto.cognome}", 'value': adulto.id} for adulto in adulti]

    # Se è stato selezionato un adulto, aggiorniamo l'email
    if adulto_id:
        adulto_selezionato = PazienteAdulto.get(id=adulto_id)
        email = adulto_selezionato.mail if adulto_selezionato else ""
    else:
        email = ""

    return options, email

# Callback per gestire l'inserimento di un nuovo paziente minore
@app.callback(
    Output('output-message-minore', 'children'),
    Input('submit-minore', 'n_clicks'),
    [State('input-cf-minore', 'value'),
     State('input-nome-minore', 'value'),
     State('input-cognome-minore', 'value'),
     State('input-data-nascita-minore', 'value'),
     State('input-luogo-nascita-minore', 'value'),
     State('dropdown-adulto', 'value'),
     State('input-email-responsabile', 'value')]
)
@db_session
def add_paziente_minore(n_clicks, cf, nome, cognome, data_nascita, luogo_nascita, adulto_id, email_responsabile):
    if n_clicks is not None:
        if all([cf, nome, cognome, data_nascita, luogo_nascita, adulto_id, email_responsabile]):
            # Trova l'adulto responsabile
            adulto_responsabile = PazienteAdulto.get(id=adulto_id)
            if adulto_responsabile:
                # Creiamo il nuovo record per il paziente minore
                PazienteMinore(
                    id=cf,
                    CF=cf,
                    nome=nome,
                    cognome=cognome,
                    data_nascita=data_nascita,
                    luogo_nascita=luogo_nascita,
                    mail_responsabile=email_responsabile,
                    responsabile_adulto=adulto_responsabile
                )
                commit()  # Salviamo i cambiamenti nel database
                return "Paziente Minore aggiunto con successo!"
            else:
                return "Errore: Adulto responsabile non trovato."
        else:
            return "Errore: Tutti i campi devono essere compilati."
    return ""

