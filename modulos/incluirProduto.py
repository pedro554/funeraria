import PySimpleGUI as sg


def cadastro(banco, cursor):
    framePrincipalTexto = [
        [sg.Text('Produto:')],
        [sg.Text('Cód. Barras:')],
        [sg.Text('Unidade:')],
        [sg.Text('Preço Custo:')],
        [sg.Text('Preço Venda:')],
        [sg.Text('Quantidade:')],
        [sg.Text('NCM:')],
        [sg.Text('Tributação IPI:')],
        [sg.Text('Tributação PIS:')],
        [sg.Text('CSOSN:')],
        [sg.Text('Tributação COFINS:')],
        [sg.Text('Valor ICMSST:')],
        [sg.Text('Valor IPI:')],
    ]
    framePrincipalInput = [
        [sg.Input(key='PRODUTO')],
        [sg.Input(key='CODBARRAS')],
        [sg.Input(key='UNIDADE')],
        [sg.Input(key='PRECOCUSTO')],
        [sg.Input(key='PRECOVENDA')],
        [sg.Input(key='QTDE')],
        [sg.Input(key='NCM')],
        [sg.Input(key='TRIBUTACAOIPI')],
        [sg.Input(key='TRIBUTACAOPIS')],
        [sg.Input(key='CSOSN')],
        [sg.Input(key='TRIBUTACAOCOFINS')],
        [sg.Input(key='VALORICMSST')],
        [sg.Input(key='VALORIPI')],
    ]


    frameAdicionalTexto = [
        [sg.Text('Tipo Barra:')],
        [sg.Text('Grupo:')],
        [sg.Text('Fornecedor:')],
        [sg.Text('Tamanho:')],
        [sg.Text('Peso:')],
        [sg.Text('Qtde. Minima:')],
        [sg.Text('Qtde. Maxima:')],
    ]

    frameAdicionalInput = [
        [sg.Input(key='TIPOBARRA')],
        [sg.Input(key='GRUPO')],
        [sg.Input(key='FORNECEDOR')],
        [sg.Input(key='TAMANHO')],
        [sg.Input(key='PESO')],
        [sg.Input(key='QTDEMINIMA')],
        [sg.Input(key='QTDEMAXIMA')],
        
    ]
    frame1 = [
			[sg.Frame('', framePrincipalTexto, relief='flat'), sg.Frame('', framePrincipalInput, relief='flat')]
		]
    frame2 = [
        [sg.Frame('', frameAdicionalTexto, relief='flat'), sg.Frame('', frameAdicionalInput, relief='flat')]
    ]

    layout = [
        [sg.TabGroup([[
				sg.Tab('Informações Principais', frame1, element_justification='center'),
				sg.Tab('Informações Adicionais', frame2, element_justification='center'),
			]])],
			[sg.Button('Cadastrar', key='-CADASTRAR-')],
    ]

    janelaCadastroProduto = sg.Window('Cadastro Produto', layout, finalize=True)

    while True:
        event, values = janelaCadastroProduto.read()
        if event == sg.WIN_CLOSED:
            break

        if event == '-CADASTRAR-':
            values.pop(0)
            colunas = ''
            valores = ''
            for i in values.keys():
                colunas += str(i) + ','
            colunas = colunas.rstrip(',')

            for i in values.values():
                valores += f"'{str(i)}',"
            valores = valores.rstrip(',')
            sql = f"INSERT INTO TESTOQUE ({colunas}) VALUES ({valores})"
            yn = sg.popup_yes_no('Salvar as informações?')
            if yn == 'Yes':
                cursor.execute(sql)
                banco.commit()
                sg.popup('Produto cadastrado')

        estoque = []

        sql = "SELECT * FROM TESTOQUE"
        cursor.execute(sql)
        r = cursor.fetchall()
        for x in r:
            estoque.append(x)


        return estoque