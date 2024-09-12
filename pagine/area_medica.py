from dash import html
import dash_bootstrap_components as dbc
from compo.breadcrumb_header import create_breadcrumb_header

# Layout per l'Area Medica
layout = html.Div([

    create_breadcrumb_header("AREA MEDICA", "/area-medica"),

    html.H1("AREA MEDICA", style={'textAlign': 'center', 'marginTop': 20}),
    
    html.Div([
        html.P(
            "Benvenuto nella sezione dedicata all'Area Medica. Qui puoi trovare informazioni sui servizi medici che offriamo, compresi dettagli sui tipi di visite, diagnosi e trattamenti disponibili. La nostra Area Medica è progettata per fornire assistenza completa e di alta qualità a tutti i pazienti.",
            style={'textAlign': 'center'}
        ),
        # html.Img(src="/assets/area_medica.jpg", style={'display': 'block', 'margin': '20px auto', 'maxWidth': '100%'}),
        
        html.Div([
            html.H2("Servizi Offerti", style={'textAlign': 'center'}),
            html.Ul([
                html.Li("Visite specialistiche in diverse branche della medicina"),
                html.Li("Diagnosi avanzate e trattamenti mirati"),
                html.Li("Servizi di consulenza e follow-up"),
                html.Li("Accesso a tecnologie diagnostiche all'avanguardia"),
            ], style={'textAlign': 'center', 'listStyleType': 'none', 'padding': 0}),
        ], style={'marginTop': 20}),
        
        html.Div([
            html.H3("Orari di Apertura", style={'textAlign': 'center'}),
            html.Ul([
                html.Li("Lunedì - Venerdì: 08:00 - 18:00"),
                html.Li("Sabato: 09:00 - 13:00"),
                html.Li("Domenica: Chiuso"),
            ], style={'textAlign': 'center', 'listStyleType': 'none', 'padding': 0}),
        ], style={'marginTop': 20}),
        
        html.Div([
            html.H3("Prenotazioni", style={'textAlign': 'center'}),
            html.P(
                "Per prenotare una visita o richiedere ulteriori informazioni, "
                "ti preghiamo di contattarci tramite il nostro numero di telefono o email, "
                "oppure utilizzare il nostro sistema di prenotazione online.",
                style={'textAlign': 'center'}
            ),
        ], style={'marginTop': 20}),
    ], style={'textAlign': 'center'})
])

