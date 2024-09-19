from dash import html, dcc, callback, Input, Output, State, ALL
import dash_bootstrap_components as dbc
from pony.orm import db_session, commit
from entities.models import Infermiere, Visitainf, EsitoVisitaInfermieristica
from ponteflask import app


# Funzione per generare il layout per la gestione delle visite infermieristiche del segretario
def layout_gestione_visite_infermiere_segretario():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Gestione Visite Infermiere"),
                    
                    # Dropdown per selezionare un infermiere
                    dbc.Label("Seleziona un Infermiere"),
                    dcc.Dropdown(
                        id="infermiere-dropdown",
                        options=[],  # Le opzioni saranno popolati nel callback
                        placeholder="Seleziona un infermiere",
                    ),

                    # Sezione per mostrare le visite
                    html.Div(id='visite-infermiere-lista')
                ], width=8)
            ], justify="center")
        ])
    ])

# Callback per popolare il dropdown degli infermieri
@app.callback(
    Output('infermiere-dropdown', 'options'),
    Input('infermiere-dropdown', 'value')
)
@db_session
def populate_infermiere_dropdown(value):
    infermieri = Infermiere.select()[:]
    options = [{'label': f"Infermiere {infermiere.nome} {infermiere.cognome}", 'value': infermiere.id} for infermiere in infermieri]
    return options

# Callback per mostrare le visite dell'infermiere selezionato
@app.callback(
    Output('visite-infermiere-lista', 'children'),
    [Input('infermiere-dropdown', 'value')]
)
@db_session
def mostra_visite_infermiere(infermiere_id):
    if infermiere_id:
        visiteinf = Visitainf.select(lambda v: v.infermiere.id == infermiere_id)[:]
        if not visiteinf:
            return html.Div("Nessuna visita trovata per questo infermiere.")

        # Creiamo una lista di card per ogni visita
        visite_cards = []
        for visitainf in visiteinf:
            paziente_nome = "Paziente sconosciuto"
            if visitainf.paziente_adulto:
                paziente_nome = f"{visitainf.paziente_adulto.nome} {visitainf.paziente_adulto.cognome}"
            elif visitainf.paziente_minore:
                paziente_nome = f"{visitainf.paziente_minore.nome} {visitainf.paziente_minore.cognome} (Minore)"
            elif visitainf.paziente_adolescente:
                paziente_nome = f"{visitainf.paziente_adolescente.nome} {visitainf.paziente_adolescente.cognome} (Adolescente)"

            esito = EsitoVisitaInfermieristica.get(visitainf=visitainf)
            descrizione = esito.descrizione if esito else ""
            referto = esito.referto if esito else ""

            visita_card = dbc.Card([
                dbc.CardBody([
                    html.H5(f"Visita con {paziente_nome}", className="card-title"),
                    html.P(f"Data: {visitainf.data}", className="card-text"),
                    dbc.Label("Descrizione"),
                    dbc.Textarea(id={'type': 'descrizione-input-infseg', 'index': visitainf.id}, value=descrizione),
                    dbc.Label("Referto"),
                    dbc.Textarea(id={'type': 'referto-input-infseg', 'index': visitainf.id}, value=referto),
                    dbc.Button("Salva Referto", id={'type': 'salva-referto-btn-infseg', 'index': visitainf.id}, color="primary"),
                    html.Div(id={'type': 'referto-output-infseg', 'index': visitainf.id})
                ])
            ], className="mb-4")
            visite_cards.append(visita_card)

        return visite_cards

    return html.Div("Seleziona un infermiere per visualizzare le visite.")

# Callback per salvare il referto e la descrizione delle visite infermieristiche
@app.callback(
    Output({'type': 'referto-output-infseg', 'index': ALL}, 'children'),
    [Input({'type': 'salva-referto-btn-infseg', 'index': ALL}, 'n_clicks')],
    [State({'type': 'descrizione-input-infseg', 'index': ALL}, 'value'),
     State({'type': 'referto-input-infseg', 'index': ALL}, 'value'),
     State({'type': 'salva-referto-btn-infseg', 'index': ALL}, 'id')]
)
@db_session
def salva_referto_infermiere(n_clicks, descrizioni, referti, ids):
    output = ['' for _ in range(len(n_clicks))]

    if any(n_clicks):
        for i, n_click in enumerate(n_clicks):
            if n_click and i < len(descrizioni) and i < len(referti):
                visitainf_id = ids[i]['index']
                descrizione = descrizioni[i]
                referto = referti[i]

                visitainf = Visitainf.get(id=visitainf_id)
                if visitainf:
                    esito = EsitoVisitaInfermieristica.get(visitainf=visitainf)
                    if not esito:
                        EsitoVisitaInfermieristica(id=visitainf.id, visitainf=visitainf, infermiere=visitainf.infermiere, descrizione=descrizione, referto=referto, data=visitainf.data)
                    else:
                        esito.descrizione = descrizione
                        esito.referto = referto
                    commit()

                    output[i] = f"Referto salvato per la visita con ID: {visitainf_id}"

    return output
