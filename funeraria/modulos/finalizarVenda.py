import PySimpleGUI as sg
import random
from datetime import datetime




def finalizarVenda(banco, cursor, total_venda, produtos):
    frame_forma_pagamento = [
        [sg.Text(f'Valor total: R${total_venda:.2f}', font=('Consolas', 16), text_color='#333', background_color='#aaa')], 
        [sg.Text('Valor restante: R$', font=('Consolas', 16), text_color='#333', background_color='#aaa'), 
        sg.Input(key='-VALOR_RESTANTE-', font=('Concolas', 16), background_color='#FFF', readonly=True, border_width=0, default_text=f"{total_venda:.2f}",
            disabled_readonly_background_color='#aaa', size=(7,1)),
            sg.Button(key='-ATUALIZAR-', visible=False, bind_return_key=True)],
    ]

    frame_input_forma_pagamento = [
        [sg.Input(key='-VALOR_DINHEIRO-', focus=True, default_text='0', size=(10, 1), font=('Concolas', 16), background_color='#aaa')],
        [sg.Input(key='-VALOR_DEBITO-', default_text='0', size=(10, 1), font=('Concolas', 16), background_color='#aaa')],
        [sg.Input(key='-VALOR_CREDITO-', default_text='0', size=(10, 1), font=('Concolas', 16), background_color='#aaa')],
    ]

    frameTextoFormaPagamento = [
        [sg.Text('DINHEIRO', font=('Consolas', 16), text_color='#333', background_color='#aaa')],
        [sg.Text('DÉBITO', font=('Consolas', 16), text_color='#333', background_color='#aaa')],
        [sg.Text('CRÉDITO', font=('Consolas', 16), text_color='#333', background_color='#aaa')],
    ]

    layout = [
        [sg.Frame('', frame_forma_pagamento,  background_color='#aaa', relief='flat')],
        [sg.Frame('', frameTextoFormaPagamento, background_color='#aaa', relief='flat'), sg.Frame('', frame_input_forma_pagamento, background_color='#aaa', relief='flat')],
        [sg.Button('Finalizar', key='-FINALIZAR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333"), visible=False)]
    ]

    janelaFormaPagamento = sg.Window('Finalizar venda', layout, finalize=True, background_color='#aaa')
    while True:
        event, values = janelaFormaPagamento.read()

        if event == sg.WIN_CLOSED:
            break
        
        if event == '-ATUALIZAR-':
            '''Calcula o troco que deve ser dado ao cliente e libera a venda'''
            dinheiro = float(values.get('-VALOR_DINHEIRO-'))
            debito = float(values.get('-VALOR_DEBITO-'))
            credito = float(values.get('-VALOR_CREDITO-'))
            valorRestante = total_venda
            totalPago = valorRestante - (dinheiro + debito + credito)
            janelaFormaPagamento['-VALOR_RESTANTE-'].Update(f"{totalPago:.2f}")
            if float(values.get('-VALOR_RESTANTE-')) == 0:
                janelaFormaPagamento['-FINALIZAR-'].Update(visible=True)

        if event == '-FINALIZAR-':
            documento = random.random()
            documento = str(documento).split('.')
            documento = documento[1]
            especie = ''
            if dinheiro != 0:
                especie += f'Dinheiro R${dinheiro},'
            if debito != 0:
                especie += f'Debito R${debito},'
            if credito != 0:
                especie += f'Credito R${credito},'
            especie = especie.rstrip(',')
            valorEntrada = total_venda

            for i in range(0, len(produtos)):
                sqlEstoque = f"UPDATE TESTOQUE SET QTDE=(QTDE - {float(produtos[i][0])}), DATAULTIMAVENDA='{datetime.now()}' WHERE PRODUTO='{produtos[i][1]}'"
                cursor.execute(sqlEstoque)
                banco.commit()
            janelaFormaPagamento.close()
            sqlCaixa = f"INSERT INTO TCAIXA (DOCUMENTO, ESPECIE, VALORENTRADA, DESCRICAOLANCAMENTO) VALUES ('{documento}', '{especie}', '{valorEntrada}', '{'VENDA RAPIDA'}')"
            cursor.execute(sqlCaixa)
            banco.commit()
            sg.popup('Venda efetuada')
            break



            