import PySimpleGUI as sg



def cadastro(banco, cursor):
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
            [sg.Input(key='ENDERECO', font=('Consolas', 12))],
            [sg.Input(key='BAIRRO', font=('Consolas', 12))],
            [sg.Input(key='CIDADE', font=('Consolas', 12))],
            [sg.Input(key='PAIS', font=('Consolas', 12))],
            [sg.Input(key='UF', font=('Consolas', 12))],
            [sg.Input(key='CEP', font=('Consolas', 12))],
            [sg.Input(key='COMPLEMENTO', font=('Consolas', 12))],
            [sg.Input(key='TELEFONE', font=('Consolas', 12))],
            [sg.Input(key='SAC', font=('Consolas', 12))],
            [sg.Input(key='EMAIL', font=('Consolas', 12))],
            [sg.Input(key='SITE', font=('Consolas', 12))],
    ]

    framePrincipalTexto = [
        [sg.Text('Razão Social:', font=('Consolas', 12))],
        [sg.Text('Nome Fantasia:', font=('Consolas', 12))],
        [sg.Text('CNPJ:', font=('Consolas', 12))],
        [sg.Text('I. Estadual:', font=('Consolas', 12))],
        [sg.Text('I. Municipal:', font=('Consolas', 12))],
    ]
    framePrincipalInput = [
            [sg.Input(key='RAZAOSOCIAL', font=('Consolas', 12))],
            [sg.Input(key='NOMEFANTASIA', font=('Consolas', 12))],
            [sg.Input(key='CNPJ', font=('Consolas', 12))],
            [sg.Input(key='IE', font=('Consolas', 12))],
            [sg.Input(key='IM', font=('Consolas', 12))],
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

    janelaCadastroCliente = sg.Window('Incluir Cliente', layout, finalize=True)

    while True:
        event, values = janelaCadastroCliente.read()
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

            sql = f"INSERT INTO TFORNECEDOR ({colunas}) VALUES ({valores})"
            yn = sg.popup_yes_no('Salvar as informações?')
            if yn == 'Yes':
                cursor.execute(sql)
                banco.commit()
                sg.popup('Fornecedor cadastrado')

        fornecedores = []

        sql = "SELECT * FROM TFORNECEDOR"
        cursor.execute(sql)
        r = cursor.fetchall()
        for x in r:
            fornecedores.append(x)


        return fornecedores