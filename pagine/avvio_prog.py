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
    else:
        return home_layout  # Mostra la home come pagina predefinita
if __name__ == '__main__':
   
    app.run_server(debug=True)