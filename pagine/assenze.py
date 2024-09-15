from dash import html
import dash_bootstrap_components as dbc
from pony.orm import db_session
from entities.models import Assenze
from flask import session
# Funzione per generare il layout delle assenze
def layout_assenze():
    # Recupera l'ID del medico dalla sessione
    medico_id = session.get('medico_id')

    if not medico_id:
        return html.Div("Errore: ID del medico non trovato nella sessione.")

    # Estrai le assenze del medico dal database
    with db_session:
        assenze = Assenze.select(lambda a: a.medico.id == medico_id)[:]

        # Creiamo una lista di card per ogni assenza
        assenze_cards = []
        for assenza in assenze:
            assenza_card = dbc.Card([
                dbc.CardBody([
                    html.H5(f"Assenza del {assenza.data}", className="card-title"),
                    html.P(f"Motivo: {assenza.motivo}", className="card-text")  # Se hai un campo motivo o descrizione
                ])
            ], className="mb-4")
            assenze_cards.append(assenza_card)

    return html.Div([
        html.H2("Calendario delle Assenze", style={'textAlign': 'center', 'marginTop': '20px'}),
        *assenze_cards
    ])