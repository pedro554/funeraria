import PySimpleGUI as sg




def excluir(banco, cursor, clientes, indice):
	try:
		for i in indice:
			cliente =  clientes[i]

		sql = f"DELETE FROM TCLIENTE WHERE ID = '{cliente[0]}'"

		yn = sg.popup_yes_no('Deseja realmente deletar este cliente?')

		if yn == 'Yes':
			cursor.execute(sql)
			banco.commit()
			clientes.pop(i)
			sg.popup('Cliente deletado')
		else:
			pass
	except:
		sg.popup('Selecione um cliente')



	return clientes

