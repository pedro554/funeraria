


def janelaPlanos(banco, cursor):
    import PySimpleGUI as sg
    from modulos import colunasTabelaBanco
    from modulos import criarPlano, excluirPlano, alterarPlano


    colunas = colunasTabelaBanco.colunas(cursor, 'TPLANOS')
    planos = []
    sql = "SELECT * FROM TPLANOS"
    cursor.execute(sql)
    r = cursor.fetchall()
    for x in r:
        planos.append(x)
    frame_top = [
            [
                sg.Button('Criar Plano', key='-CRIAR_PLANO-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
                sg.Button('Excluir', key='-EXCLUIR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
                sg.Button('Alterar', key='-ALTERAR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
                sg.Button('Selecionar', key='-SELECIONAR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            ]
        ]
    frame_tabela = [
        [
            sg.Table(values=planos, headings = colunas, visible_column_map = None, col_widths = 20, def_col_width = 20, row_height = 20,
            auto_size_columns = False, max_col_width = 36,vertical_scroll_only = False, size=((20,25)),
            font = ('Concolas', 10), justification = "left", text_color = '#333', background_color = '#ddd',
            alternating_row_color = '#ccc', header_text_color = '#000', header_background_color = '#ddd',
            header_font = ('Concolas', 10), enable_events = True, key='-TABELA_PLANOS-'),
        ]
    ]
    frame_bottom = [
            [sg.Combo(colunas, key='-PESQUISAR_POR_COLUNA-', readonly=True, default_value=colunas[1])],
            [
                sg.Input(key='-PLANO-', size=(36,1)), sg.Button('Pesquisar', key='-PESQUISAR-'),
                sg.Checkbox('Todos', key='-PESQUISAR_TODOS-', background_color="#aaa"),
            ],
    ]

    layout = [
        [sg.Frame('', frame_top, relief='flat', background_color="#aaa")],
        [sg.Frame('', frame_tabela, relief='flat', background_color="#aaa")],
        [sg.Frame('', frame_bottom, relief='groove', background_color="#aaa")],
    ]

    janelaPlanos = sg.Window('Janela Planos', layout, finalize=True, background_color="#aaa")
    janelaPlanos.maximize()

    while True:
        event, values = janelaPlanos.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == '-CRIAR_PLANO-':
            planos = criarPlano.criar(banco, cursor, planos)
            janelaPlanos['-TABELA_PLANOS-'].Update(planos)
        
        elif event == '-EXCLUIR-':
            indice = values.get('-TABELA_PLANOS-')
            try:
                planos = excluirPlano.excluir(banco, cursor, planos, indice)
            except:
                sg.popup('Selecione um plano')
            janelaPlanos['-TABELA_PLANOS-'].Update(planos)

        elif event == '-ALTERAR-':
            indice = values.get('-TABELA_PLANOS-')
            try:
                indice = indice[0]
                planos = alterarPlano.alterar(banco, cursor, planos, indice)
                janelaPlanos['-TABELA_PLANOS-'].Update(planos)
            except:
                sg.popup('Selecione um plano')

        elif event == '-PESQUISAR-' and values.get('-PESQUISAR_TODOS-') == False:
            planos = []
            try:
                col = values.get('-PESQUISAR_POR_COLUNA-')
                plano = values.get('-PLANO-')
                sql = f"SELECT * FROM TPLANOS WHERE {col} LIKE '{plano}%'"
                cursor.execute(sql)
                r = cursor.fetchall()
                for x in r:
                    planos.append(x)
                janelaPlanos['-TABELA_PLANOS-'].Update(planos)
            except:
                sg.popup('Selecione uma coluna')
                
        elif event == '-PESQUISAR-' and values.get('-PESQUISAR_TODOS-') == True:
            planos = []
            sql = f"SELECT * FROM TPLANOS"
            cursor.execute(sql)
            r = cursor.fetchall()
            for x in r:
                planos.append(x)
            janelaPlanos['-TABELA_PLANOS-'].Update(planos)

        elif event == '-SELECIONAR-':
            try:
                plano = values.get('-TABELA_PLANOS-')
                janelaPlanos.close()
                return planos[plano[0]]
            except:
                sg.popup('Selecione um plano')

