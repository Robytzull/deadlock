from dash import html

def create_breadcrumb_header(page_name, page_href):
    return html.Div([
        # SEZIONE SINISTRA - BREADCRUMB
        html.Div([
            html.A("HOME", href="/", style={'color': '#666666', 'textDecoration': 'none', 'textAlign': 'left'}),
            html.Span(" > "),
            html.A(page_name, href=page_href, style={'color': '#008080', 'fontWeight': 'bold', 'textDecoration': 'none'}),
        ], 
        style={'textAlign': 'left', 'paddingLeft': '20px'}),
        
        # SEZIONE DESTRA - TESTO E BOTTONE
        html.Div([
            # Contenitore principale per il testo e il bottone
            html.Div([
                html.H2("Accedi ai nostri servizi online", 
                    style={'marginTop': '20px', 'marginBottom': '2px', 'color': '#666666'}
                ),
                html.P("Veloci, comodi, sicuri", 
                    style={'marginBottom': '20px', 'marginTop': '2px', 'color': '#666666'}
                )
            ], 
            style={'textAlign': 'right', 'paddingRight': '20px'}),

            # SEZIONE DEL BOTTONE
            html.Div(
                html.A(
                    "PRENOTA ONLINE", 
                    href="/prenotazioni", 
                    style={
                        'display': 'block',
                        'width': '200px',
                        'textAlign': 'center',
                        'padding': '10px',
                        'backgroundColor': '#7bb372',
                        'color': 'white',
                        'textDecoration': 'none',
                        'border': '2px solid #2E8B57',
                        'borderRadius': '5px',
                        'marginLeft': 'auto',
                        'marginRight': 'auto'
                    }
                ), 
                style={'textAlign': 'center', 'fontSize': '20px', 'fontWeight': 'bold'}
            )
        ], 
        style={
            'display': 'flex',  # Usa il layout flessibile
            'alignItems': 'center',  # Allinea verticalmente al centro
            'justifyContent': 'center',  # Centra l'intero contenuto
            'maxWidth': '80%',
            'padding': '20px',
        })
    ], 
    style={
        'display': 'flex',  # Usa il layout flessibile
        'alignItems': 'center',  # Allinea verticalmente al centro
        'justifyContent': 'space-between',  # Spazio tra le due sezioni
        'maxWidth': '80%',
        'padding': '20px',
        'margin': '0 auto'  # Centra l'intera sezione orizzontalmente
    })
