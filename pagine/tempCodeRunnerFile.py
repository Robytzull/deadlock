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
            return layout_visite()  # Mostra la pagina delle visite del medico
        else:
            return login_layout  # Reindirizza alla pagina di login se non c'è un ID medico
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
    else:
        return home_layout  # Mostra la home come pagina predefinita