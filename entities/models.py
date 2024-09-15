from pony.orm import *
from datetime import date

db = Database()

# Classe Sostituzione
class Sostituzione(db.Entity):
    _table_ = 'sostituzioni'
    medico_sostituto = Required('Medico', reverse='sostituzioni_sostituto')
    medico_sostituito = Required('Medico', reverse='sostituzioni_sostituito')

# Classe Medico
class Medico(db.Entity):
    _table_ = 'medici'
    id = PrimaryKey(str)
    CF = Required(str, unique=True)
    nome = Required(str)
    cognome = Required(str)
    data_nascita = Required(date)
    luogo_nascita = Required(str)
    mail = Required(str)    
    specialita = Optional(str)

    credenziali = Optional('CredenzialiPersonale', reverse='medico')
    ferie = Set('Assenze', reverse='medico')
    turni = Set('TurniMedico', reverse='medico')
    report_visite = Set('ReportVisite', reverse='medico')

    sostituzioni_sostituto = Set(Sostituzione, reverse='medico_sostituto')
    sostituzioni_sostituito = Set(Sostituzione, reverse='medico_sostituito')
    
    visite = Set('Visita', reverse='medico')
    pazienti_adulti = Set('PazienteAdulto', reverse='medico')
    pazienti_minori = Set('PazienteMinore', reverse='medico')
    pazienti_adolescenti = Set('PazienteAdolescente', reverse='medico')
    prenotazioni_medico = Set('Prenotazione', reverse='medico')
    esiti_medici = Set('EsitoVisitaMedica', reverse='medico')

# Classe Infermiere
class Infermiere(db.Entity):
    _table_ = 'infermieri'
    id = PrimaryKey(str)
    CF = Required(str, unique=True)
    nome = Required(str)
    cognome = Required(str)
    data_nascita = Required(date)
    luogo_nascita = Required(str)
    mail = Required(str)
    credenziali = Optional('CredenzialiPersonale', reverse='infermiere')
    turni = Set('TurniInfermiere', reverse='infermiere')
    sala = Optional('Sala', reverse='infermieri')
    pazienti_adulti = Set('PazienteAdulto', reverse='infermiere')
    pazienti_minori = Set('PazienteMinore', reverse='infermiere')
    pazienti_adolescenti = Set('PazienteAdolescente', reverse='infermiere')
    prenotazioni_infermiere = Set('Prenotazione', reverse='infermiere')
    visite = Set('Visita', reverse='infermiere')
    visitainf = Set('Visitainf', reverse='infermiere')
    esiti_infermieristici = Set('EsitoVisitaInfermieristica', reverse='infermiere')
    report_visite = Set('ReportVisite', reverse='infermiere')

# Classe Segreteria
class Segreteria(db.Entity):
    _table_ = 'segretari'
    id = PrimaryKey(str)
    CF = Required(str, unique=True)
    nome = Required(str)
    cognome = Required(str)
    data_nascita = Required(date)
    luogo_nascita = Required(str)
    mail = Required(str)
    credenziali = Optional('CredenzialiPersonale', reverse='segreteria')

# Classe PazienteAdulto
class PazienteAdulto(db.Entity):
    _table_ = 'pazienti_adulti'
    id = PrimaryKey(str)
    CF = Required(str, unique=True)
    nome = Required(str)
    cognome = Required(str)
    data_nascita = Required(date)
    luogo_nascita = Required(str)
    mail = Required(str)
    credenziali = Optional('CredenzialiPazienteAdulto', reverse='paziente')
    
    responsabili_adolescenti = Set('PazienteAdolescente', reverse='tutor')
    responsabili_minori = Set('PazienteMinore', reverse='responsabile_adulto')
    
    medico = Optional(Medico, reverse='pazienti_adulti')
    infermiere = Optional(Infermiere, reverse='pazienti_adulti')
    prenotazioni = Set('Prenotazione', reverse='paziente_adulto')
    visite = Set('Visita', reverse='paziente_adulto')
    visitainf = Set('Visitainf', reverse='paziente_adulto')
    servizioSanitario = Set('ServizioSanitario', reverse='pazienti_adulti')
    report_servizioSanitario = Set('ReportServizioSanitario', reverse='paziente_adulto')
    report_visite = Set('ReportVisite', reverse='paziente_adulto')

# Classe PazienteMinore
class PazienteMinore(db.Entity):
    _table_ = 'pazienti_minori'
    id = PrimaryKey(str)
    CF = Required(str, unique=True)
    nome = Required(str)
    cognome = Required(str)
    data_nascita = Required(date)
    luogo_nascita = Required(str)
    mail_responsabile = Required(str)  
    responsabile_adulto = Required(PazienteAdulto, reverse='responsabili_minori')
    medico = Optional(Medico, reverse='pazienti_minori')
    infermiere = Optional(Infermiere, reverse='pazienti_minori')
    prenotazioni = Set('Prenotazione', reverse='paziente_minore')
    visite = Set('Visita', reverse='paziente_minore')
    visitainf = Set('Visitainf', reverse='paziente_minore')
    servizioSanitario = Set('ServizioSanitario', reverse='pazienti_minori')
    report_servizioSanitario = Set('ReportServizioSanitario', reverse='paziente_minore')
    report_visite = Set('ReportVisite', reverse='paziente_minore')

