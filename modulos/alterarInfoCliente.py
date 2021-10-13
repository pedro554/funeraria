import PySimpleGUI as sg



def alterar(banco, cursor, clientes, indice):
	#try:
		for i in indice:
			cliente = clientes[i]
		id = cliente[0]
		framePrincipalInput = [
        [sg.Input(key='NOME', font=('Consolas', 12), default_text=cliente[1])],
        [sg.Input(key='RG', font=('Consolas', 12), default_text=cliente[2])],
        [sg.Input(key='CPF', font=('Consolas', 12), default_text=cliente[3])],
        [sg.Input(key='TELEFONE', font=('Consolas', 12), default_text=cliente[4])],
        [sg.Input(key='EMAIL', font=('Consolas', 12), default_text=cliente[5])],
		]
		framePrincipalTexto = [
			[sg.Text('Cliente:', font=('Consolas', 12))],
			[sg.Text('RG:', font=('Consolas', 12))],
			[sg.Text('CPF:', font=('Consolas', 12))],
			[sg.Text('Telefone:', font=('Consolas', 12))],
			[sg.Text('Email:', font=('Consolas', 12))],
		]

		frame1 = [
			[sg.Frame('', framePrincipalTexto, relief='flat'), sg.Frame('', framePrincipalInput, relief='flat')],
		]

		frameAdicionalInput = [
			[sg.Input(key='ENDERECO', font=('Consolas', 12), default_text=cliente[8])],
			[sg.Input(key='COMPLEMENTO', font=('Consolas', 12), default_text=cliente[9])],
			[sg.Input(key='BAIRRO', font=('Consolas', 12), default_text=cliente[10])],
			[sg.Input(key='CIDADE', font=('Consolas', 12), default_text=cliente[11])],
			[sg.Input(key='UF', font=('Consolas', 12), default_text=cliente[12])],
			[sg.Input(key='CEP', font=('Consolas', 12), default_text=cliente[13])],
			[sg.Input(key='PAIS', font=('Consolas', 12), default_text=cliente[14])],
        	[sg.Input(key='NATURALIDADE', font=('Consolas', 12), default_text=cliente[7])],
		]
		frameAdicionalTexto = [
			[sg.Text('Endereço:', font=('Consolas', 12))],
			[sg.Text('Complemento:', font=('Consolas', 12))],
			[sg.Text('Bairro:', font=('Consolas', 12))],
			[sg.Text('Cidade:', font=('Consolas', 12))],
			[sg.Text('UF:', font=('Consolas', 12))],
			[sg.Text('CEP:', font=('Consolas', 12))],
			[sg.Text('Pais:', font=('Consolas', 12))],
			[sg.Text('Naturalidade:', font=('Consolas', 12))],
		]

		frame2 = [
			[sg.Frame('', frameAdicionalTexto, relief='flat'), sg.Frame('', frameAdicionalInput, relief='flat')]
		]

		layout = [
			[sg.TabGroup([[
				sg.Tab('Informações Principais', frame1, element_justification='center'),
				sg.Tab('Informações adicionais', frame2, element_justification='center'),
			]])],
			[sg.Button('Atualizar', key='-ATUALIZAR_CLIENTE-')],
		]
		
		janelaAlterar = sg.Window('Alterar informações do cliente', layout, finalize=True)

		while True:
			event, values = janelaAlterar.read()
			if event == sg.WIN_CLOSED:
				break

			if event == '-ATUALIZAR_CLIENTE-':
				clientes.pop(indice[0])
				cliente = values.get('NOME')
				endereco = values.get('ENDERECO')
				complemento = values.get('COMPLEMENTO')
				bairro = values.get('BAIRRO')
				cidade = values.get('CIDADE')
				uf = values.get('UF')
				pais = values.get('PAIS')
				cep = values.get('CEP')
				naturalidade = values.get('NATURALIDADE')
				rg = values.get('RG')
				cpf = values.get('CPF')
				telefone = values.get('TELEFONE')
				email = values.get('EMAIL')
				sql = f"UPDATE TCLIENTE SET NOME='{cliente}', ENDERECO='{endereco}', COMPLEMENTO='{complemento}', BAIRRO='{bairro}', CIDADE='{cidade}', UF='{uf}', PAIS='{pais}', CEP='{cep}', NATURALIDADE='{naturalidade}', RG='{rg}', CPF='{cpf}', TELEFONE='{telefone}', EMAIL='{email}' WHERE ID='{id}'"
				cursor.execute(sql)
				banco.commit()
				janelaAlterar.close()
				sg.popup('Cliente Cadastrado')
				janelaAlterar.close()

				sql = f"SELECT * FROM TCLIENTE WHERE ID='{id}'"
				cursor.execute(sql)
				r = cursor.fetchall()
				for x in r:
					clientes.append(x)

	#except:
		#sg.popup('Selecione um cliente')


		return clientes