def alterar(banco, cursor, planos, indice):
    import PySimpleGUI as sg
    frame_texto = [
        [sg.Text('Nome do plano:', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Input(key='-NOME_PLANO-', size=(40, 1), font=('Concolas', 16), background_color='#FFF', default_text=planos[indice][1])],
        [sg.Text('Valor: R$     ', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Input(key='-VALOR_PLANO-', size=(15, 1), font=('Concolas', 16), background_color='#FFF', default_text=planos[indice][3])],
        [sg.Text('Descrição:    ', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Multiline(key='-DESCRICAO_PLANO-', size=(40, 10), font=('Concolas', 16), background_color='#FFF', default_text=planos[indice][2])],
    ]



    layout = [
        [sg.Frame('', frame_texto, relief='flat', background_color="#aaa")],
        [sg.Button('Alterar Plano', key='-ALTERAR_PLANO-')],
    ]

    janelaAlterarPlanos = sg.Window('Janela Alterar Planos', layout, finalize=True, background_color="#aaa")

    while True:
        event, values = janelaAlterarPlanos.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-ALTERAR_PLANO-':
            plano = values.get('-NOME_PLANO-')
            valor = values.get('-VALOR_PLANO-')
            descricao = values.get('-DESCRICAO_PLANO-')

            sql = f"UPDATE TPLANOS SET PLANO='{plano}', DESCRICAO='{descricao}', VALOR='{valor}' WHERE ID='{planos[indice][0]}'"
            print(sql)
            cursor.execute(sql)
            banco.commit()
            janelaAlterarPlanos.close()
            sg.popup('Plano Alterado')
            break

    planos = []
    sql = "SELECT * FROM TPLANOS"
    cursor.execute(sql)
    r = cursor.fetchall()
    for x in r:
        planos.append(x)

    return planos