# Classe PazienteAdolescente
class PazienteAdolescente(db.Entity):
    _table_ = 'pazienti_adolescenti'
    id = PrimaryKey(str)
    CF = Required(str, unique=True)
    nome = Required(str)
    cognome = Required(str)
    data_nascita = Required(date)
    luogo_nascita = Required(str)
    mail_tutor = Required(str)
    tutor = Required(PazienteAdulto, reverse='responsabili_adolescenti')  
    credenziali_adolescente = Optional('CredenzialiAdolescente', reverse='paziente')
    medico = Optional(Medico, reverse='pazienti_adolescenti')
    infermiere = Optional(Infermiere, reverse='pazienti_adolescenti')
    prenotazioni = Set('Prenotazione', reverse='paziente_adolescente')
    visite = Set('Visita', reverse='paziente_adolescente')
    visitainf = Set('Visitainf', reverse='paziente_adolescente')
    servizioSanitario = Set('ServizioSanitario', reverse='pazienti_adolescenti')
    report_servizioSanitario = Set('ReportServizioSanitario', reverse='paziente_adolescente')
    report_visite = Set('ReportVisite', reverse='paziente_adolescente')

# Classe Assenze (per Medico)
class Assenze(db.Entity):
    _table_ = 'assenze'
    id = PrimaryKey(int, auto=True)
    data = Required(date)
    medico = Required(Medico, reverse='ferie')
    motivo = Optional(str)

# Classe Prenotazione
class Prenotazione(db.Entity):
    _table_ = 'prenotazioni'
    id = PrimaryKey(str)
    paziente_adulto = Optional(PazienteAdulto, reverse='prenotazioni')
    paziente_minore = Optional(PazienteMinore, reverse='prenotazioni')
    paziente_adolescente = Optional(PazienteAdolescente, reverse='prenotazioni')
    medico = Optional(Medico, reverse='prenotazioni_medico')
    infermiere = Optional(Infermiere, reverse='prenotazioni_infermiere')
    sala = Optional('Sala', reverse='prenotazioni')
    ambulatorio = Optional('Ambulatorio', reverse='prenotazioni')
    data = Required(date)
    visite = Set('Visita', reverse='prenotazione')
    visitainf = Set('Visitainf', reverse='prenotazione')
    report_visita = Set('ReportVisite', reverse='prenotazione')
    servizioSanitario = Optional('ServizioSanitario', reverse='prenotazioni')

# Classe Visita
class Visita(db.Entity):
    _table_ = 'visite'
    id = PrimaryKey(str)
    paziente_adulto = Optional(PazienteAdulto, reverse='visite')
    paziente_minore = Optional(PazienteMinore, reverse='visite')
    paziente_adolescente = Optional(PazienteAdolescente, reverse='visite')
    medico = Optional(Medico, reverse='visite')
    infermiere = Optional(Infermiere, reverse='visite')
    data = Required(date)
    prenotazione = Optional(Prenotazione, reverse='visite')
    report_visita = Set('ReportVisite', reverse='visita')
    esito_medico = Set('EsitoVisitaMedica', reverse='visita')
    esito_infermieristico = Set('EsitoVisitaInfermieristica', reverse='visita')

class Visitainf(db.Entity):
    _table_ = 'visitainf'
    id = PrimaryKey(str)
    paziente_adulto = Optional(PazienteAdulto, reverse='visitainf')
    paziente_minore = Optional(PazienteMinore, reverse='visitainf')
    paziente_adolescente = Optional(PazienteAdolescente, reverse='visitainf')
    infermiere = Optional(Infermiere, reverse='visitainf')
    data = Required(date)
    prenotazione = Optional(Prenotazione, reverse='visitainf')
    #report_visita = Set('ReportVisite', reverse='visitainf')
    tipologia = Required(str)
    descrizione = Optional(str)
    esito_infermieristico = Set('EsitoVisitaInfermieristica', reverse='visitainf')    

# Classe CredenzialiPersonale
class CredenzialiPersonale(db.Entity):
    _table_ = 'credenziali_personale'
    username = PrimaryKey(str)
    password = Required(str)
    medico = Optional(Medico, reverse='credenziali')
    infermiere = Optional(Infermiere, reverse='credenziali')
    segreteria = Optional(Segreteria, reverse='credenziali')

