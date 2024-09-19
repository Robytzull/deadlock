from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from flask import session
import uuid
import datetime
from entities.models import Visita, Visitainf, PazienteAdulto, PazienteMinore, PazienteAdolescente, Medico, Infermiere, Ambulatorio, Sala

# Funzione per generare il layout della pagina di prenotazione
def layout_prenotazione_visite():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Prenota una Visita"),
                    dbc.Form([
                        # Dropdown per selezionare il paziente (se il paziente adulto ha dei minori associati)
                        dbc.Label("Seleziona il Paziente"),
                        dcc.Dropdown(
                            id="dropdown-paziente",
                            options=[],  # Popolato dinamicamente
                            placeholder="Seleziona il paziente"
                        ),
                        
                        # Dropdown per il tipo di visita (medica o infermieristica)
                        dbc.Label("Tipo di Visita"),
                        dcc.Dropdown(
                            id="dropdown-tipo-visita",
                            options=[
                                {'label': 'Visita Medica', 'value': 'medico'},
                                {'label': 'Visita Infermieristica', 'value': 'infermiere'}
                            ],
                            placeholder="Seleziona il tipo di visita"
                        ),
                        
                        # Dropdown per il regime della visita (pediatrica o per adulti)
                        dbc.Label("Regime della Visita"),
                        dcc.Dropdown(
                            id="dropdown-regime-visita",
                            options=[
                                {'label': 'Pediatrica', 'value': 'pediatrica'},
                                {'label': 'Per Adulti', 'value': 'adulti'}
                            ],
                            placeholder="Seleziona il regime"
                        ),

                        # Campo per la data della visita
                        dbc.Label("Data della Visita"),
                        dbc.Input(id="input-data-visita", type="date"),

                        # Dropdown per l'orario della visita
                        dbc.Label("Ora della Visita"),
                        dcc.Dropdown(id="dropdown-orario-visita", options=[], placeholder="Seleziona un orario"),

                        # Dropdown per la tipologia infermieristica (prelievo o medicazione)
                        dbc.Label("Tipologia Infermieristica"),
                        dcc.Dropdown(
                            id="dropdown-tipologia-infermieristica",
                            options=[
                                {'label': 'Prelievo', 'value': 'prelievo'},
                                {'label': 'Medicazione', 'value': 'medicazione'}
                            ],
                            placeholder="Seleziona la tipologia",
                            style={'display': 'none'}  # Nascondilo all'inizio
                        ),

                        # Dropdown per selezionare il medico o infermiere
                        dbc.Label("Seleziona Medico o Infermiere"),
                        dcc.Dropdown(id="dropdown-seleziona-personale", options=[], placeholder="Seleziona un Medico o Infermiere"),

                        # Pulsante per confermare la prenotazione
                        dbc.Button("Conferma Prenotazione", id="submit-prenotazione", color="primary", className="mt-3"),

                        # Spazio per mostrare eventuali messaggi di errore o conferma
                        html.Div(id="output-message-prenotazione", className="mt-3"),
                        html.Div(id="output-availability", className="mt-3")  # Per mostrare la disponibilità
                    ])
                ], width=6)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown dei pazienti (adulti, minori o adolescenti)
@callback(
    Output('dropdown-paziente', 'options'),
    Input('dropdown-paziente', 'value')
)
@db_session
def populate_pazienti_dropdown(value):
    paziente_adulto_id = session.get('paziente_id')
    paziente_adolescente_id = session.get('paziente_adolescente_id')

    options = []
    
    # Se il paziente è un adulto
    if paziente_adulto_id:
        paziente_adulto = PazienteAdulto.get(id=paziente_adulto_id)
        options.append({'label': f"{paziente_adulto.nome} {paziente_adulto.cognome} (Adulto)", 'value': paziente_adulto.id})
        
        # Aggiungi i minori associati al paziente adulto
        for minore in paziente_adulto.responsabili_minori:
            options.append({'label': f"{minore.nome} {minore.cognome} (Minore)", 'value': minore.id})
    
    # Se il paziente è un adolescente
    elif paziente_adolescente_id:
        paziente_adolescente = PazienteAdolescente.get(id=paziente_adolescente_id)
        options.append({'label': f"{paziente_adolescente.nome} {paziente_adolescente.cognome} (Adolescente)", 'value': paziente_adolescente.id})

    return options

# Callback per mostrare la tipologia infermieristica solo se selezionato il tipo "infermiere"
@callback(
    Output('dropdown-tipologia-infermieristica', 'style'),
    Input('dropdown-tipo-visita', 'value')
)
def show_tipologia_infermieristica(tipo_visita):
    if tipo_visita == 'infermiere':
        return {'display': 'block'}
    else:
        return {'display': 'none'}

# Callback per popolare gli orari disponibili
@callback(
    Output('dropdown-orario-visita', 'options'),
    Input('input-data-visita', 'value'),
    State('dropdown-tipo-visita', 'value')
)
@db_session
def populate_orari_dropdown(data_visita, tipo_visita):
    if not data_visita:
        return []

    # Lista di orari disponibili (personalizzabile)
    orari_disponibili = ['09:00', '10:00', '11:00', '14:00', '15:00']

    return [{'label': orario, 'value': orario} for orario in orari_disponibili]

