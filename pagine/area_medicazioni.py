from dash import html
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

# Layout per l'Area Medicazioni
layout = html.Div([
    # Breadcrumb per navigazione
     create_breadcrumb_header("AREA MEDICAZIONI", "/Area-Medicazioni"),

    # Titolo principale
    html.H1("AREA MEDICAZIONI", style={'textAlign': 'center', 'marginTop': '20px'}),

    # Sezione principale del contenuto
    html.Div([
        html.P(
            "Benvenuto nella sezione dedicata all'Area Medicazioni. Qui puoi trovare informazioni sui servizi di medicazione che offriamo, inclusi i tipi di trattamenti e le procedure che seguiamo per garantire la tua sicurezza e comfort. La nostra Area Medicazioni è attrezzata per eseguire una vasta gamma di trattamenti con la massima precisione.",
            style={'textAlign': 'center', 'marginBottom': '20px'}
        ),

        # Immagine (assicurati che il percorso dell'immagine sia corretto e che l'immagine esista nella cartella assets)
        # html.Img(src="/assets/area_medicazioni.jpg", style={'display': 'block', 'margin': '20px auto', 'maxWidth': '100%'}),

        # Servizi di medicazione
        html.Div([
            html.H2("Servizi di Medicazione", style={'textAlign': 'center', 'marginBottom': '20px'}),
            html.Ul([
                html.Li("Trattamenti per ferite e lesioni cutanee"),
                html.Li("Medicazioni avanzate per ulcere e piaghe da decubito"),
                html.Li("Gestione e cura di infezioni cutanee"),
                html.Li("Consulenza pre e post trattamento"),
            ], style={'textAlign': 'center', 'listStyleType': 'none', 'padding': '0'}),
        ], style={'marginTop': '20px'}),

        # Orari di apertura
        html.Div([
            html.H3("Orari di Apertura", style={'textAlign': 'center', 'marginBottom': '20px'}),
            html.Ul([
                html.Li("Lunedì - Venerdì: 08:00 - 18:00"),
                html.Li("Sabato: 09:00 - 13:00"),
                html.Li("Domenica: Chiuso"),
            ], style={'textAlign': 'center', 'listStyleType': 'none', 'padding': '0'}),
        ], style={'marginTop': '20px'}),

        # Informazioni per prenotazioni
        html.Div([
            html.H3("Prenotazioni", style={'textAlign': 'center', 'marginBottom': '20px'}),
            html.P(
                "Per prenotare un trattamento o per ulteriori informazioni, "
                "puoi contattarci tramite il nostro numero di telefono o email, "
                "oppure utilizzare il nostro sistema di prenotazione online.",
                style={'textAlign': 'center'}
            ),
        ], style={'marginTop': '20px'}),
    ], style={'maxWidth': '800px', 'margin': '0 auto'})
])
