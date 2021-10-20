

def adicionar(banco, cursor, cliente):
    
    import PySimpleGUI as sg
    from interface import janelaPlanos
    from modulos import addDependente, alterarInfoDependente
    count = 1
    count_list = ['1']

    sql = f"SELECT * FROM TDEPENDENTE WHERE IDCLIENTE='{cliente[0]}'"
    cursor.execute(sql)
    r = cursor.fetchall()


    frame_top = [
        [sg.Text('Cliente:', font=('Consolas', 12)), sg.Input(key='-CLIENTE-', readonly=True, default_text=cliente[1], font=('Consolas', 12)), sg.Button('Adicionar Dependente', key='-ADD_DEPENDENTE-', font=('Consolas', 12))],
        [sg.Text('Plano:  ', font=('Consolas', 12)), sg.Input(key='-PLANO-', readonly=True, font=('Consolas', 12)), sg.Button('Selecionar Plano', key='-SELECIONAR_PLANO-', font=('Consolas', 12))],
    ]

    frame_info = []

    layout = [
        [sg.Frame('', frame_top, relief='flat')],
        [sg.Button('Alterar Info. Dependente', key='-ALTERAR_INFO_DEPENDENTE-', font=('Consolas', 12))],
        [sg.Frame('', frame_info, relief='flat', key='-FRAME_INFO-')],
    ]

    janelaAdicionarPlano = sg.Window('Adicionar Plano', layout, finalize=True)
    janelaAdicionarPlano.maximize()

    for x in r:
        janelaAdicionarPlano.extend_layout(
                    janelaAdicionarPlano['-FRAME_INFO-'],
                    [[sg.Radio(f'{count} -', 'DEPENDENTES', font=('Consolas', 12), key=f'{count}', enable_events=True), sg.Input(readonly=True, default_text=x[3], font=('Consolas', 12), key=f'-INPUT_{count}-')]]
                )
        count+=1
        count_list.append(str(count))


    while True:
        event, values = janelaAdicionarPlano.read()
        if event == sg.WIN_CLOSED:
            break

        elif event == '-SELECIONAR_PLANO-':
            try:
                plano_selecionado = janelaPlanos.janelaPlanos(banco, cursor)
                janelaAdicionarPlano['-PLANO-'].Update(plano_selecionado[1])
            except:
                ...
        
        elif event == '-ADD_DEPENDENTE-':
            dependente = addDependente.add(banco, cursor, cliente[0], plano_selecionado[0])
            janelaAdicionarPlano.extend_layout(
                janelaAdicionarPlano['-FRAME_INFO-'],
                [[sg.Radio(f'{count} -', 'DEPENDENTES', font=('Consolas', 12), key=f'{count}', enable_events=True), sg.Input(readonly=True, default_text=dependente.get('-NOME-'), font=('Consolas', 12), key=f'-INPUT_{count}-')]]
            )
            count += 1
            count_list.append(str(count))
        
        elif event in count_list:
            indice = event
            nome_dependente = values.get(f'-INPUT_{indice}-')
            sql = f"SELECT * FROM TDEPENDENTE WHERE nomedependente='{nome_dependente}'"
            cursor.execute(sql)
            dependente_selecionado = cursor.fetchone()

        elif event == '-ALTERAR_INFO_DEPENDENTE-':
            try:
                nome_dependente = alterarInfoDependente.alterar(banco,cursor, dependente_selecionado)
                janelaAdicionarPlano[f'-INPUT_{indice}-'].Update(nome_dependente)
            except:
                sg.popup('Selecione um dependente')



