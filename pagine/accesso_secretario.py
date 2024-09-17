from dash import html
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

# Layout per la pagina Accesso Segreteria
layout = html.Div([

    # Breadcrumb per la navigazione
    create_breadcrumb_header("ACCESSO SEGRETERIA", "/accesso-segreteria"),

    # Contenuto principale della pagina
    html.Div([ 
        # Testo di benvenuto per la segreteria
        html.H2(
            "Benvenuto, Segretar* Nome", 
            style={
                'textAlign': 'center', 
                'color': '#000000', 
                'marginTop': '100px'
            }
        ),
        
        # Rettangoli con: Gestione Visite, Gestione Pazienti, Gestione Medici, Gestione Infermieri
        html.Div([
            dbc.Row([
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Gestione Visite", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/gestione-visite',  # Link alla pagina di gestione visite
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
                                html.H4("Gestione Pazienti", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/accesso-gestione-pazienti',  # Link alla pagina di gestione pazienti
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
                                html.H4("Gestione Medici", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/accesso-gestione-medici',  # Link alla pagina di gestione medici
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
                                html.H4("Gestione Infermieri", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/accesso-gestione-infermiere',  # Link alla pagina di gestione infermieri
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