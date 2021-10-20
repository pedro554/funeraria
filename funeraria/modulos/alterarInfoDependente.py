

def alterar(banco, cursor, dependente):
    import PySimpleGUI as sg
    from datetime import date
    from interface import janelaPlanos

    sql = f"SELECT * FROM TPLANOS WHERE ID='{dependente[2]}'"
    cursor.execute(sql)
    plano = cursor.fetchone()

    frame_texto = [
        [sg.Text('Plano:', font=('Consolas', 12))],
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
        [sg.Input(key='-PLANO-', font=('Consolas', 12), default_text=plano[1], readonly=True), sg.Button('Pesquisar', key='-PESQUISAR-')],
        [sg.Input(key='-NOME-', font=('Consolas', 12), default_text=dependente[3])],
        [sg.Input(key='-RG-', font=('Consolas', 12), default_text=dependente[4])],
        [sg.Input(key='-CPF-', font=('Consolas', 12), default_text=dependente[5])],
        [sg.Input(key='-ENDERECO-', font=('Consolas', 12), default_text=dependente[6])],
        [sg.Input(key='-COMPLEMENTO-', font=('Consolas', 12), default_text=dependente[7])],
        [sg.Input(key='-BAIRRO-', font=('Consolas', 12), default_text=dependente[8])],
        [sg.Input(key='-CIDADE-', font=('Consolas', 12), default_text=dependente[9])],
        [sg.Input(key='-UF-', font=('Consolas', 12), default_text=dependente[10])],
        [sg.Input(key='-PAIS-', font=('Consolas', 12), default_text=dependente[11])]
    ]

    layout = [
        [sg.Frame('', frame_texto, relief='flat'), sg.Frame('', frame_input, relief='flat')],
        [sg.Button('Salvar', key='-SALVAR-', font=('Consolas', 12))]
    ]

    janelaAlterarInfoDependente = sg.Window('Alterar Informações do Dependente', layout, finalize=True)

    while True:
        event, values = janelaAlterarInfoDependente.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == '-PESQUISAR-':
            plano = janelaPlanos.janelaPlanos(banco, cursor)
            janelaAlterarInfoDependente['-PLANO-'].Update(plano[1])

        elif event == '-SALVAR-':
            try:
                sql = f"SELECT * FROM TPLANOS WHERE PLANO='{values.get('-PLANO-')}'"
                cursor.execute(sql)
                plano = cursor.fetchone()
                nome = values.get('-NOME-')
                rg = values.get('-RG-')
                cpf = values.get('-CPF-')
                endereco = values.get('-ENDERECO-')
                complemento = values.get('-COMPLEMENTO-')
                bairro = values.get('-BAIRRO-')
                cidade = values.get('-CIDADE-')
                uf = values.get('-UF-')
                pais = values.get('-PAIS-')
                sql = f"UPDATE TDEPENDENTE SET IDPLANO='{plano[0]}', NOMEDEPENDENTE='{nome}', RG='{rg}', CPF='{cpf}', ENDERECO='{endereco}', BAIRRO='{bairro}', CIDADE='{cidade}', UF='{uf}', PAIS='{pais}' WHERE ID='{dependente[0]}'"
                cursor.execute(sql)
                banco.commit()
                janelaAlterarInfoDependente.close()
                sg.popup('Dependente Alterado')
                break
            except:
                sg.popup('Preencha todas as informações')

    sql = f"SELECT NOMEDEPENDENTE FROM TDEPENDENTE WHERE ID='{dependente[0]}'"
    cursor.execute(sql)
    nome = cursor.fetchone()[0]

    return nome