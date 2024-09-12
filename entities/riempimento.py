from datetime import date, timedelta
from pony.orm import *
from models import db, init_db
from models import (
    Medico, Infermiere, Segreteria, PazienteAdulto, PazienteMinore, 
    PazienteAdolescente, Visita, Prenotazione, 
    EsitoVisitaMedica, EsitoVisitaInfermieristica, 
    TurniMedico, TurniInfermiere, CredenzialiPersonale, 
    CredenzialiPazienteAdulto, CredenzialiAdolescente, Sala, Ambulatorio,
    Assenze
)
@db_session
def popolamento_database():
    
        # Popolamento Ambulatorio
        ambulatori = [
            Ambulatorio(id='amb_01', nome='Ambulatorio Generale'),
            Ambulatorio(id='amb_02', nome='Ambulatorio Urgenze'),
            Ambulatorio(id='amb_03', nome='Ambulatorio Specialistico')
        ]

        # Popolamento Sala
        sale = [
            Sala(id='sala_01', numero='1', tipoSala='Medicazioni'),
            Sala(id='sala_02', numero='2', tipoSala='Prelievi')
        ]

        # Popolamento Medico
        medici = [
            Medico(id='med_01', CF='RSSMRA80A01H501A', nome='Mario', cognome='Rossi', 
                   data_nascita=date(1980, 1, 1), luogo_nascita='Roma', mail='mario.rossi@example.com'),
            Medico(id='med_02', CF='VRDLCA85A41H501B', nome='Luca', cognome='Verdi', 
                   data_nascita=date(1985, 1, 1), luogo_nascita='Milano', mail='luca.verdi@example.com')
        ]

        # Popolamento Infermiere
        infermieri = [
            Infermiere(id='inf_01', CF='BNCMRA90A01H501C', nome='Maria', cognome='Bianchi', 
                       data_nascita=date(1990, 1, 1), luogo_nascita='Napoli', mail='maria.bianchi@example.com'),
            Infermiere(id='inf_02', CF='NREGVN88A01H501D', nome='Giovanni', cognome='Neri', 
                       data_nascita=date(1988, 1, 1), luogo_nascita='Firenze', mail='giovanni.neri@example.com')
        ]

        # Popolamento Segreteria
        segreterie = [
            Segreteria(id='seg_01', CF='GLLRSA92A41H501E', nome='Rosa', cognome='Gialli', 
                       data_nascita=date(1992, 1, 1), luogo_nascita='Torino', mail='rosa.gialli@example.com')
        ]

        # Popolamento PazienteAdulto
        pazienti_adulti = [
            PazienteAdulto(id='pad_01', CF='BNCGPP75A01H501F', nome='Giuseppe', cognome='Bianchi', 
                           data_nascita=date(1975, 1, 1), luogo_nascita='Bologna', mail='giuseppe.bianchi@example.com'),
            PazienteAdulto(id='pad_02', CF='RSSLRA80A41H501G', nome='Laura', cognome='Rossi', 
                           data_nascita=date(1980, 1, 1), luogo_nascita='Palermo', mail='laura.rossi@example.com')
        ]

        # Popolamento PazienteMinore
        pazienti_minori = [
            PazienteMinore(id='pmi_01', CF='VRDMRC10A01H501H', nome='Marco', cognome='Verdi', 
                           data_nascita=date(2010, 1, 1), luogo_nascita='Genova', 
                           mail_responsabile='giuseppe.bianchi@example.com', responsabile_adulto=pazienti_adulti[0])
        ]

        # Popolamento PazienteAdolescente
        pazienti_adolescenti = [
            PazienteAdolescente(id='pad_01', CF='NRSFNC05A41H501I', nome='Francesca', cognome='Neri', 
                                data_nascita=date(2005, 1, 1), luogo_nascita='Venezia', 
                                mail_tutor='laura.rossi@example.com', tutor=pazienti_adulti[1])
        ]

        # Popolamento Prenotazione
        prenotazioni = [
            Prenotazione(id='pre_01', data=date(2024, 3, 15), paziente_adulto=pazienti_adulti[0], 
                         medico=medici[0], ambulatorio=ambulatori[0]),
            Prenotazione(id='pre_02', data=date(2024, 3, 16), paziente_minore=pazienti_minori[0], 
                         medico=medici[1], ambulatorio=ambulatori[1])
        ]

        # Popolamento Visita
        visite = [
            Visita(id='vis_01', data=date(2024, 3, 15), paziente_adulto=pazienti_adulti[0], 
                   medico=medici[0], prenotazione=prenotazioni[0]),
            Visita(id='vis_02', data=date(2024, 3, 16), paziente_minore=pazienti_minori[0], 
                   medico=medici[1], prenotazione=prenotazioni[1])
        ]

        # Popolamento EsitoVisitaMedica
        esiti_medici = [
            EsitoVisitaMedica(id='esm_01', visita=visite[0], medico=medici[0], 
                              descrizione='Visita di routine completata', data=date(2024, 3, 15)),
            EsitoVisitaMedica(id='esm_02', visita=visite[1], medico=medici[1], 
                              descrizione='Controllo pediatrico completato', data=date(2024, 3, 16))
        ]

        # Popolamento EsitoVisitaInfermieristica
        esiti_infermieristici = [
            EsitoVisitaInfermieristica(id='esi_01', visita=visite[0], infermiere=infermieri[0], 
                                       descrizione='Parametri vitali nella norma', data=date(2024, 3, 15)),
            EsitoVisitaInfermieristica(id='esi_02', visita=visite[1], infermiere=infermieri[1], 
                                       descrizione='Vaccinazione effettuata', data=date(2024, 3, 16))
        ]

        # Popolamento Assenze
        assenze = [
            Assenze(medico=medici[0], data=date(2024, 4, 1)),
            Assenze(medico=medici[1], data=date(2024, 4, 2))
        ]

        # Popolamento TurniMedico
        turni_medici = [
            TurniMedico(id='turno_01', medico=medici[0], data_inizio=date(2024, 3, 15), data_fine=date(2024, 3, 15), 
                    orario_inizio='09:00', orario_fine='17:00'),
            TurniMedico(id='turno_02', medico=medici[1], data_inizio=date(2024, 3, 16), data_fine=date(2024, 3, 16), 
                    orario_inizio='09:00', orario_fine='17:00')
    ]

        # Popolamento TurniInfermiere
        turni_infermieri = [
            TurniInfermiere(id='turno_inf_01', infermiere=infermieri[0], data_inizio=date(2024, 3, 15), data_fine=date(2024, 3, 15), 
                            orario_inizio='08:00', orario_fine='16:00'),
            TurniInfermiere(id='turno_inf_02', infermiere=infermieri[1], data_inizio=date(2024, 3, 16), data_fine=date(2024, 3, 16), 
                            orario_inizio='08:00', orario_fine='16:00')
        ]

        # Popolamento CredenzialiPersonale
        credenziali_personale = [
            CredenzialiPersonale(username='mario.rossi', password='password123', medico=medici[0]),
            CredenzialiPersonale(username='luca.verdi', password='password456', medico=medici[1]),
            CredenzialiPersonale(username='maria.bianchi', password='password789', infermiere=infermieri[0]),
            CredenzialiPersonale(username='giovanni.neri', password='passwordabc', infermiere=infermieri[1]),
            CredenzialiPersonale(username='rosa.gialli', password='passworddef', segreteria=segreterie[0])
        ]

        # Popolamento CredenzialiPazienteAdulto
        credenziali_paziente_adulto = [
            CredenzialiPazienteAdulto(CF='BNCGPP75A01H501F', password='paziente123', paziente=pazienti_adulti[0]),
            CredenzialiPazienteAdulto(CF='RSSLRA80A41H501G', password='paziente456', paziente=pazienti_adulti[1])
        ]

        # Popolamento CredenzialiAdolescente
        credenziali_adolescente = [
            CredenzialiAdolescente(CF='NRSFNC05A41H501I', password='adolescente123', paziente=pazienti_adolescenti[0])
        ]

        commit()   
if __name__ == "__main__":
    init_db()
    popolamento_database()
    print("Database popolato con successo!")