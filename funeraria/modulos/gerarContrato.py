


def geraContrato(val, cursor, banco):
    from PIL import Image, ImageFont, ImageDraw
    import os
    from datetime import date, datetime
    import PySimpleGUI as sg
    path = os.path.dirname(__file__)
    
    my_image = Image.open(f"{path}\\contratoPage1.png")
    my_image2 = Image.open(f"{path}\\contratoPage2.png")
    empresa_font = ImageFont.truetype('C:\\WINDOWS\\FONTS\\ARIAL.TTF', 24)
    text_font = ImageFont.truetype('C:\\WINDOWS\\FONTS\\ARIAL.TTF', 36)
    clausula_font = ImageFont.truetype('C:\\WINDOWS\\FONTS\\ARIAL.TTF', 36)
    title_font = ImageFont.truetype('C:\\WINDOWS\\FONTS\\ARIAL.TTF', 20)
    title_bold_font = ImageFont.truetype('C:\\WINDOWS\\FONTS\\ARIAL.TTF', 20)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((500,200), val.get('empresa'), (0, 0, 0), font=empresa_font)
    image_editable.text((500,225), val.get('endereco_empresa'), (0, 0, 0), font=empresa_font)
    image_editable.text((500,250), val.get('cidade_empresa'), (0, 0, 0), font=empresa_font)
    image_editable.text((500,275), val.get('cnpj_empresa'), (0, 0, 0), font=empresa_font)
    image_editable.text((500,300), val.get('telefone_empresa'), (0, 0, 0), font=empresa_font)
    image_editable.text((500,325), val.get('email_empresa'), (0, 0, 0), font=empresa_font)
    image_editable.text((1190,302), val.get('vendedor'), (0, 0, 0), font=title_font)
    image_editable.text((1190,265), val.get('emissao'), (0, 0, 0), font=title_font)
    image_editable.text((1355,225), val.get('n_contrato'), (0, 0, 0), font=title_font)
    image_editable.text((100,450), val.get('cod_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((220,450), val.get('nome_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((715,450), val.get('cpf_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((990,450), val.get('rg_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((1210,450), val.get('nasc_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((100,510), val.get('endereco_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((890,510), val.get('telefone_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((100,570), val.get('cidade_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((640,570), val.get('uf_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((720,570), val.get('cep_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((890,570), val.get('complemento_contratante'), (0, 0, 0), font=title_font)
    image_editable.text((90,610), val.get('texto_1'), (0, 0, 0), font=text_font)
    image_editable.text((90, 790), 'Clausula 1º.', (0, 0, 0), font=clausula_font)
    image_editable.text((300, 792), 'É objeto do presente contrato a prestação dos serviços fúnebres de:', (0, 0, 0), font=text_font)
    image_editable.text((100,865), val.get('cod_falecido'), (0, 0, 0), font=title_font)
    image_editable.text((220,865), val.get('nome_falecido'), (0, 0, 0), font=title_font)
    image_editable.text((720,865), val.get('nasc_falecido'), (0, 0, 0), font=title_font)
    image_editable.text((905,865), val.get('seputado_em'), (0, 0, 0), font=title_font)
    image_editable.text((1210,865), val.get('local'), (0, 0, 0), font=title_font)
    image_editable.text((90,900), 'Contendo o(s) seguinte(s) item(ns) e serviço(s)', (0, 0, 0), font=text_font)
    linha = 970
    image_editable.text((90,linha), ('. '*67), (0, 0, 0), font=title_font)
    linha += 30
    total_prod = 0
    total_desconto = 0
    total = 0
    for x in val.get('produtos'):
        if len(x) > 3:
            total_prod += float(x[2])
            total_desconto += float(x[3])
            total += float(x[2])
            image_editable.text((1320,linha), f"{float(x[3]):.2f}", (0, 0, 0), font=title_font)

        else:
            total_prod += float(x[2])
            total += float(x[2])
        
        image_editable.text((90,linha), str(x[1]), (0, 0, 0), font=title_font)
        image_editable.text((950,linha), 'UN', (0, 0, 0), font=title_font)
        image_editable.text((1010,linha), f"{float(x[0]):.2f}", (0, 0, 0), font=title_font)
        image_editable.text((1450,linha), f"{float(x[2]):.2f}", (0, 0, 0), font=title_font)
        linha += 30
    image_editable.text((90,linha-20), ('. '*67), (0, 0, 0), font=title_font)
    image_editable.text((1010,linha), 'Totais:', (0, 0, 0), font=title_bold_font)
    image_editable.text((1200,linha), f"{total_prod:.2f}", (0, 0, 0), font=title_bold_font)
    image_editable.text((1320,linha), f"{total_desconto:.2f}", (0, 0, 0), font=title_bold_font)
    image_editable.text((1450,linha), f"{total:.2f}", (0, 0, 0), font=title_bold_font)
    image_editable.text((90,1320), 'Clausula 2º. ', (0, 0, 0), font=clausula_font)
    image_editable.text((300,1320), str(val.get('text_2')), (0, 0, 0), font=text_font)
    image_editable.text((90,1360), f"R$ {total:.2f}({val.get('valor_escrito')})", (0, 0, 0), font=clausula_font)
    image_editable.text((90,1400), str(val.get('text_2_continue')), (0, 0, 0), font=text_font)

    my_image.save(f"{val.get('save_path')}{val.get('nome_contratante')}-{date.today()}-pagina1.png")
    my_image2.show()
    my_image.show()


    import base64
    with open(f"{val.get('save_path')}{val.get('nome_contratante')}-{date.today()}-pagina1.png", "rb") as img_file:
        my_string = str(base64.b64encode(img_file.read()))
    my_string = my_string.replace("'", " ")
    my_string = my_string.lstrip("b ")


    escolha = sg.popup_yes_no('Deseja gravar este contrato?')
    if escolha == 'Yes':
        sql = f"INSERT INTO CONTRATOS VALUES ('', '{val.get('nome_contratante')}', 1, '{my_string}')"
        cursor.execute(sql)
        banco.commit()

    file = f"{val.get('save_path')}{val.get('nome_contratante')}-{date.today()}-pagina1.png"
    os.remove(file)