# Callback per gestire la disponibilità di medici o infermieri
@callback(
    [Output('dropdown-seleziona-personale', 'options'),
     Output('output-availability', 'children')],  # Mostra la disponibilità
    [Input('dropdown-tipo-visita', 'value'),
     Input('input-data-visita', 'value'),
     Input('dropdown-orario-visita', 'value')]
)
@db_session
def populate_personale_dropdown(tipo_visita, data_visita, orario_visita):
    if not data_visita or not orario_visita:
        return [], "Seleziona una data e un orario per vedere la disponibilità."

    data_visita = datetime.datetime.strptime(data_visita, '%Y-%m-%d').date()

    if tipo_visita == 'medico':
        # Verifica quanti ambulatori sono già occupati
        ambulatori_occupati = Visita.select(lambda v: v.data == data_visita and v.orario == orario_visita).count()
        max_ambulatori = 3  # Numero massimo di ambulatori disponibili per visite mediche

        if ambulatori_occupati >= max_ambulatori:
            return [], "Tutti gli ambulatori sono già prenotati per questa data e ora."

        # Filtra i medici che non hanno già una prenotazione nella stessa data e ora
        medici_disponibili = Medico.select(lambda m: not Visita.exists(lambda v: v.medico == m and v.data == data_visita and v.orario == orario_visita))
        
        if medici_disponibili:
            options = [{'label': f"Dr. {medico.nome} {medico.cognome}", 'value': medico.id} for medico in medici_disponibili]
            return options, f"Medici disponibili per questo orario. Ambulatori liberi: {max_ambulatori - ambulatori_occupati}"
        else:
            return [], "Tutti i medici sono già prenotati per questa data e ora."

    elif tipo_visita == 'infermiere':
        # Verifica la disponibilità delle sale (prelievi e medicazioni)
        infermieri_disponibili = Infermiere.select(lambda i: not Visitainf.exists(lambda v: v.infermiere == i and v.data == data_visita and v.orario == orario_visita))
        
        if infermieri_disponibili:
            options = [{'label': f"{infermiere.nome} {infermiere.cognome}", 'value': infermiere.id} for infermiere in infermieri_disponibili]
            return options, "Infermieri disponibili per questo orario."
        else:
            return [], "Tutti gli infermieri sono già prenotati per questa data e ora."

    return [], "Errore nella selezione del personale."

# Callback per gestire la conferma della prenotazione
@callback(
    Output('output-message-prenotazione', 'children'),
    Input('submit-prenotazione', 'n_clicks'),
    [State('dropdown-paziente', 'value'),
     State('dropdown-tipo-visita', 'value'),
     State('dropdown-regime-visita', 'value'),
     State('input-data-visita', 'value'),
     State('dropdown-orario-visita', 'value'),
     State('dropdown-tipologia-infermieristica', 'value'),
     State('dropdown-seleziona-personale', 'value')]
)
@db_session
def conferma_prenotazione(n_clicks, paziente_id, tipo_visita, regime_visita, data_visita, orario_visita, tipologia_infermieristica, personale_id):
    if n_clicks is None:
        return ''

    if not all([paziente_id, tipo_visita, regime_visita, data_visita, orario_visita, personale_id]):
        return 'Errore: Tutti i campi devono essere compilati.'

    # Converti la data della visita
    data_visita = datetime.datetime.strptime(data_visita, '%Y-%m-%d').date()

    paziente_adulto = PazienteAdulto.get(id=paziente_id)
    paziente_minore = PazienteMinore.get(id=paziente_id)
    paziente_adolescente = PazienteAdolescente.get(id=paziente_id)

    # Prenotazione per visita medica
    if tipo_visita == 'medico':
        medico = Medico.get(id=personale_id)
        ambulatorio = Ambulatorio.select(lambda a: Visita.select(lambda p: p.ambulatorio == a and p.data == data_visita).count() < 3).first()

        if ambulatorio:
            nuova_visita = Visita(
                id=str(uuid.uuid4()), 
                data=data_visita, 
                orario=orario_visita,
                medico=medico,
                ambulatorio=ambulatorio,
                paziente_adulto=paziente_adulto if paziente_adulto else None,
                paziente_minore=paziente_minore if paziente_minore else None,
                paziente_adolescente=paziente_adolescente if paziente_adolescente else None
            )
            commit()
            return f"La tua prenotazione per una visita medica con il Dr. {medico.nome} {medico.cognome} è stata confermata per il {data_visita} alle {orario_visita}."
        else:
            return "Non ci sono ambulatori disponibili per questa data."

    # Prenotazione per prelievo o medicazione
    elif tipo_visita == 'infermiere':
        infermiere = Infermiere.get(id=personale_id)
        sala = Sala.select(lambda s: Visitainf.select(lambda p: p.sala == s and p.data == data_visita).count() < 1).first()

        if sala and tipologia_infermieristica:
            nuova_visita_inf = Visitainf(
                id=str(uuid.uuid4()), 
                data=data_visita, 
                orario=orario_visita,  # Assicurati che l'orario venga salvato
                infermiere=infermiere,
                sala=sala,
                tipologia=tipologia_infermieristica,
                paziente_adulto=paziente_adulto if paziente_adulto else None,
                paziente_minore=paziente_minore if paziente_minore else None,
                paziente_adolescente=paziente_adolescente if paziente_adolescente else None
            )
            commit()
            return f"La tua prenotazione per un {tipologia_infermieristica} con {infermiere.nome} {infermiere.cognome} è stata confermata per il {data_visita} alle {orario_visita}."
        else:
            return "Non ci sono sale disponibili per questa data o tipologia non selezionata."






