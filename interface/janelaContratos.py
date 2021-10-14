def contratos(banco, cursor, path):
    import PySimpleGUI as sg
    from modulos import colunasTabelaBanco
    from PIL import Image
    from modulos import excluirContrato, alterarContrato

    colunas = colunasTabelaBanco.colunas(cursor, 'CONTRATOS')
    contratos = []

    sql = "SELECT * FROM CONTRATOS"
    cursor.execute(sql)
    r = cursor.fetchall()
    for x in r:
        contratos.append(x)

    frame_top = [
        [
            sg.Button('Excluir', key='-EXCLUIR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            sg.Button('Alterar', key='-ALTERAR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            sg.Button('Ver Contrato', key='-VER_CONTRATO-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333"))
        ]
    ]
    frame_tabela = [
        [
            sg.Table(values=contratos, headings = colunas, visible_column_map = None, col_widths = 20, def_col_width = 20, row_height = 20,
			auto_size_columns = False, max_col_width = 36,vertical_scroll_only = False, size=((20,25)),
            font = ('Concolas', 10), justification = "left", text_color = '#333', background_color = '#ddd',
        	alternating_row_color = '#ccc', header_text_color = '#000', header_background_color = '#ddd',
            header_font = ('Concolas', 10), enable_events = True, key='-TABELA_CONTRATOS-'),
        ]
    ]
    frame_bottom = [
            [sg.Combo(colunas, key='-PESQUISAR_POR_COLUNA-', readonly=True, default_value=colunas[1])],
            [
                sg.Input(key='-CLIENTE-', size=(36,1)), sg.Button('Pesquisar', key='-PESQUISAR-'),
                sg.Checkbox('Todos', key='-PESQUISAR_TODOS-', background_color="#aaa"),
            ],
    ]

    layout = [
        [sg.Frame('', frame_top, relief='flat', background_color="#aaa")],
        [sg.Frame('', frame_tabela, relief='flat', background_color="#aaa")],
        [sg.Frame('', frame_bottom, relief='groove', background_color="#aaa")],
    ]

    janelaContratos = sg.Window('Janela Contratos', layout, finalize=True, background_color="#aaa")
    janelaContratos.maximize()

    while True:
        event, values = janelaContratos.read()
        if event == sg.WIN_CLOSED:
            break

        if event == '-PESQUISAR-' and values.get('-PESQUISAR_TODOS-') == False:
            try:
                contratos = []
                col = values.get('-PESQUISAR_POR_COLUNA-')
                cliente = values.get('-CLIENTE-')
                sql = f"SELECT * FROM CONTRATOS WHERE {col}='{cliente}'"
                cursor.execute(sql)
                r = cursor.fetchall()
                for x in r:
                    contratos.append(x)
                janelaContratos['-TABELA_CONTRATOS-'].Update(contratos)
            except:
                sg.popup('Selecione uma coluna')
        if event == '-PESQUISAR-' and values.get('-PESQUISAR_TODOS-') == True:
            contratos = []
            sql = f"SELECT * FROM CONTRATOS"
            cursor.execute(sql)
            r = cursor.fetchall()
            for x in r:
                contratos.append(x)
            janelaContratos['-TABELA_CONTRATOS-'].Update(contratos)

        if event == '-VER_CONTRATO-':
            for x in values.get('-TABELA_CONTRATOS-'):
                indice = x
            b64img = contratos[indice][3]
            import base64
            img_data = bytes(b64img, 'UTF-8')
            with open("temp.png", "wb") as fh:
                fh.write(base64.decodebytes(img_data))

            contrato_temp = Image.open(f"{path}\\temp.png")
            contrato_temp.show()

        if event == '-EXCLUIR-':
            contratos =  excluirContrato.excluir(banco, cursor, contratos, values.get('-TABELA_CONTRATOS-'))
            janelaContratos['-TABELA_CONTRATOS-'].Update(contratos)

        if event == '-ALTERAR-':
            indice = values.get('-TABELA_CONTRATOS-')
            alterarContrato.alterar(banco, cursor, contratos, indice)
            
