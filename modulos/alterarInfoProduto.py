import PySimpleGUI as sg


def alterar(banco, cursor, estoque, indice):
    for i in indice:
        produto = estoque[i]
    id = produto[0]
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
        [sg.Input(key='PRODUTO', default_text=produto[1])],
        [sg.Input(key='CODBARRAS', default_text=produto[2])],
        [sg.Input(key='UNIDADE', default_text=produto[3])],
        [sg.Input(key='PRECOCUSTO', default_text=produto[4])],
        [sg.Input(key='PRECOVENDA', default_text=produto[5])],
        [sg.Input(key='QTDE', default_text=produto[6])],
        [sg.Input(key='NCM', default_text=produto[7])],
        [sg.Input(key='TRIBUTACAOIPI', default_text=produto[8])],
        [sg.Input(key='TRIBUTACAOPIS', default_text=produto[9])],
        [sg.Input(key='CSOSN', default_text=produto[10])],
        [sg.Input(key='TRIBUTACAOCOFINS', default_text=produto[11])],
        [sg.Input(key='VALORICMSST', default_text=produto[12])],
        [sg.Input(key='VALORIPI', default_text=produto[13])],
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
        [sg.Input(key='TIPOBARRA', default_text=produto[14])],
        [sg.Input(key='GRUPO', default_text=produto[15])],
        [sg.Input(key='FORNECEDOR', default_text=produto[16])],
        [sg.Input(key='TAMANHO', default_text=produto[17])],
        [sg.Input(key='PESO', default_text=produto[18])],
        [sg.Input(key='QTDEMINIMA', default_text=produto[19])],
        [sg.Input(key='QTDEMAXIMA', default_text=produto[20])],
        
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

    janelaAlterarInfoProduto = sg.Window('Alterar informações do produto', layout, finalize=True)

    while True:
        event, values = janelaAlterarInfoProduto.read()
        if event == sg.WIN_CLOSED:
            break

        if event == '-ATUALIZAR-':
            estoque.pop(indice[0])
            produto = values.get('PRODUTO')
            tipobarra = values.get('TIPOBARRA')
            codbarra = values.get('CODBARRA')
            unidade = values.get('UNIDADE')
            precocusto = values.get('PRECOCUSTO')
            precovenda = values.get('PRECOVENDA')
            grupo = values.get('GRUPO')
            fornecedor = values.get('FORNECEDOR')
            tamanho = values.get('TAMANHO')
            peso = values.get('PESO')
            qtdemaxima = values.get('QTDEMAXIMA')
            qtdeminima = values.get('QTDEMINIMA')
            qtde = values.get('QTDE')
            ncm = values.get('NCM')
            tributacaoipi = values.get('TRIBUTACAOIPI')
            tributacaopis = values.get('TRIBUTACAOPIS')
            tributacaocofins = values.get('TRIBUTACAOCOFINS')
            csosn = values.get('CSOSN')
            valoricmsst = values.get('VALORICMSST')
            valoripi = values.get('VALORIPI')
            sql = f"UPDATE TESTOQUE SET PRODUTO='{produto}', TIPOBARRA='{tipobarra}', CODBARRAS='{codbarra}', UNIDADE='{unidade}', PRECOCUSTO='{precocusto}', PRECOVENDA='{precovenda}', GRUPO='{grupo}', FORNECEDOR='{fornecedor}', TAMANHO='{tamanho}', PESO='{peso}', QTDEMAXIMA='{qtdemaxima}', QTDEMINIMA='{qtdeminima}', QTDE='{qtde}', NCM='{ncm}', TRIBUTACAOPIS='{tributacaopis}', TRIBUTACAOIPI='{tributacaoipi}', TRIBUTACAOCOFINS='{tributacaocofins}', CSOSN='{csosn}', VALORICMSST='{valoricmsst}', VALORIPI='{valoripi}' WHERE ID='{id}'"
            cursor.execute(sql)
            banco.commit()
            janelaAlterarInfoProduto.close()
            sg.popup('Produto atualizado')

            sql = f"SELECT * FROM TESTOQUE WHERE ID='{id}'"
            cursor.execute(sql)
            r = cursor.fetchone()
            estoque.append(r)

    return estoque
