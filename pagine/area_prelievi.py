from dash import html
import dash_bootstrap_components as dbc  #
from compo.breadcrumb_header import create_breadcrumb_header


# Layout per l'Area Prelievi
layout = html.Div([

    create_breadcrumb_header("AREA PRELIEVI", "/area-prelievi"),

    html.H1("Area Prelievi", style={'textAlign': 'center', 'marginTop': 20}),
    
    html.Div([
        html.P(
            "Benvenuto nella sezione dedicata all'Area Prelievi. Qui puoi trovare informazioni sui servizi di prelievo che offriamo, inclusi i tipi di test e le procedure che seguiamo per garantire la tua sicurezza e comfort. La nostra Area Prelievi è attrezzata per eseguire una vasta gamma di test diagnostici con la massima precisione.",
            style={'textAlign': 'center'}
        ),
        html.Img(src="/assets/area_prelievi.jpg", style={'display': 'block', 'margin': '20px auto', 'maxWidth': '100%'}),
        
        html.Div([
            html.H2("Servizi di Prelievo", style={'textAlign': 'center'}),
            html.Ul([
                html.Li("Prelievi di sangue per analisi cliniche"),
                html.Li("Test di diagnostica per la ricerca di patologie"),
                html.Li("Prelievi per analisi specialistiche su richiesta"),
                html.Li("Servizi di consulenza pre e post prelievo"),
            ], style={'textAlign': 'center', 'listStyleType': 'none', 'padding': 0}),
        ], style={'marginTop': 20}),
        
        html.Div([
            html.H3("Orari di Apertura", style={'textAlign': 'center'}),
            html.P(
                "Lunedì - Venerdì: 07:00 - 15:00\n"
                "Sabato: 08:00 - 12:00\n"
                "Domenica: Chiuso",
                style={'textAlign': 'center'}
            ),
        ], style={'marginTop': 20}),
        
        html.Div([
            html.H3("Prenotazioni", style={'textAlign': 'center'}),
            html.P(
                "Per prenotare un prelievo o per ulteriori informazioni, "
                "puoi contattarci tramite il nostro numero di telefono o email, "
                "oppure utilizzare il nostro sistema di prenotazione online.",
                style={'textAlign': 'center'}
            ),
        ], style={'marginTop': 20}),
    ])
])