# Classe CredenzialiPazienteAdulto
class CredenzialiPazienteAdulto(db.Entity):
    _table_ = 'credenziali_pazienti_adulti'
    CF = PrimaryKey(str)
    password = Required(str)
    paziente = Required(PazienteAdulto, reverse='credenziali')

# Classe CredenzialiAdolescente
class CredenzialiAdolescente(db.Entity):
    _table_ = 'credenziali_adolescenti'
    CF = PrimaryKey(str)
    password = Required(str)
    paziente = Required(PazienteAdolescente, reverse='credenziali_adolescente')

# Classe TurniMedico
class TurniMedico(db.Entity):
    _table_ = 'turni_medici'
    id = PrimaryKey(str)
    medico = Required(Medico, reverse='turni')
    data_inizio = Required(date)
    data_fine = Required(date)
    orario_inizio = Required(str)
    orario_fine = Required(str)

# Classe TurniInfermiere
class TurniInfermiere(db.Entity):
    _table_ = 'turni_infermieri'
    id = PrimaryKey(str)
    infermiere = Required(Infermiere, reverse='turni')
    data_inizio = Required(date)
    data_fine = Required(date)
    orario_inizio = Required(str)
    orario_fine = Required(str)

# Classe EsitoVisitaMedica
class EsitoVisitaMedica(db.Entity):
    _table_ = 'esiti_visita_medica'
    id = PrimaryKey(str)
    visita = Required(Visita, reverse='esito_medico')
    medico = Required(Medico, reverse='esiti_medici')
    descrizione = Required(str)
    referto = Optional(str)
    data = Required(date)

# Classe EsitoVisitaInfermieristica
class EsitoVisitaInfermieristica(db.Entity):
    _table_ = 'esiti_visita_infermieristica'
    id = PrimaryKey(str)
    visita = Required(Visita, reverse='esito_infermieristico')
    visitainf = Optional(Visitainf, reverse='esiti_visita_infermieristica')
    infermiere = Required(Infermiere, reverse='esiti_infermieristici')
    descrizione = Optional(str)
    data = Required(date)

# Classe Sala
class Sala(db.Entity):
    _table_ = 'sale'
    id = PrimaryKey(str)
    numero = Required(str)
    tipoSala = Required(str)
    infermieri = Set(Infermiere, reverse='sala')
    prenotazioni = Set(Prenotazione, reverse='sala')

# Classe Ambulatorio
class Ambulatorio(db.Entity):
    _table_ = 'ambulatori'
    id = PrimaryKey(str)
    nome = Required(str)
    prenotazioni = Set(Prenotazione, reverse='ambulatorio')

# Classe ServizioSanitario
class ServizioSanitario(db.Entity):
    _table_ = 'servizi_sanitari'
    id = PrimaryKey(str)
    nome = Required(str)
    pazienti_adulti = Set(PazienteAdulto, reverse='servizioSanitario')
    pazienti_minori = Set(PazienteMinore, reverse='servizioSanitario')
    pazienti_adolescenti = Set(PazienteAdolescente, reverse='servizioSanitario')
    report_servizi_sanitari = Set('ReportServizioSanitario', reverse='servizioSanitario')
    report_visite = Set('ReportVisite', reverse='servizioSanitario')
    prenotazioni = Set(Prenotazione, reverse='servizioSanitario')

# Classe ReportServizioSanitario
class ReportServizioSanitario(db.Entity):
    _table_ = 'report_servizi_sanitari'
    id = PrimaryKey(str)
    servizioSanitario = Required(ServizioSanitario, reverse='report_servizi_sanitari')
    paziente_adulto = Optional(PazienteAdulto, reverse='report_servizioSanitario')
    paziente_minore = Optional(PazienteMinore, reverse='report_servizioSanitario')
    paziente_adolescente = Optional(PazienteAdolescente, reverse='report_servizioSanitario')
    data = Required(date)
    descrizione = Required(str)

# Classe ReportVisite
class ReportVisite(db.Entity):
    _table_ = 'report_visite'
    id = PrimaryKey(str)
    medico = Optional(Medico, reverse='report_visite')
    infermiere = Optional(Infermiere, reverse='report_visite')
    paziente_adulto = Optional(PazienteAdulto, reverse='report_visite')
    paziente_minore = Optional(PazienteMinore, reverse='report_visite')
    paziente_adolescente = Optional(PazienteAdolescente, reverse='report_visite')
    descrizione = Required(str)
    data = Required(date)
    visita = Required(Visita, reverse='report_visita')
    #visitainf = Set(Visitainf, reverse='report_visite')
    prenotazione = Required(Prenotazione, reverse='report_visita')
    servizioSanitario = Optional(ServizioSanitario, reverse='report_visite')


def init_db():
    db.bind(provider='sqlite', filename='database.db', create_db=True)
    db.generate_mapping(create_tables=True)




