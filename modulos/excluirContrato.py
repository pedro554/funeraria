def excluir(banco, cursor, contratos, indice):
    import PySimpleGUI as sg

    try:
        for i in indice:
            contrato =  contratos[i]

        sql = f"DELETE FROM CONTRATOS WHERE ID = '{contrato[0]}'"

        yn = sg.popup_yes_no('Deseja realmente deletar este contrato?')

        if yn == 'Yes':
            cursor.execute(sql)
            banco.commit()
            contratos.pop(i)
            sg.popup('Contrato deletado')
        else:
            pass
    except:
        sg.popup('Selecione um cliente')



    return contratos