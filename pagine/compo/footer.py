from dash import html
import dash_bootstrap_components as dbc

# Layout per il footer
layout = html.Footer(
    dbc.Container(
        [
            # Logo e Titolo
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Img(src="/assets/casasalute.jpg", alt="Logo", height="30px"),  # Logo
                        html.Span("CASA della SALUTE", className="ms-2", style={'fontWeight': 'bold', 'fontSize': '20px', 'color': 'white'})  # Titolo
                    ], className="text-center", style={'marginBottom': '20px'})  # Centrato e con margine inferiore
                )
            ),
            # Testo copyright
            dbc.Row(
                dbc.Col(
                    html.P([
                        html.Span("© 2024 Casa della Salute - ", style={'fontWeight': 'bold', 'color': 'white'}),
                        html.A("Privacy", href="/privacy", style={'color': 'white', 'textDecoration': 'underline', 'marginRight': '10px'}),
                        html.A("Cookie", href="/cookie", style={'color': 'white', 'textDecoration': 'underline'})
                    ],
                        className="text-center",
                        style={'margin': '10px 0', 'color': 'white'}
                    )
                )
            )
        ],
        fluid=True,
        style={'backgroundColor': '#7bb372', 'padding': '20px'}  # Sfondo verde
    ),
    className="mt-4"  # Margine superiore per distanziarlo dal contenuto
)

