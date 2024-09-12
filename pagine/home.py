from dash import html , Dash
import dash_bootstrap_components as dbc
#from comp import navbar

#app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# Layout per la pagina Home
layout = html.Div([
    #navbar,
    # Sezione di immagini a scorrimento (carosello)
    html.Div([
        dbc.Carousel(
            items=[
                {"key": "1", "src": "/assets/struttura.png", "alt": "Immagine 1", "img_style": {"width": "100%", "height": "400px"}},
                {"key": "2", "src": "/assets/imm.jpeg", "alt": "Immagine 2", "img_style": {"width": "100%", "height": "400px"}},
                {"key": "3", "src": "/assets/casasalute.jpg", "alt": "Immagine 3", "img_style": {"width": "100%", "height": "400px"}}
            ],
            controls=True,
            indicators=True,
            interval=3000  # cambia immagine ogni 3 secondi
        )
    ], style={'marginTop': 20}),
    
    # Barra di testo "Chi siamo"
    html.Div([
        html.H2("CASA della SALUTE", style={'textAlign': 'center', 'color': '#000000'}),
        html.P(
            "La Casa della Salute è una struttura sanitaria ambulatoriale privata, polispecialistica, a media complessità, "
            "attiva nei settori della prevenzione, diagnosi e cura. È accreditata al Servizio Sanitario (cioè accessibile, "
            "nell’ambito della programmazione regionale, anche con l’impegnativa del Medico di Famiglia ed il pagamento del solo ticket, "
            "ove previsto) per la Diagnostica per Immagini, la Medicina dello Sport di 1’ livello, l'Endocrinologia /Diabetologia e la Dermatologia.",
            style={'textAlign': 'center'}
        )
    ], style={'marginTop': 40}),
    
    # Sezione rettangoli colorati: Area Medica, Area Prelievi, Area Medicazioni
    html.Div([
        dbc.Row([
            dbc.Col(
                html.A(
                    dbc.Card([
                        dbc.CardBody(
                            html.H4("Area Medica", className="card-title", style={'textAlign': 'center'})
                        )
                    ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde chiaro e testo bianco
                    href='/area-medica',  # Link per aprire la pagina Area Medica
                    style={
                        'textDecoration': 'none',  # Rimuove la sottolineatura del link
                        'display': 'block',  # Assicura che il link copra tutta la colonna
                        'height': '150px', 'width': '100%'
                    }
                ),
                width=4, 
                className="mb-4",
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center'
                }
            ),
            
            dbc.Col(
                html.A(
                    dbc.Card([
                        dbc.CardBody(
                            html.H4("Area Prelievi", className="card-title", style={'textAlign': 'center'})
                        )
                    ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde chiaro e testo bianco
                    href='/area-prelievi',  # Link per aprire la pagina Area Prelievi
                    style={
                        'textDecoration': 'none',  # Rimuove la sottolineatura del link
                        'display': 'block',  # Assicura che il link copra tutta la colonna
                        'height': '150px', 'width': '100%'
                    }
                ),
                width=4, 
                className="mb-4",
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center'
                }
            ),
            
            dbc.Col(
                html.A(
                    dbc.Card([
                        dbc.CardBody(
                            html.H4("Area Medicazioni", className="card-title", style={'textAlign': 'center'})
                        )
                    ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde chiaro e testo bianco
                    href='/area-medicazioni',  # Link per aprire la pagina Area Medicazioni
                    style={
                        'textDecoration': 'none',  # Rimuove la sottolineatura del link
                        'display': 'block',  # Assicura che il link copra tutta la colonna
                        'height': '150px', 'width': '100%'
                    }
                ),
                width=4, 
                className="mb-4",
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center'
                }
            )
        ], justify='center')  # Centra i rettangoli orizzontalmente
    ], style={'marginTop': 40, 'marginLeft': '5%', 'marginRight': '5%'}),  # Maggiore distanziamento dai margini

    # Frase divisoria per informare sugli accessi
    html.Div(
        html.P(
            "Per prenotare visite, ritirare referti o consultare lo storico delle visite, effettua il login o crea un account.",
            style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40, 'color': '#333'}
        ),
    ),

    # Sezione Login
    html.Div([
        dbc.Row([
            dbc.Col(
                html.A(
                    dbc.Card([
                        dbc.CardBody(
                            html.H4("Log in", className="card-title", style={'textAlign': 'center'})
                        )
                    ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde chiaro e testo bianco
                    href='/LOG-IN',  # Link per aprire la pagina Login
                    style={
                        'textDecoration': 'none',
                        'display': 'block',
                        'height': '150px', 'width': '100%'
                    }
                ),
                width=4,
                className="mb-4",
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center'
                }
            )
        ], justify='center')  # Centra il rettangolo orizzontalmente
    ], style={'marginTop': 40, 'marginLeft': '5%', 'marginRight': '5%'}),

    # Didascalia divisoria per separare Login dai Contatti
    html.Div([
        html.P(
            "Se hai bisogno di ulteriori informazioni o desideri parlare direttamente con noi, visita la sezione sottostante.",
            style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40, 'color': '#333'}
        )
    ]),

    # Sezione Contatti
    html.Div([
        dbc.Row([
            dbc.Col(
                html.A(
                    dbc.Card([
                        dbc.CardBody(
                            html.H4("Contatti", className="card-title", style={'textAlign': 'center'})
                        )
                    ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde chiaro e testo bianco
                    href='/Contatti',  # Link per aprire la pagina Contatti
                    style={
                        'textDecoration': 'none',
                        'display': 'block',
                        'height': '150px', 'width': '100%'
                    }
                ),
                width=4,
                className="mb-4",
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center'
                }
            )
        ], justify='center')  # Centra i rettangoli orizzontalmente
    ], style={'marginTop': 40, 'marginLeft': '5%', 'marginRight': '5%'})
])

#if __name__ == '__main__':
    #app.run_server(debug=True)