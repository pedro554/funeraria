import PySimpleGUI as sg
from modulos import colunasTabelaBanco, incluirFornecedor, excluirFornecedor, alterarInfoFornecedor

def janela(banco, cursor):
    colunas = colunasTabelaBanco.colunas(cursor, 'TFORNECEDOR')
    fornecedores = []

    sql = "SELECT * FROM TFORNECEDOR"
    cursor.execute(sql)
    r = cursor.fetchall()
    for x in r:
        fornecedores.append(x)

    frame_top = [
        [
            sg.Button('Incluir', key='-INCLUIR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            sg.Button('Excluir', key='-EXCLUIR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
            sg.Button('Alterar', key='-ALTERAR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
        ]
    ]


    
    frame_tabela = [
        [
            sg.Table(values=fornecedores, headings = colunas, visible_column_map = None, col_widths = 20, def_col_width = 20, row_height = 20,
			auto_size_columns = False, max_col_width = 36,vertical_scroll_only = False, size=((20,25)),
            font = ('Concolas', 10), justification = "left", text_color = '#333', background_color = '#ddd',
        	alternating_row_color = '#ccc', header_text_color = '#000', header_background_color = '#ddd',
            header_font = ('Concolas', 10), enable_events = True, key='-TABELA_FORNECEDORES-'),
        ]
    ]

    frame_bottom = [
            [sg.Combo(colunas, key='-PESQUISAR_POR_COLUNA-', readonly=True)],
            [
                sg.Input(key='-FORNECEDOR-', size=(36,1)), sg.Button('Pesquisar', key='-PESQUISAR-'),
                sg.Checkbox('Todos', key='-PESQUISAR_TODOS-', background_color="#aaa"),
            ],
    ]


    layout = [
        [sg.Frame('', frame_top, relief='flat', background_color="#aaa")],
        [sg.Frame('', frame_tabela, relief='flat', background_color="#aaa")],
        [sg.Frame('', frame_bottom, relief='groove', background_color="#aaa")],
    ]

    janelaFornecedores = sg.Window('Fornecedores', layout, finalize=True, background_color="#aaa")
    janelaFornecedores.maximize()

    while True:
        event, values = janelaFornecedores.read()
        print(event)
        if event == sg.WIN_CLOSED:
            break

        if event == '-INCLUIR-':
            fornecedores = incluirFornecedor.cadastro(banco, cursor)
            janelaFornecedores['-TABELA_FORNECEDORES-'].Update(fornecedores)

        if event == '-ALTERAR-':
            fornecedores = alterarInfoFornecedor.alterar(banco, cursor, fornecedores, values.get('-TABELA_FORNECEDORES-'))
            janelaFornecedores['-TABELA_FORNECEDORES-'].Update(fornecedores)

        if event == '-EXCLUIR-':
            fornecedores = excluirFornecedor.excluir(banco, cursor, fornecedores, values.get('-TABELA_FORNECEDORES-'))
            janelaFornecedores['-TABELA_FORNECEDORES-'].Update(fornecedores)

        if event == '-PESQUISAR-' and values.get('-PESQUISAR_TODOS-') == False:
            try:
                fornecedores = []
                col = values.get('-PESQUISAR_POR_COLUNA-')
                fornecedor = values.get('-FORNECEDOR-')
                sql = f"SELECT * FROM TFORNECEDOR WHERE {col}='{fornecedor}'"
                cursor.execute(sql)
                r = cursor.fetchall()
                for x in r:
                    fornecedores.append(x)
                janelaFornecedores['-TABELA_FORNECEDORES-'].Update(fornecedores)
            except:
                sg.popup('Selecione uma coluna')

        if event == '-PESQUISAR-' and values.get('-PESQUISAR_TODOS-') == True:
            fornecedores = []
            sql = f"SELECT * FROM TFORNECEDOR"
            cursor.execute(sql)
            r = cursor.fetchall()
            for x in r:
                fornecedores.append(x)
            janelaFornecedores['-TABELA_FORNECEDORES-'].Update(fornecedores)