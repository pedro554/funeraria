import PySimpleGUI as sg


def cadastro(banco, cursor):
    framePrincipalInput = [
        [sg.Input(key='NOME', font=('Consolas', 12))],
        [sg.Input(key='NATURALIDADE', font=('Consolas', 12))],
        [sg.Input(key='RG', font=('Consolas', 12))],
        [sg.Input(key='CPF', font=('Consolas', 12))],
        [sg.Input(key='TELEFONE', font=('Consolas', 12))],
        [sg.Input(key='EMAIL', font=('Consolas', 12))],
    ]
    framePrincipalTexto = [
        [sg.Text('Cliente:', font=('Consolas', 12))],
        [sg.Text('Naturalidade:', font=('Consolas', 12))],
        [sg.Text('RG:', font=('Consolas', 12))],
        [sg.Text('CPF:', font=('Consolas', 12))],
        [sg.Text('Telefone:', font=('Consolas', 12))],
        [sg.Text('Email:', font=('Consolas', 12))],
    ]

    frame1 = [
        [sg.Frame('', framePrincipalTexto, relief='flat'), sg.Frame('', framePrincipalInput, relief='flat')],
    ]

    frameAdicionalInput = [
        [sg.Input(key='ENDERECO', font=('Consolas', 12))],
        [sg.Input(key='COMPLEMENTO', font=('Consolas', 12))],
        [sg.Input(key='BAIRRO', font=('Consolas', 12))],
        [sg.Input(key='CIDADE', font=('Consolas', 12))],
        [sg.Input(key='UF', font=('Consolas', 12))],
        [sg.Input(key='CEP', font=('Consolas', 12))],
        [sg.Input(key='PAIS', font=('Consolas', 12))],
    ]
    frameAdicionalTexto = [
        [sg.Text('Endereço:', font=('Consolas', 12))],
        [sg.Text('Complemento:', font=('Consolas', 12))],
        [sg.Text('Bairro:', font=('Consolas', 12))],
        [sg.Text('Cidade:', font=('Consolas', 12))],
        [sg.Text('UF:', font=('Consolas', 12))],
        [sg.Text('CEP:', font=('Consolas', 12))],
        [sg.Text('Pais:', font=('Consolas', 12))],
    ]

    frame2 = [
        [sg.Frame('', frameAdicionalTexto, relief='flat'), sg.Frame('', frameAdicionalInput, relief='flat')]
    ]

    layout = [
        [sg.TabGroup([[
            sg.Tab('Informações Principais', frame1, element_justification='center'),
            sg.Tab('Informações adicionais', frame2, element_justification='center'),
        ]])],
        [sg.Button('Cadastrar', key='-CADASTRAR-'), sg.Button('Adicionar Dependente', key='-ADD_DEPENDENTE-')],
    ]

    janelaIncluirCliente = sg.Window("Cadastro Cliente", layout, finalize=True)
    count = 1
    while True:
        event, values = janelaIncluirCliente.read()
        if event == sg.WIN_CLOSED:
            break

        if event == '-CADASTRAR-':
            values.pop(0)
            colunas = f""
            valores = f""
            for i in values.keys():
                colunas += str(i) + ','
            colunas = colunas.rstrip(',')

            for i in values.values():
                valores += f"'{str(i)}',"
            valores = valores.rstrip(',')
            sql = f"INSERT INTO TCLIENTE ({colunas}) VALUES ({valores})"
            print(sql)
            yn = sg.popup_yes_no('Salvar as informações?')
            if yn == 'Yes':
                cursor.execute(sql)
                banco.commit()
                sg.popup('Cliente cadastrado')

        clientes = []

        sql = "SELECT * FROM TCLIENTE"
        cursor.execute(sql)
        r = cursor.fetchall()
        for x in r:
            clientes.append(x)


        return clientes
