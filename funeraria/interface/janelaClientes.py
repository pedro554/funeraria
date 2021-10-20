import PySimpleGUI as sg
from modulos import colunasTabelaBanco, incluirCliente, excluirCliente, alterarInfoCliente, adicionarPlano

def janela(banco, cursor):
    colunas = colunasTabelaBanco.colunas(cursor, 'TCLIENTE')
    clientes = []

    sql = "SELECT * FROM TCLIENTE"
    cursor.execute(sql)
    r = cursor.fetchall()
    for x in r:
        clientes.append(x)

    frame_top = [
        [
            sg.Button('Incluir', key='-INCLUIR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            sg.Button('Excluir', key='-EXCLUIR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            sg.Button('Alterar', key='-ALTERAR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            sg.Button('Selecionar', key='-SELECIONAR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            sg.Button('Adicionar Plano', key='-ADD_PLANO-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
        ]
    ]


    
    frame_tabela = [
        [
            sg.Table(values=clientes, headings = colunas, visible_column_map = None, col_widths = 20, def_col_width = 20, row_height = 20,
			auto_size_columns = False, max_col_width = 36,vertical_scroll_only = False, size=((20,25)),
            font = ('Concolas', 10), justification = "left", text_color = '#333', background_color = '#ddd',
        	alternating_row_color = '#ccc', header_text_color = '#000', header_background_color = '#ddd',
            header_font = ('Concolas', 10), enable_events = True, key='-TABELA_CLIENTES-'),
        ]
    ]

    frame_bottom = [
            [sg.Combo(colunas, key='-PESQUISAR_POR_COLUNA-', readonly=True)],
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

    janelaCliente = sg.Window('Clientes', layout, finalize=True, background_color="#aaa")
    janelaCliente.maximize()

    while True:
        event, values = janelaCliente.read()
        if event == sg.WIN_CLOSED:
            break

        elif event == '-ADD_PLANO-':
            indice = values.get('-TABELA_CLIENTES-')

            try:
                cliente = clientes[indice[0]]
            except:
                sg.popup('Selecione um cliente')
            adicionarPlano.adicionar(banco, cursor, cliente)

        elif event == '-SELECIONAR-':
            for x in values.get('-TABELA_CLIENTES-'):
                indice = x
            try:
                clienteSelecionado = clientes[indice]
                janelaCliente.close()
                return clienteSelecionado
            except:
                sg.popup("Selecione um cliente")
        
        elif event == '-INCLUIR-':
            clientes = incluirCliente.cadastro(banco, cursor)
            janelaCliente['-TABELA_CLIENTES-'].Update(clientes)

        elif event == '-EXCLUIR-':
            clientes = excluirCliente.excluir(banco, cursor, clientes, values.get('-TABELA_CLIENTES-'))
            janelaCliente['-TABELA_CLIENTES-'].Update(clientes)

        elif event == '-ALTERAR-':
            clientes = alterarInfoCliente.alterar(banco, cursor, clientes, values.get('-TABELA_CLIENTES-'))
            janelaCliente['-TABELA_CLIENTES-'].Update(clientes)

        elif event == '-PESQUISAR-' and values.get('-PESQUISAR_TODOS-') == False:
            try:
                clientes = []
                col = values.get('-PESQUISAR_POR_COLUNA-')
                cliente = values.get('-CLIENTE-')
                sql = f"SELECT * FROM TCLIENTE WHERE {col}='{cliente}'"
                cursor.execute(sql)
                r = cursor.fetchall()
                for x in r:
                    clientes.append(x)
                janelaCliente['-TABELA_CLIENTES-'].Update(clientes)
            except:
                sg.popup('Selecione uma coluna')

        elif event == '-PESQUISAR-' and values.get('-PESQUISAR_TODOS-') == True:
            clientes = []
            sql = f"SELECT * FROM TCLIENTE"
            cursor.execute(sql)
            r = cursor.fetchall()
            for x in r:
                clientes.append(x)
            janelaCliente['-TABELA_CLIENTES-'].Update(clientes)