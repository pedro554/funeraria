

def criar(banco, cursor, planos):
    import PySimpleGUI as sg

    frame_texto = [
        [sg.Text('Nome do plano:', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Input(key='-NOME_PLANO-', size=(40, 1), font=('Concolas', 16), background_color='#FFF')],
        [sg.Text('Valor: R$     ', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Input(key='-VALOR_PLANO-', size=(15, 1), font=('Concolas', 16), background_color='#FFF')],
        [sg.Text('Descrição:    ', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Multiline(key='-DESCRICAO_PLANO-', size=(40, 10), font=('Concolas', 16), background_color='#FFF')],
    ]



    layout = [
        [sg.Frame('', frame_texto, relief='flat', background_color="#aaa")],
        [sg.Button('Criar Plano', key='-CRIAR_PLANO-')],
    ]

    janelaPlanos = sg.Window('Janela Planos', layout, finalize=True, background_color="#aaa")

    while True:
        event, values = janelaPlanos.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-CRIAR_PLANO-':
            nome_plano = values.get('-NOME_PLANO-')
            descricao = values.get('-DESCRICAO_PLANO-')
            valor = values.get('-VALOR_PLANO-')
            sql = f"INSERT INTO TPLANOS VALUES ('', '{nome_plano}', '{descricao}', '{valor}')"
            cursor.execute(sql)
            banco.commit()
            janelaPlanos.close()
            sg.popup('Plano criado')
            break
        
    planos = []
    sql = "SELECT * FROM TPLANOS"
    cursor.execute(sql)
    r = cursor.fetchall()
    for x in r:
        planos.append(x)

    return planos
