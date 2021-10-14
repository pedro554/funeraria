import PySimpleGUI as sg
from datetime import date, datetime
import random
from interface import janelaClientes
from modulos import gerarContrato
from random import randint
import os

def parcelar(banco, cursor, totalVenda, produtos, path):
    d = date.today()
    colunas = ['N PARCELA', 'VALOR', 'DATA']
    parcelas = []
    formasPagamento = ['Dinheiro', 'Débito', 'Crédito']

    frame_selecionar_cliente = [
        [sg.Text('Cliente:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Nome Falecido:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('CPF:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('RG:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Endereço:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Data Nascimento:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Falecido em:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Hora do Óbito:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Seputado em:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Local do Óbito:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Nome do Médico:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Nome do Cemitério/Local:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
    ]

    frame_input_selecionar_cliente = [
        [sg.Input(key='-NOME_CLIENTE-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), readonly=True), sg.Button('Pesquisar Cliente', key='-PESQUISAR_CLIENTE-')],
        [sg.Text('', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('DADOS DO FALECIDO', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Input(key='-NOME_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-CPF_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-RG_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-ENDERECO_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-DATA_NASC_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-FALECIDO_EM-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-HORA_OBITO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-SEPUTADO_EM-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-LOCAL_OBITO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-NOME_MEDICO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
        [sg.Input(key='-NOME_CEMITERIO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1))],
    ]


    frame_texto = [
        [sg.Text('Total: R$', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Valor Escrito:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Vendedor:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Forma de Pagamento:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Entrada: R$', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Qtde Parcelas:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Dia fixo para pagamento:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('Intervalo entre parcelas:', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
    ]

    frame_input = [
        [sg.Text(f'{totalVenda:.2f}', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Input(key='-VALOR_ESCRITO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(16,1))],
        [sg.Input(key='-NOME_VENDEDOR-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(16,1))],
        [sg.Combo(formasPagamento, key='-FORMAS_PAGAMENTO-', default_value=formasPagamento[0], readonly=True, font=('Consolas', 16), text_color='#333')],
        [sg.Input(key='-VALOR_ENTRADA-', font=('Consolas', 16), text_color='#333', background_color='#FFF', default_text='0', focus=True, size=(7,1))],
        [sg.Input(key='-QTDE_PARCELAS-', font=('Consolas', 16), text_color='#333', background_color='#FFF', default_text='1', size=(7,1))],
        [sg.Input(key='-DIA_FIXO_PAGAMENTO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', default_text='1', size=(7,1))],
        [sg.Input(key='-INTERVALO_PARCELAS-', font=('Consolas', 16), text_color='#333', background_color='#FFF', default_text='0', size=(7,1))],
    ]

    frame_parcelas = [
        [sg.Table(values=parcelas, headings=colunas, visible_column_map=None, col_widths=11, def_col_width=11, auto_size_columns=False, max_col_width=100, row_height=30,
            font = ('Concolas', 16), justification = "left", text_color = '#333', background_color = '#ddd', alternating_row_color = '#ccc', header_text_color = '#000', header_background_color = '#ddd',
            header_font = ('Concolas', 16), size = (None, None), enable_events = True, key='-TABELA_PARCELAS-')]
    ]

    frame_direito = [
        [sg.Frame('', frame_texto, relief='flat', background_color='#FFF'), sg.Frame('', frame_input, relief='flat', background_color='#FFF')],
        [sg.Frame('', frame_parcelas, relief='flat', background_color='#FFF')]
    ]
    frame_esquerdo = [
        [sg.Frame('', frame_selecionar_cliente, relief='flat', background_color='#FFF'), sg.Frame('', frame_input_selecionar_cliente, relief='flat', background_color='#FFF')],
        [sg.Button('Excluir Parcelas', key='-EXCLUIR_PARCELAS-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333")),
        sg.Button('Finalizar Venda', key='-FINALIZAR-', border_width=0, size=(20, 2), button_color='#666', font=('Consolas Bold', 12), mouseover_colors = ("#fff", "#333"))],
        [sg.Button(key='-ATUALIZAR_PARCELAS-', bind_return_key=True, visible=False)],
    ]

    layout = [
        [sg.Frame('', frame_direito, relief='flat', background_color='#FFF'), sg.Frame('', frame_esquerdo, relief='flat', background_color='#FFF')],
        
    ]

    janelaParcelarVenda = sg.Window('Finalizar Cartão', layout, finalize=True, background_color='#fff', auto_size_text=True)
    dateList = []
    while True:
        event, values = janelaParcelarVenda.read()
        
        a = date.today().toordinal()

        if event == sg.WIN_CLOSED:
            break

        if event == '-PESQUISAR_CLIENTE-':
            cliente = janelaClientes.janela(banco, cursor)
            janelaParcelarVenda['-NOME_CLIENTE-'].Update(cliente[1])

        if event == '-ATUALIZAR_PARCELAS-':
            if int(values.get('-INTERVALO_PARCELAS-')) != 0:
                intervalo_parcelas = int(values.get('-INTERVALO_PARCELAS-'))
                n_parcelas = int(values.get('-QTDE_PARCELAS-'))
                for i in range(0, n_parcelas):
                    d = date.fromordinal(a + intervalo_parcelas)
                    dateList.append((f"{d.year}-{d.month}-{d.day}"))
                    a = a + intervalo_parcelas

            else:
                dia_fixo_pagamento = int(values.get('-DIA_FIXO_PAGAMENTO-'))
                n_parcelas = int(values.get('-QTDE_PARCELAS-'))
                count = 1
                d = date.fromordinal(a)
                mes = d.month
                ano = d.year
                for i in range(0, n_parcelas):
                    if mes + count >= 13:
                        count = 0
                        mes = 1
                        ano += 1
                    dateList.append((f"{ano}-{mes+count}-{dia_fixo_pagamento}"))
                    count+=1

            for i in range(0, n_parcelas):
                valorEntrada = float(values.get('-VALOR_ENTRADA-'))
                valor = (totalVenda - valorEntrada) / n_parcelas
                parcelas.append((i+1 , f"R$ {valor:.2f}", f'{dateList[i]}'))
            janelaParcelarVenda['-TABELA_PARCELAS-'].Update(parcelas)

        if event == '-EXCLUIR_PARCELAS-':
                parcelas = []
                janelaParcelarVenda['-TABELA_PARCELAS-'].Update(parcelas)

        if event == '-FINALIZAR-':
                documento = random.random()
                documento = str(documento).split('.')
                documento = documento[1]

                for i in range(0, len(produtos)):
                    sqlEstoque = f"UPDATE TESTOQUE SET QTDE=(QTDE - {float(produtos[i][0])}), DATAULTIMAVENDA='{datetime.now()}' WHERE PRODUTO='{produtos[i][1]}'"
                    cursor.execute(sqlEstoque)
                    banco.commit()
                for i in range(0, len(dateList)):
                    sqlReceber = f"INSERT INTO TRECEBER VALUES ('', '{cliente[0]}', '{i+1}', '{n_parcelas}','{dateList[i]}', '{totalVenda}', '{valorEntrada}', '{valor}', '', '0', '0', '{documento}', '{str(values.get('-VALOR_ESCRITO-'))}', '{str(values.get('-NOME_VENDEDOR-'))}')"
                    cursor.execute(sqlReceber)
                    banco.commit()
            #try:
                sqlFalecido = f"INSERT INTO TFALECIDO VALUES ('', {documento},'{str(values.get('-NOME_FALECIDO-'))}', '{str(values.get('-CPF_FALECIDO-'))}', '{str(values.get('-RG_FALECIDO-'))}', '{str(values.get('-ENDERECO_FALECIDO-'))}', '{str(values.get('-DATA_NASC_FALECIDO-'))}', '{str(values.get('-FALECIDO_EM-'))}', '{str(values.get('-HORA_OBITO-'))}', '{str(values.get('-SEPUTADO_EM-'))}', '{str(values.get('-LOCAL_OBITO-'))}', '{str(values.get('-NOME_MEDICO-'))}', '{str(values.get('-NOME_CEMITERIO-'))}', '{cliente[0]}')"
                cursor.execute(sqlFalecido)
                banco.commit()
                sql = "SELECT ID FROM TFALECIDO WHERE CPF='" + str(values.get('-CPF_FALECIDO-')) + "'"
                cursor.execute(sql)
                falecido = cursor.fetchone()
            
                gerarContrato.geraContrato({
                'empresa': 'TAC PLAN PLANOS ASSISTENCIAIS',
                'endereco_empresa': 'RUA DR VERGÍLIO NASCIMENTO - CENTRO',
                'cidade_empresa': 'BOSSOROCA (RS) CEP 97850-000',
                'cnpj_empresa': 'CNPJ: 33.872.970/0001-36',
                'telefone_empresa': 'Telefone: (55) 3356-1078',
                'email_empresa': 'E-mail: assistencialtacplan@gmail.com',
                'vendedor': str(values.get('-NOME_VENDEDOR-')),
                'emissao': f"{d.day}/{d.month}/{d.year}",
                'n_contrato': str(documento),
                'cod_contratante': str(cliente[0]),
                'nome_contratante': str(cliente[1]),
                'cpf_contratante': str(cliente[3]),
                'rg_contratante': str(cliente[2]),
                'nasc_contratante': str(cliente[6]),
                'endereco_contratante': f"{cliente[8]}-{cliente[10]}",
                'telefone_contratante': str(cliente[4]),
                'cidade_contratante': str(cliente[11]),
                'uf_contratante': str(cliente[12]),
                'cep_contratante': str(cliente[13]),
                'complemento_contratante': str(cliente[9]),
                'texto_1': '''As partes acima identificadas têm, justo e acertado o presente contrato de prestação
de serviço, que se regerá pelas cláusulas seguintes e pelas condições de preço, forma e
termo de pagamento descritas no presente.''',
                'cod_falecido': str(falecido[0]),
                'nome_falecido': str(values.get('-NOME_FALECIDO-')),
                'nasc_falecido': str(values.get('-DATA_NASC_FALECIDO-')),
                'seputado_em': str(values.get('-SEPUTADO_EM-')),
                'local': str(values.get('-NOME_CEMITERIO-')),
                'produtos': produtos,
                'valor_escrito': str(values.get('-VALOR_ESCRITO-')),
                'text_2': 'O presnete serviço será remunerado pela quantia total de:',
                'text_2_continue': '''referente ao(s) item(ns) e serviço(s) efetivamente prestado(s), e será pago na seguinte
condição:''',
                'save_path': f"{path}\\contratos\\"
                }, cursor, banco)
                janelaParcelarVenda.close()
                sg.popup('Venda efetuada')
                break
            #except:
                #sg.popup('Preencha todos os valores!')

