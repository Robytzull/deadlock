from dash import Dash
import dash_bootstrap_components as dbc
from flask import Flask


# Crea un'app Flask e integra Dash
server = Flask(__name__)  # L'app Flask
server.secret_key = '8f42a73054b1749f8f58848be5e6502c'
print(f"Flask secret key: {server.secret_key}")

app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)  # L'app Dash legata a Flask

# Aggiungi altre configurazioni dell'app o del server se necessario

