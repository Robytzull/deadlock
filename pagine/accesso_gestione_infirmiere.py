from dash import html
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

# Layout per la pagina Accesso Gestione Infermiere
layout = html.Div([

    # Breadcrumb per la navigazione
    create_breadcrumb_header("ACCESSO GESTIONE INFERMIERE", "/accesso-gestione-infermiere"),

    # Testo di introduzione per il segretario
    html.Div([ 
        html.H2(
            "Scegli un'operazione", 
            style={
                'textAlign': 'center', 
                'color': '#000000', 
                'marginTop': '50px'
            }
        ), 

        # Tre pulsanti: Aggiungi Infermiere, Crea Credenziali, Aggiungi Turni
        html.Div([
            dbc.Row([

                # Bottone per Aggiungere Informazioni Infermiere
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Aggiungi Informazioni Infermiere", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#007BFF', 'color': 'white'}),  # Bottone blu con testo bianco
                        href='/add-infermiere-info',  # Link alla pagina di aggiunta informazioni infermiere
                        style={
                            'textDecoration': 'none', 
                            'display': 'block', 
                            'height': '150px', 
                            'width': '350px'
                        }
                    ),
                    width=4,
                    className="mb-4 d-flex align-items-center justify-content-center"
                ),

                # Bottone per Creare Credenziali Infermiere
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Crea Credenziali Infermiere", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#28A745', 'color': 'white'}),  # Bottone verde con testo bianco
                        href='/add-infermiere-creds',  # Link alla pagina di creazione credenziali infermiere
                        style={
                            'textDecoration': 'none', 
                            'display': 'block', 
                            'height': '150px', 
                            'width': '350px'
                        }
                    ),
                    width=4,
                    className="mb-4 d-flex align-items-center justify-content-center"
                ),

                # Bottone per Aggiungere Turni di Lavoro
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Aggiungi Turni di Lavoro", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#FFC107', 'color': 'white'}),  # Bottone giallo con testo bianco
                        href='/add-turni-infermiere',  # Link alla pagina di aggiunta turni infermiere
                        style={
                            'textDecoration': 'none', 
                            'display': 'block', 
                            'height': '150px', 
                            'width': '350px'
                        }
                    ),
                    width=4,
                    className="mb-4 d-flex align-items-center justify-content-center"
                )

            ], className="justify-content-center")  # Centra i pulsanti orizzontalmente
        ], style={'marginTop': '50px'})  # Spazio sopra i pulsanti

    ])
])
