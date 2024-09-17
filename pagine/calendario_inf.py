from dash import html
import dash_bootstrap_components as dbc
from pony.orm import db_session
from entities.models import TurniInfermiere
from flask import session
# Funzione per generare il layout delle assenze
def layout_calendario():
    # Recupera l'ID del medico dalla sessione
    infermiere_id = session.get('infermiere_id')

    if not infermiere_id:
        return html.Div("Errore: ID del medico non trovato nella sessione.")

    # Estrai le assenze del medico dal database
    with db_session:
        turni = TurniInfermiere.select(lambda a: a.infermiere.id == infermiere_id)[:]

        # Creiamo una lista di card per ogni assenza
        turni_cards = []
        for turno in turni:
            turni_card = dbc.Card([
                dbc.CardBody([
                    html.H5(f"Turno del giorno: {turno.data_inizio}", className="card-title"),
                    html.P(f"Orario di inizio: {turno.orario_inizio}", className="card-text"),
                    html.P(f"Orario di fine: {turno.orario_fine}", className="card-text")
                    #html.P(f"Motivo: {turno.motivo}", className="card-text")  # Se hai un campo motivo o descrizione
                ])
            ], className="mb-4")
            turni_cards.append(turni_card)

    return html.Div([
        html.H2("Calendario dei Turni", style={'textAlign': 'center', 'marginTop': '20px'}),
        *turni_cards
    ])