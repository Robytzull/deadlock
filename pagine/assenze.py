from dash import html
import dash_bootstrap_components as dbc
from pony.orm import db_session
from entities.models import Assenze, Sostituzione
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
            # Cerca se esiste una sostituzione per questa assenza
            sostituzione = Sostituzione.get(medico_sostituito=assenza.medico)

            # Mostra il nome del medico sostituto se esiste
            if sostituzione:
                medico_sostituto = f"{sostituzione.medico_sostituto.nome} {sostituzione.medico_sostituto.cognome}"
            else:
                medico_sostituto = "Nessun sostituto"

            # Crea una card per ogni assenza
            assenza_card = dbc.Card([
                dbc.CardBody([
                    html.H5(f"Assenza del {assenza.data}", className="card-title"),
                    html.P(f"Motivo: {assenza.motivo}", className="card-text"),
                    html.P(f"Sostituto: {medico_sostituto}", className="card-text")  # Mostra il sostituto se esiste
                ])
            ], className="mb-4")
            assenze_cards.append(assenza_card)

    return html.Div([
        html.H2("Calendario delle Assenze", style={'textAlign': 'center', 'marginTop': '20px'}),
        *assenze_cards  # Aggiungi tutte le card delle assenze
    ])