from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from flask import Flask, session
# Importa i layout delle altre pagine
from home import layout as home_layout
from contatti import layout as contatti_layout
from area_medica import layout as area_medica_layout
from area_medicazioni import layout as area_medicazioni_layout
from area_prelievi import layout as area_prelievi_layout
from login import layout as login_layout
from accesso_medico import layout as medico_layout
from visite import layout_visite
from ponteflask import app, server
from assenze import layout_assenze
from accesso_infermiere import layout as infermiere_layout
from accesso_secretario import layout as segretario_layout
from accesso_gestione_pazienti import layout as gestione_pazienti_layout
from add_adolescenti import layout as add_adolescenti_layout
from add_minori import layout as add_minori_layout
from add_adulti import layout as add_adulti_layout
from visiteinf import layout_visite_infermiere
from calendario_inf import layout_calendario
from add_adolescenti_info import layout_add_adolescenti_info
from add_adolescenti_creds import layout_add_adolescenti_creds
from add_adulti_info import layout_add_adulti_info
from add_adulti_creds import layout_add_adulti_creds
from accesso_gestione_infirmiere import layout as gestione_infermiere_layout
from add_infermiere_info import layout_add_infermiere_info
from add_infermiere_creds import layout_add_infermiere_creds
from add_turni_infermiere import layout_add_turni_infermiere
from add_medico_info import layout_add_medico_info
from accesso_gestione_medici import layout as gestione_medici_layout
from add_medico_creds import layout_add_medico_creds
from add_medico_assenze import layout_gestione_assenze_medico
from accesso_gestione_visite import layout_gestione_visite
from gestione_visite_medico_segretario import layout_gestione_visite_medico_segretario
from gestione_visite_inf_segretario import layout_gestione_visite_infermiere_segretario
from add_minori_info import layout_add_minori_info
from acesso_paziente import layout as layout_paziente
from paziente_prenotazione_visita import layout_prenotazione_visite
#from sedi import layout as sedi_layout
#from prestazioni import layout as prestazioni_layout
#from presentazione import layout as presentazione_layout


# Crea l'applicazione Dash
#if i comment this one the app runs but without images
#app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],  suppress_callback_exceptions=True)

# Layout principale dell'app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Memorizza l'URL corrente
    html.Div(id='page-content')  # Placeholder per il contenuto della pagina
    ])

