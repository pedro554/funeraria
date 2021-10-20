import PySimpleGUI as sg



def alterarValor(indice, produtos):
    produto = produtos[indice]
    produtos.pop(indice)

    frame1 = [
        [sg.Text('Valor anterior: R$', font=('Consolas', 16), text_color='#333', background_color='#aaa')],
        [sg.Text('Novo valor: R$', font=('Consolas', 16), text_color='#333', background_color='#aaa')],
    ]

    frame2 = [
        [sg.Input(key='-VALOR_ANTERIOR-', default_text=f'{float(produto[2]):.2f}', background_color='#aaa', font=('Consolas', 16), readonly=True, size=(7,1))],
        [sg.Input(key='-VALOR_ATUAL-', size=(7,1), font=('Consolas', 16))]
    ]

    layout = [
        [sg.Frame('', frame1, relief='flat', background_color='#aaa'), sg.Frame('', frame2, relief='flat', background_color='#aaa')],
        [sg.Button(key='-ALTERAR-', bind_return_key=True, visible=False)],
    ]

    janelaAlterarValor = sg.Window('Alterar valor', layout, finalize=True, background_color='#aaa')

    while True:
        event, values = janelaAlterarValor.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-ALTERAR-':
            valorNovo = float(values.get('-VALOR_ATUAL-'))
            desc = produto[1]
            qtde = produto[0]
            valor_original = produto[2]
            valor_desconto = float(produto[2]) - valorNovo
            produto = (qtde, desc, valorNovo, valor_desconto, valor_original)
            print(produto)
            janelaAlterarValor.close()
            sg.popup('Valor alterado')
            break

    return produto