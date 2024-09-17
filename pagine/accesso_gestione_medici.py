from dash import html
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

# Layout per la pagina Accesso Gestione Medici
layout = html.Div([

    # Breadcrumb per la navigazione
    create_breadcrumb_header("ACCESSO GESTIONE MEDICI", "/accesso-gestione-medici"),

    # Contenuto principale della pagina
    html.Div([ 
        # Testo di benvenuto per la gestione medici
        html.H2(
            "Gestione Medici", 
            style={
                'textAlign': 'center', 
                'color': '#000000', 
                'marginTop': '100px'
            }
        ),
        
        # Rettangoli con: Aggiungi Medico, Crea Credenziali, Gestione Assenze
        html.Div([
            dbc.Row([
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Aggiungi Medico", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/add-medico-info',  # Link alla pagina per aggiungere medico
                        style={
                            'textDecoration': 'none', 
                            'display': 'block', 
                            'height': '150px', 
                            'width': '300px'
                        }  # Dimensioni rettangolo
                    ),
                    width=3,
                    className="mb-4 d-flex align-items-center justify-content-center"
                ),

                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Crea Credenziali", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/add-medico-creds',  # Link alla pagina per creare credenziali
                        style={
                            'textDecoration': 'none', 
                            'display': 'block', 
                            'height': '150px', 
                            'width': '300px'
                        }  # Dimensioni rettangolo
                    ),
                    width=3,
                    className="mb-4 d-flex align-items-center justify-content-center"
                ),

                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Gestione Assenze", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/gestione-assenze-medico',  # Link alla pagina per gestire le assenze del medico
                        style={
                            'textDecoration': 'none', 
                            'display': 'block', 
                            'height': '150px', 
                            'width': '300px'
                        }  # Dimensioni rettangolo
                    ),
                    width=3,
                    className="mb-4 d-flex align-items-center justify-content-center"
                )
            ], className="justify-content-center")  # Centra i rettangoli orizzontalmente
        ], style={'marginTop': '100px'})  # Spazio sopra i rettangoli
    ])
])
