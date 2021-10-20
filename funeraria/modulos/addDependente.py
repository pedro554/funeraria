

def add(banco, cursor, idcliente, idplano):
    import PySimpleGUI as sg
    from datetime import date

    frame_texto = [
        [sg.Text('Nome:', font=('Consolas', 12))],
        [sg.Text('RG:', font=('Consolas', 12))],
        [sg.Text('CPF:', font=('Consolas', 12))],
        [sg.Text('Endereço:', font=('Consolas', 12))],
        [sg.Text('Complemento:', font=('Consolas', 12))],
        [sg.Text('Bairro:', font=('Consolas', 12))],
        [sg.Text('Cidade:', font=('Consolas', 12))],
        [sg.Text('UF:', font=('Consolas', 12))],
        [sg.Text('Pais:', font=('Consolas', 12))]
    ]
    frame_input = [
        [sg.Input(key='-NOME-', font=('Consolas', 12))],
        [sg.Input(key='-RG-', font=('Consolas', 12))],
        [sg.Input(key='-CPF-', font=('Consolas', 12))],
        [sg.Input(key='-ENDERECO-', font=('Consolas', 12))],
        [sg.Input(key='-COMPLEMENTO-', font=('Consolas', 12))],
        [sg.Input(key='-BAIRRO-', font=('Consolas', 12))],
        [sg.Input(key='-CIDADE-', font=('Consolas', 12))],
        [sg.Input(key='-UF-', font=('Consolas', 12))],
        [sg.Input(key='-PAIS-', font=('Consolas', 12))]
    ]

    layout = [
        [sg.Frame('', frame_texto, relief='flat'), sg.Frame('', frame_input, relief='flat')],
        [sg.Button('Salvar', key='-SALVAR-', font=('Consolas', 12))]
    ]

    janelaAddDependente = sg.Window('Adicionar Dependente', layout, finalize=True)

    while True:
        event, values = janelaAddDependente.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-SALVAR-':
            nome = values.get('-NOME-')
            rg = values.get('-RG-')
            cpf = values.get('-CPF-')
            endereco = values.get('-ENDERECO-')
            complemento = values.get('-COMPLEMENTO-')
            bairro = values.get('-BAIRRO-')
            cidade = values.get('-CIDADE-')
            uf = values.get('-UF-')
            pais = values.get('-PAIS-')
            sql = f"INSERT INTO TDEPENDENTE VALUES ('', '{idcliente}', '{idplano}', '{nome}', '{rg}', '{cpf}', '{endereco}', '{complemento}', '{bairro}', '{cidade}', '{uf}', '{pais}', '{date.today()}')"
            cursor.execute(sql)
            banco.commit()
            janelaAddDependente.close()
            sg.popup('Dependente Adicionado')
            return values