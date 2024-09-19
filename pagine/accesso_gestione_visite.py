from dash import html
import dash_bootstrap_components as dbc

# Layout per la pagina Gestione Visite
layout_gestione_visite = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2("Gestione Visite", style={'textAlign': 'center', 'marginTop': '50px'}),
            ], width=12)
        ]),
        dbc.Row([
            dbc.Col([
                html.A(
                    dbc.Card([
                        dbc.CardBody(
                            html.H4("Gestione Visite Medico", className="card-title", style={'textAlign': 'center'})
                        )
                    ], style={'backgroundColor': '#007bff', 'color': 'white'}),  # Colore blu e testo bianco
                    href='/gestione-visite-medico',  # Link alla gestione visite medico
                    style={
                        'textDecoration': 'none', 
                        'display': 'block', 
                        'height': '150px', 
                        'width': '300px'
                    }
                ),
            ], width=6, className="d-flex justify-content-center mb-4"),

            dbc.Col([
                html.A(
                    dbc.Card([
                        dbc.CardBody(
                            html.H4("Gestione Visite Infermiere", className="card-title", style={'textAlign': 'center'})
                        )
                    ], style={'backgroundColor': '#28a745', 'color': 'white'}),  # Colore verde e testo bianco
                    href='/gestione-visite-infermiere',  # Link alla gestione visite infermiere
                    style={
                        'textDecoration': 'none', 
                        'display': 'block', 
                        'height': '150px', 
                        'width': '300px'
                    }
                ),
            ], width=6, className="d-flex justify-content-center mb-4"),
        ])
    ], style={'marginTop': '50px'})
])
