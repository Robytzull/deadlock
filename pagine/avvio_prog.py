from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Importa i layout delle altre pagine
from home import layout as home_layout
from contatti import layout as contatti_layout
from area_medica import layout as area_medica_layout
from area_medicazioni import layout as area_medicazioni_layout
from area_prelievi import layout as area_prelievi_layout
from login import layout as login_layout
#from sedi import layout as sedi_layout
#from prestazioni import layout as prestazioni_layout
#from presentazione import layout as presentazione_layout


# Crea l'applicazione Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
    if pathname == '/Contatti':
        return contatti_layout
    elif pathname == '/area-medica':
        return area_medica_layout
    elif pathname == '/area-medicazioni':
        return area_medicazioni_layout
    elif pathname == '/area-prelievi':
        return area_prelievi_layout
    elif pathname == '/LOG-IN':
        return login_layout
    else:
        return home_layout  # Mostra la home come pagina predefinita

# Avvia l'applicazione
if __name__ == '__main__':
    app.run_server(debug=True)