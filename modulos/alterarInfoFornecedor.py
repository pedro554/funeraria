import PySimpleGUI as sg



def alterar(banco, cursor, fornecedores, indice):
	try:
		for i in indice:
			fornecedor = fornecedores[i]
		id = fornecedor[0]
		frameAdicionalTexto = [
            [sg.Text('Endereço:', font=('Consolas', 12))],
            [sg.Text('Bairro:', font=('Consolas', 12))],
            [sg.Text('Cidade:', font=('Consolas', 12))],
            [sg.Text('Pais:', font=('Consolas', 12))],
            [sg.Text('UF:', font=('Consolas', 12))],
            [sg.Text('CEP:', font=('Consolas', 12))],
            [sg.Text('Complemento:', font=('Consolas', 12))],
            [sg.Text('Telefone:', font=('Consolas', 12))],
            [sg.Text('SAC:', font=('Consolas', 12))],
            [sg.Text('Email:', font=('Consolas', 12))],
            [sg.Text('Site:', font=('Consolas', 12))],
		]
		frameAdicionalInput = [
				[sg.Input(key='ENDERECO', font=('Consolas', 12), default_text=fornecedor[6])],
				[sg.Input(key='BAIRRO', font=('Consolas', 12), default_text=fornecedor[7])],
				[sg.Input(key='CIDADE', font=('Consolas', 12), default_text=fornecedor[8])],
				[sg.Input(key='PAIS', font=('Consolas', 12), default_text=fornecedor[9])],
				[sg.Input(key='UF', font=('Consolas', 12), default_text=fornecedor[10])],
				[sg.Input(key='CEP', font=('Consolas', 12), default_text=fornecedor[11])],
				[sg.Input(key='COMPLEMENTO', font=('Consolas', 12), default_text=fornecedor[12])],
				[sg.Input(key='TELEFONE', font=('Consolas', 12), default_text=fornecedor[13])],
				[sg.Input(key='SAC', font=('Consolas', 12), default_text=fornecedor[14])],
				[sg.Input(key='EMAIL', font=('Consolas', 12), default_text=fornecedor[15])],
				[sg.Input(key='SITE', font=('Consolas', 12), default_text=fornecedor[16])],
		]

		framePrincipalTexto = [
			[sg.Text('Razão Social:', font=('Consolas', 12))],
			[sg.Text('Nome Fantasia:', font=('Consolas', 12))],
			[sg.Text('CNPJ:', font=('Consolas', 12))],
			[sg.Text('I. Estadual:', font=('Consolas', 12))],
			[sg.Text('I. Municipal:', font=('Consolas', 12))],
		]
		framePrincipalInput = [
				[sg.Input(key='RAZAOSOCIAL', font=('Consolas', 12), default_text=fornecedor[1])],
				[sg.Input(key='NOMEFANTASIA', font=('Consolas', 12), default_text=fornecedor[2])],
				[sg.Input(key='CNPJ', font=('Consolas', 12), default_text=fornecedor[3])],
				[sg.Input(key='IE', font=('Consolas', 12), default_text=fornecedor[4])],
				[sg.Input(key='IM', font=('Consolas', 12), default_text=fornecedor[5])],
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
			[sg.Button('Alterar', key='-ALTERAR-')],
		]

		janelaAlterarInfoFornecedor = sg.Window('Alterar informações do fornecedor', layout, finalize=True)

		while True:
			event, values = janelaAlterarInfoFornecedor.read()
			if event == sg.WIN_CLOSED:
				break

			if event == '-ALTERAR-':
				fornecedores.pop(indice[0])
				razaosocial = values.get('RAZAOSOCIAL')
				nomefantasia = values.get('NOMEFANTASIA')
				endereco = values.get('ENDERECO')
				bairro = values.get('BIRRO')
				cidade = values.get('CIDADE')
				pais = values.get('PAIS')
				uf = values.get('UF')
				cep = values.get('CEP')
				complemento = values.get('COMPLEMENTO')
				cnpj = values.get('CNPJ')
				ie = values.get('IE')
				im = values.get('IM')
				telefone = values.get('TELEFONE')
				sac = values.get('SAC')
				email = values.get('EMAIL')
				site = values.get('SITE')
				sql = f"UPDATE TFORNECEDOR SET RAZAOSOCIAL='{razaosocial}', NOMEFANTASIA='{nomefantasia}', ENDERECO='{endereco}', BAIRRO='{bairro}', CIDADE='{cidade}', PAIS='{pais}', UF='{uf}', CEP='{cep}', COMPLEMENTO='{complemento}', CNPJ='{cnpj}', IE='{ie}', IM='{im}', TELEFONE='{telefone}', SAC='{sac}', EMAIL='{email}', SITE='{site}' WHERE ID='{id}'"
				cursor.execute(sql)
				banco.commit()
				sg.popup('Fornecedor alterado')
				janelaAlterarInfoFornecedor.close()

				sql = f"SELECT * FROM TFORNECEDOR WHERE ID='{id}'"
				cursor.execute(sql)
				r = cursor.fetchall()
				for x in r:
					fornecedores.append(x)
	except:
		sg.popup('Selecione um fornecedor')

	return fornecedores

