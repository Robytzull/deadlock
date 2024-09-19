from dash import html, dcc
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

# Layout per la pagina del paziente
layout = html.Div([

    # Breadcrumb per la navigazione
    create_breadcrumb_header("ACCESSO PAZIENTE", "/accesso-paziente"),

    # Contenuto principale della pagina
    html.Div([ 
        # Testo di benvenuto per il paziente
        html.H2(
            "Benvenuto, Paziente", 
            style={
                'textAlign': 'center', 
                'color': '#000000', 
                'marginTop': '100px'
            }
        ),

        # Rettangoli con: Storico Visite e Prenotazione Visite
        html.Div([
            dbc.Row([
                # Bottone per visualizzare lo storico delle visite
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Storico Visite", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/storico-visite',  # Link alla pagina dello storico delle visite
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

                # Bottone per prenotare una nuova visita
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Prenotazione Visite", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/prenotazione-visite',  # Link alla pagina di prenotazione visite
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
            ], className="justify-content-center")  # Centra i rettangoli orizzontalmente
        ], style={'marginTop': '100px'})  # Spazio sopra i rettangoli
    ])
])
