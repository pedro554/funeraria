import PySimpleGUI as sg



def excluir(banco, cursor, fornecedores, indice):
	try:
		for i in indice:
			fornecedor =  fornecedores[i]
		print(fornecedor)

		sql = f"DELETE FROM TFORNECEDOR WHERE ID = '{fornecedor[0]}'"

		yn = sg.popup_yes_no('Deseja realmente deletar este fornecedor?')

		if yn == 'Yes':
			cursor.execute(sql)
			banco.commit()
			fornecedores.pop(i)
			sg.popup('Fornecedor deletado')
		else:
			pass
	except:
		sg.popup('Selecione um fornecedor')



	return fornecedores
