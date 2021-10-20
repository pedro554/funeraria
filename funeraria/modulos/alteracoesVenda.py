from interface.janelaClientes import janela
import PySimpleGUI as sg


def alterarQuantidade(indice, produtos):
    produto = produtos[indice]
    produtos.pop(indice)
    frame1 = [
        [sg.Text('Qtde. anterior:', font=('Consolas', 16), text_color='#333', background_color='#aaa')],
        [sg.Text('Nova Qtde.:', font=('Consolas', 16), text_color='#333', background_color='#aaa')],
    ]

    frame2 = [
        [sg.Input(key='-QTDE_ANTERIOR-', default_text=f'{produto[0]}', background_color='#aaa', font=('Consolas', 16), readonly=True, size=(7,1))],
        [sg.Input(key='-QTDE_ATUAL-', size=(7,1), font=('Consolas', 16))]
    ]

    layout = [
        [sg.Frame('', frame1, relief='flat', background_color='#aaa'), sg.Frame('', frame2, relief='flat', background_color='#aaa')],
        [sg.Button(key='-ALTERAR-', bind_return_key=True, visible=False)],
    ]

    janelaAlterarQuantidade = sg.Window('Alterar quantidade', layout, finalize=True, background_color='#aaa')

    while True:
        event, values = janelaAlterarQuantidade.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-ALTERAR-':
            qtde = int(values.get('-QTDE_ATUAL-'))
            desc = produto[1]
            valor = qtde * float(produto[2])
            produto = (qtde, desc, valor)
            janelaAlterarQuantidade.close()
            sg.popup('Quantidade alterada')
            break

    return produto