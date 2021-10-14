def alterar(banco, cursor, contratos, indice):
    import PySimpleGUI as sg
    from datetime import date, datetime
    from interface import janelaClientes

    total = 0
    data_parcelas = []

    for x in indice:
        contrato = contratos[x]
    sql = f"SELECT * FROM TCLIENTE WHERE NOME='{contrato[1]}'"
    cursor.execute(sql)
    cliente = cursor.fetchone()
    sql = f"SELECT * FROM TFALECIDO WHERE CONTRATANTE='{cliente[0]}'"
    cursor.execute(sql)
    falecido = cursor.fetchone()
    sql = f"SELECT * FROM TRECEBER WHERE IDCLIENTE='{cliente[0]}'"
    cursor.execute(sql)
    parcelas = cursor.fetchall()
    for x in parcelas:
        total = float(x[5])
        valor_escrito = x[12]
        nome_vendedor = x[13]
        valor_entrada = float(x[6])
        qtde_parcelas = x[3]
        data_parcelas.append((x[2], x[7], x[4]))


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
        [sg.Input(key='-NOME_CLIENTE-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), readonly=True, default_text=cliente[1]), 
            sg.Button('Pesquisar Cliente', key='-PESQUISAR_CLIENTE-')],
        [sg.Text('', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Text('DADOS DO FALECIDO', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Input(key='-NOME_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[2])],
        [sg.Input(key='-CPF_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[3])],
        [sg.Input(key='-RG_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[4])],
        [sg.Input(key='-ENDERECO_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[5])],
        [sg.Input(key='-DATA_NASC_FALECIDO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[6])],
        [sg.Input(key='-FALECIDO_EM-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[7])],
        [sg.Input(key='-HORA_OBITO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[8])],
        [sg.Input(key='-SEPUTADO_EM-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[9])],
        [sg.Input(key='-LOCAL_OBITO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[10])],
        [sg.Input(key='-NOME_MEDICO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[11])],
        [sg.Input(key='-NOME_CEMITERIO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(26,1), default_text=falecido[12])],
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
        [sg.Text(f'{total:.2f}', font=('Consolas', 16), text_color='#333', background_color='#FFF')],
        [sg.Input(key='-VALOR_ESCRITO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(16,1), default_text=valor_escrito)],
        [sg.Input(key='-NOME_VENDEDOR-', font=('Consolas', 16), text_color='#333', background_color='#FFF', size=(16,1), default_text=nome_vendedor)],
        [sg.Combo(formasPagamento, key='-FORMAS_PAGAMENTO-', default_value=formasPagamento[0], readonly=True, font=('Consolas', 16), text_color='#333')],
        [sg.Input(key='-VALOR_ENTRADA-', font=('Consolas', 16), text_color='#333', background_color='#FFF', default_text=f"{valor_entrada:.2f}", focus=True, size=(7,1))],
        [sg.Input(key='-QTDE_PARCELAS-', font=('Consolas', 16), text_color='#333', background_color='#FFF', default_text=qtde_parcelas, size=(7,1))],
        [sg.Input(key='-DIA_FIXO_PAGAMENTO-', font=('Consolas', 16), text_color='#333', background_color='#FFF', default_text='1', size=(7,1))],
        [sg.Input(key='-INTERVALO_PARCELAS-', font=('Consolas', 16), text_color='#333', background_color='#FFF', default_text='0', size=(7,1))],
    ]

    frame_parcelas = [
        [sg.Table(values=data_parcelas, headings=colunas, visible_column_map=None, col_widths=11, def_col_width=11, auto_size_columns=False, max_col_width=100, row_height=30,
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

    janelaAlterarContrato = sg.Window('Alterar Contrato', layout, finalize=True, background_color='#fff', auto_size_text=True)
    dateList = []
    while True:
        event, values = janelaAlterarContrato.read()
        
        a = date.today().toordinal()

        if event == sg.WIN_CLOSED:
            break

        if event == '-PESQUISAR_CLIENTE-':
            cliente = janelaClientes.janela(banco, cursor)
            janelaAlterarContrato['-NOME_CLIENTE-'].Update(cliente[1])