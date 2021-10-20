import PySimpleGUI as sg





def excluir(banco, cursor, estoque, indice):
	try:
		for i in indice:
			produto = estoque[i]

		sql = f"DELETE FROM TESTOQUE WHERE CONTROLE = '{produto[0]}'"

		yn = sg.popup_yes_no('Deseja realmente deletar este produto?')

		if yn == 'Yes':
			cursor.execute(sql)
			banco.commit()
			estoque.pop(i)
			sg.popup('Produto deletado')
		else:
			pass
	except:
		sg.popup('Selecione um produto')



	return estoque