# Callback per aggiornare il layout in base al percorso URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    # Gestisci il routing tra le varie pagine
    if  pathname == '/accesso-medico':
        return medico_layout  # Show medico page if logged in as medico
    elif pathname == '/accesso-infermiere':
        return infermiere_layout
    elif pathname == '/Contatti':
        return contatti_layout
    elif pathname == '/area-medica':
        return area_medica_layout
    elif pathname == '/area-medicazioni':
        return area_medicazioni_layout
    elif pathname == '/area-prelievi':
        return area_prelievi_layout
    elif pathname == '/accesso-gestione-pazienti':
        return gestione_pazienti_layout
    elif pathname =='/accesso-gestione-infermiere':
        return gestione_infermiere_layout
    elif pathname =='/accesso-gestione-medici':
        return gestione_medici_layout
    elif pathname =='/add-infermiere-info':
        return layout_add_infermiere_info()
    elif pathname == '/add-infermiere-creds':
        return layout_add_infermiere_creds()  # Mostra la pagina per aggiungere le credenziali
    elif pathname == '/add-turni-infermiere':
        return layout_add_turni_infermiere()  # Mostra la pagina per aggiungere i turni dell'infermiere
    elif pathname == '/add-medico-info':
        return layout_add_medico_info()
    elif pathname == '/add-medico-creds':
        return layout_add_medico_creds()
    elif pathname == '/gestione-assenze-medico':
        return layout_gestione_assenze_medico()
    elif pathname == '/gestione-visite':
        return layout_gestione_visite  # Mostra la pagina con i due bottoni per gestire visite medico/infermiere
    elif pathname == '/gestione-visite-medico':
        return layout_gestione_visite_medico_segretario()  # Mostra la pagina per gestire le visite del medico
    elif pathname == '/gestione-visite-infermiere':
        return layout_gestione_visite_infermiere_segretario()
    elif pathname == '/add-minori':
        return add_minori_layout
    elif pathname == '/add-adolescenti':
        return add_adolescenti_layout
    elif pathname == '/add-minori-info':
        return layout_add_minori_info()
    elif pathname == '/add-adolescenti-info':
        return layout_add_adolescenti_info()  # Mostra la pagina per aggiungere informazioni su pazienti adolescenti
    elif pathname == '/add-adolescenti-creds':
        return layout_add_adolescenti_creds()  # Mostra la pagina per creare credenziali per adolescenti
    elif pathname == '/add-adulti':
        return add_adulti_layout
    elif pathname == '/add-adulti-info':
        return layout_add_adulti_info() # Mostra la pagina per aggiungere informazioni del paziente adulto
    elif pathname == '/add-adulti-creds':
        return layout_add_adulti_creds()  # Mostra la pagina per creare credenziali paziente adulto
    elif pathname == '/LOG-IN':
        return login_layout
    elif pathname == '/medico/visite':
        # Recupera l'ID del medico dalla sessione dopo il login
        medico_id = session.get('medico_id')

        if medico_id:
            # Se l'ID del medico esiste nella sessione, mostra la pagina delle visite
            return layout_visite()
        else:
            # Se non esiste l'ID del medico, reindirizza alla pagina di login
            return login_layout
    elif pathname == '/calendario-medico':  # Nuovo routing per il Calendario Assenze
        # Recupera l'ID del medico dalla sessione dopo il login
        medico_id = session.get('medico_id')

        if medico_id:
            # Se l'ID del medico esiste nella sessione, mostra la pagina del calendario delle assenze
            return layout_assenze()  # Funzione che definisce il layout delle assenze
        else:
            # Se non esiste l'ID del medico, reindirizza alla pagina di login
            return login_layout
    elif pathname == '/accesso-segreteria':  # Nuovo routing per il Calendario Assenze
        # Recupera l'ID del medico dalla sessione dopo il login
        segretario_id = session.get('segretario_id')

        if segretario_id:
            # Se l'ID del medico esiste nella sessione, mostra la pagina del calendario delle assenze
            return segretario_layout  # Funzione che definisce il layout delle assenze
        else:
            # Se non esiste l'ID del medico, reindirizza alla pagina di login
            return login_layout
        
    elif pathname == '/calendario-medico':  # Calendario assenze per il medico
        medico_id = session.get('medico_id')
        if medico_id:
            return layout_assenze()  # Mostra il calendario delle assenze del medico
        else:
            return login_layout
    elif pathname == '/infermiere/visite':  # Nuovo routing per visite infermieristiche
        infermiere_id = session.get('infermiere_id')
        if infermiere_id:
            return layout_visite_infermiere()  # Mostra la pagina delle visite infermieristiche
        else:
            return login_layout
    elif pathname == '/calendario-infermiere':
        infermiere_id=session.get('infermiere_id') 
        if infermiere_id:
            return layout_calendario()
        else:
            return login_layout 

    if pathname == '/accesso-paziente':
        # Verifica se il paziente è loggato
        paziente_adulto_id = session.get('paziente_id')
        paziente_adolescente_id = session.get('paziente_adolescente_id')

        if paziente_adulto_id:
            return layout_paziente  # Mostra la pagina specifica per il paziente adulto
        elif paziente_adolescente_id:
            return layout_paziente  # Mostra la pagina specifica per il paziente adolescente
        else:
            return html.Div("Errore: Nessun paziente loggato.", style={'color': 'red'})
        
    elif pathname == '/prenotazione-visite':
        paziente_id = session.get('paziente_id') or session.get('paziente_adolescente_id')
    
        if paziente_id:
            return layout_prenotazione_visite()  # Mostra la pagina di prenotazione se il paziente è loggato
        else:
            return login_layout  # Reindirizza al login se non c'è un paziente loggato    


    else:
        return home_layout  # Mostra la home come pagina predefinita

    
    
if __name__ == '__main__':
   
    app.run_server(debug=True)