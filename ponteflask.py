from dash import Dash
import dash_bootstrap_components as dbc
from flask import Flask

# Crea un'app Flask e integra Dash
server = Flask(__name__)  # L'app Flask
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])  # L'app Dash legata a Flask

# Aggiungi altre configurazioni dell'app o del server se necessario

