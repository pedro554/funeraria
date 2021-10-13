from datetime import date

d = date.today()

def diaSemana():
    if d.strftime('%A') == 'Sunday':
        dia_semana = 'domingo'
    elif d.strftime('%A') == 'Monday':
        dia_semana = 'segunda-feira'
    elif d.strftime('%A') == 'Tuesday':
        dia_semana = 'terça-feira'
    elif d.strftime('%A') == 'Wednesday':
        dia_semana = 'quarta-feira'
    elif d.strftime('%A') == 'Thursday':
        dia_semana = 'quinta-feira'
    elif d.strftime('%A') == 'Friday':
        dia_semana = 'sexta-feira'
    else:
        dia_semana = 'sábado'
    
    return dia_semana

def mes():
    if d.strftime('%B') == 'January':
        mes = 'janeiro'
    elif d.strftime('%B') == 'February':
        mes = 'fevereiro'
    elif d.strftime('%B') == 'March':
        mes = 'março'
    elif d.strftime('%B') == 'April':
        mes = 'abril'
    elif d.strftime('%B') == 'May':
        mes = 'maio'
    elif d.strftime('%B') == 'June':
        mes = 'junho'
    elif d.strftime('%B') == 'July':
        mes = 'julho'
    elif d.strftime('%B') == 'August':
        mes = 'agosto'
    elif d.strftime('%B') == 'September':
        mes = 'setembro'
    elif d.strftime('%B') == 'October':
        mes = 'outubro'
    elif d.strftime('%B') == 'November ':
        mes = 'novembro'
    else:
        mes = 'dezembro'
    
    return mes