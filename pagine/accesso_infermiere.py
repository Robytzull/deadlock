from dash import html
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

# Layout per la pagina Accesso Infermieri
layout = html.Div([

    # Breadcrumb per la navigazione
    create_breadcrumb_header("ACCESSO INFERMIERE", "/accesso-infermiere"),

    # Contenuto principale della pagina
    html.Div([ 
        # Testo di benvenuto per l'infermiere
        html.H2(
            "Benvenuto, Infermiere Nome", 
            style={
                'textAlign': 'center', 
                'color': '#000000', 
                'marginTop': '70px'
            }
        ),
        
        # Rettangoli con: Visite e Calendario
        html.Div([
            dbc.Row([
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Visite", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/visite-infermiere',  # Link alla pagina delle visite
                        style={
                            'textDecoration': 'none', 
                            'display': 'block', 
                            'height': '150px', 
                            'width': '450px'
                        }  # Dimensioni rettangolo
                    ),
                    width=6,
                    className="mb-4 d-flex align-items-center justify-content-center"
                ),

                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Calendario", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/calendario-infermiere',  # Link alla pagina del calendario
                        style={
                            'textDecoration': 'none', 
                            'display': 'block', 
                            'height': '150px', 
                            'width': '450px'
                        }  # Dimensioni rettangolo
                    ),
                    width=6,
                    className="mb-4 d-flex align-items-center justify-content-center"
                )
            ], className="justify-content-center")  # Centra i rettangoli orizzontalmente
        ], style={'marginTop': '100px'})  # Spazio sopra i rettangoli
    ])
])