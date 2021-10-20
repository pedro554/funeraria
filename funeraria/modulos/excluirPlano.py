

def excluir(banco, cursor, planos, indice):
    import PySimpleGUI as sg
    

    indice = indice[0]
    print(planos[indice][0])
    escolha = sg.popup_yes_no('Deseja realmente deletar este PLANO?')
    if escolha == 'Yes':
        sql = f"DELETE FROM TPLANOS WHERE ID='{planos[indice][0]}'"
        cursor.execute(sql)
        banco.commit()
    else:
        pass

    planos = []
    sql = "SELECT * FROM TPLANOS"
    cursor.execute(sql)
    r = cursor.fetchall()
    for x in r:
        planos.append(x)

    return planos
