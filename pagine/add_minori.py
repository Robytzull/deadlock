from dash import html
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

# Layout per la pagina Accesso Minori
layout = html.Div([

    # Breadcrumb per la navigazione
    create_breadcrumb_header("ADD MINORI", "/add-minori"),

    # Contenuto principale della pagina
    html.Div([ 
        # Testo di benvenuto per la segreteria
        html.H2(
            "Choose what type of patient to add", 
            style={
                'textAlign': 'center', 
                'color': '#000000', 
                'marginTop': '100px'
            }
        ), 

        # Rettangoli con: Aggiunta informazioni Minori
        html.Div([
            dbc.Row([

                # Bottone per aggiungere informazioni per i Minori
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Add Minori Information", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/add-minori-info',  # Link alla pagina di gestione pazienti
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
