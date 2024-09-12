from dash import html
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

layout = html.Div([

    create_breadcrumb_header("CONTATTI", "/Contatti"),

    html.Div([
        html.H2("Per maggiori informazioni", style={'textAlign': 'center', 'color': '#000000'}),
        
        # Didascalia con gli orari della segreteria
        html.P(
            "La nostra segreteria è disponibile per rispondere alle tue chiamate dal lunedì al venerdì, dalle 8:00 alle 18:00, "
            "altrimenti è possibile contattarci anche via email o compilare il modulo online per richieste non urgenti.",
            style={'textAlign': 'center', 'marginTop': 20, 'marginBottom': 40, 'color': '#555'}
        ),
        
        # Contenuto dei rettangoli "Chiamaci", "Compila il form online", e "Invia una Email"
        html.Div([
            dbc.Row([
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Chiamaci: 0432991122", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='tel:0432991122',  # per aprire la rubrica del telefono
                        style={'textDecoration': 'none', 'display': 'block', 'height': '150px', 'width': '450px'}  # Larghezza aumentata
                    ),
                    width=4,  # Ogni colonna occupa un terzo della larghezza della riga
                    className="mb-4",
                    style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'padding': '1px'}
                ),
                
                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Compila il form online", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='/Compila-il-form-online',  # Link per aprire la pagina del modulo di contatto
                        style={'textDecoration': 'none', 'display': 'block', 'height': '150px', 'width': '450px'}  # Larghezza aumentata
                    ),
                    width=4,  # Ogni colonna occupa un terzo della larghezza della riga
                    className="mb-4",
                    style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'padding': '1px'}
                ),

                dbc.Col(
                    html.A(
                        dbc.Card([
                            dbc.CardBody(
                                html.H4("Invia una Email", className="card-title", style={'textAlign': 'center'})
                            )
                        ], style={'backgroundColor': '#7bb372', 'color': 'white'}),  # Colore verde e testo bianco
                        href='mailto:info@aziendasanitaria.xyz',  # Apre il client di posta elettronica
                        style={'textDecoration': 'none', 'display': 'block', 'height': '150px', 'width': '450px'}  # Larghezza aumentata
                    ),
                    width=4,  # Ogni colonna occupa un terzo della larghezza della riga
                    className="mb-4",
                    style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'padding': '1px'}
                )
            ], justify='center')  # Centra i rettangoli orizzontalmente
        ], style={'marginTop': 30})  # Ridotto lo spazio sopra i rettangoli
    ]),
])
