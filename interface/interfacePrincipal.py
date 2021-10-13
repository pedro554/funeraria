import PySimpleGUI as sg
from interface import janelaClientes, janelaFornecedores, janelaEstoque, janelaContratos
from modulos import finalizarVenda, parcelarVenda, alteracoesVenda, alterarValorProduto

def Inicio(banco, cursor, path):
    produtos = []
    colunas = ['Qtde', 'Produto', 'Valor']
    menu_lateral = [
        [sg.Button('Clientes', key='-CLIENTES-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333"))],
        [sg.Button('Fornecedores', key='-FORNECEDORES-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333"))],
        [sg.Button('Estoque', key='-ESTOQUE-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333"))],
        [sg.Button('Contratos', key='-CONTRATOS-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333"))],
    ]

    frame_pdv = [
        [
            sg.Text('Item:', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Input(key='-CODIGO-', size=(15, 1), font=('Concolas', 16), background_color='#FFF', focus=True),
            sg.Button(key='-ATUALIZAR-', bind_return_key=True, visible=False),
            sg.Text('Quantidade:', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Input(key='-QUANTIDADE-', size=(5, 1), font=('Concolas', 16), background_color='#FFF', default_text='1'),
        ],

        [sg.Table(values=produtos, headings = colunas, visible_column_map = None, col_widths = 20, def_col_width = 20, auto_size_columns = False, max_col_width = 100, row_height = 30,
            font = ('Concolas', 16), justification = "left", text_color = '#333', background_color = '#ddd', alternating_row_color = '#ccc', header_text_color = '#000', header_background_color = '#ddd',
            header_font = ('Concolas', 16), size = (None, None), enable_events = True, key='-TABELA_PRODUTOS-')],
        [
            sg.Text('Quantidade de itens:', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Input(key='-QUANTIDADE_ITENS-', size=(5,1), font=('Concolas', 16), background_color='#FFF', readonly=True, border_width=0, default_text='0',
            disabled_readonly_background_color='#aaa'),
            sg.Text('Valor total: R$', font=('Consolas', 16), text_color='#333', background_color='#aaa'),
            sg.Input(key='-TOTAL_VENDA-', font=('Concolas', 16), background_color='#FFF', readonly=True, border_width=0, default_text='0',
            disabled_readonly_background_color='#aaa'),
        ],
        [sg.Text('F2 - VENDA', font=('Consolas', 16), text_color='#333', background_color='#aaa'), 
        sg.Text('F3 - EXCLUIR', font=('Consolas', 16), text_color='#333', background_color='#aaa'), 
        sg.Text('F4 - ALTERAR QUANTIDADE', font=('Consolas', 16), text_color='#333', background_color='#aaa'), 
        sg.Text('F5 - ALTERAR VALOR/DESCONTO', font=('Consolas', 16), text_color='#333', background_color='#aaa')]
    ]

    layout = [
        [sg.Column(menu_lateral, background_color="#aaa", size=(200,800)),
        sg.Column(frame_pdv, size=(1080,800), background_color="#aaa")],
    ]
    

    janelaPrincipal = sg.Window('Sistema', layout, finalize=True, background_color="#aaa")
    janelaPrincipal.maximize()
    total_itens = 0
    total_venda = 0
    
    while True:
        event, values = janelaPrincipal.read()
        #janelaPrincipal.bind('<Key-F1>', 'F1')
        janelaPrincipal.bind('<Key-F2>', 'F2')
        janelaPrincipal.bind('<Key-F4>', 'F4')
        janelaPrincipal.bind('<Key-F3>', 'F3')
        janelaPrincipal.bind('<Key-F5>', 'F5')

        if event == sg.WIN_CLOSED:
            break

        if event == '-CLIENTES-':
            janelaClientes.janela(banco, cursor)
        
        if event == '-FORNECEDORES-':
            janelaFornecedores.janela(banco, cursor)

        if event == '-ESTOQUE-':
            janelaEstoque.janela(banco, cursor)
        
        if event == 'F1':
            '''Venda Rápida'''
            finalizarVenda.finalizarVenda(banco, cursor, total_venda, produtos)

        if event == 'F2':
            '''Venda parcelada'''
            parcelarVenda.parcelar(banco, cursor, total_venda, produtos, path)
            produtos = []
            total_itens = 0
            total_venda = 0
            janelaPrincipal['-TABELA_PRODUTOS-'].Update(produtos)
            janelaPrincipal['-QUANTIDADE_ITENS-'].Update(total_itens)
            janelaPrincipal['-TOTAL_VENDA-'].Update(total_venda)
        
        if event == 'F4':
            '''Altera a quantidade de um produto'''
            indice = values.get('-TABELA_PRODUTOS-')
            for i in indice:
                indice = i
            total_itens -= float(produtos[indice][0])
            total_venda -= float(produtos[indice][2])
            produto = alteracoesVenda.alterarQuantidade(indice, produtos)
            total_itens += float(produto[0])
            total_venda += float(produto[2])
            
            produtos.append(produto)
            janelaPrincipal['-TABELA_PRODUTOS-'].Update(produtos)
            janelaPrincipal['-QUANTIDADE_ITENS-'].Update(total_itens)
            janelaPrincipal['-TOTAL_VENDA-'].Update(total_venda)

        if event == 'F3':
            '''Exclui um produto'''
            indice = values.get('-TABELA_PRODUTOS-')
            for i in indice:
                total_venda -= float(produtos[i][2])
                total_itens -= float(produtos[i][0])
                produtos.pop(i)
            janelaPrincipal['-TABELA_PRODUTOS-'].Update(produtos)
            janelaPrincipal['-QUANTIDADE_ITENS-'].Update(total_itens)
            janelaPrincipal['-TOTAL_VENDA-'].Update(total_venda)

        if event == 'F5':
            '''Altera valor do produto'''
            indice = values.get('-TABELA_PRODUTOS-')
            for i in indice:
                indice = i
            total_venda -= float(produtos[indice][2])
            produto = alterarValorProduto.alterarValor(indice, produtos)
            total_venda += float(produto[0]) * float(produto[2])
            produtos.append(produto)
            janelaPrincipal['-TOTAL_VENDA-'].Update(total_venda)
            janelaPrincipal['-TABELA_PRODUTOS-'].Update(produtos)


        if event == '-CONTRATOS-':
            janelaContratos.contratos(banco, cursor, path)







        if event == '-ATUALIZAR-':
            codigo = values.get('-CODIGO-')
            sql = f"SELECT PRODUTO, PRECOVENDA, ID FROM TESTOQUE WHERE ID='{codigo}' OR CODBARRAS='{codigo}' OR PRODUTO='{codigo}'"
            cursor.execute(sql)
            r = cursor.fetchone()
            quantidade_venda = float(values.get('-QUANTIDADE-'))
            try:
                valor = quantidade_venda * float(r[1])
                total_itens += quantidade_venda
                total_venda += valor
                produtos.append((quantidade_venda, r[0], f"{valor:.2f}"))
                janelaPrincipal['-TABELA_PRODUTOS-'].Update(produtos)
                janelaPrincipal['-QUANTIDADE_ITENS-'].Update(total_itens)
                janelaPrincipal['-TOTAL_VENDA-'].Update(f"{total_venda:.2f}")
            except:
                sg.popup('Produto inexistente')
