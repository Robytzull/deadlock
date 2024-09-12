from dash import html
import dash_bootstrap_components as dbc

layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("HOME", href="/")),
        dbc.NavItem(dbc.NavLink("CHI SIAMO", href="/CHI-SIAMO")),
        dbc.NavItem(dbc.NavLink("PRESTAZIONI", href="/PRESTAZIONI")),
        dbc.NavItem(dbc.NavLink("SEDI", href="/SEDI")),
        dbc.NavItem(dbc.NavLink("CONTATTI", href="/CONTATTI")), 
        dbc.NavItem(dbc.NavLink("LOG IN", href="/LOG-IN"))
    ],
    style={'color': '#2E8B57'},

    brand=[
        html.Img(src="/assets/casasalute.jpg", alt="Logo", height="30px"),
        html.Span("CASA della SALUTE", className="ms-2")
    ],
    brand_href="/",
    color="#7bb372",
    dark=True,
    sticky="top"  # la navbar rimane fissa
)




