import mysql.connector
import PySimpleGUI as sg
from interface import interfacePrincipal
import os
from modulos import version

path = os.path.dirname(__file__)

a = path.split('\\')
a.pop(-1)
b = ''
for x in a:
    b += x + '\\'
att = version.check(f"{b}\\version.json", b)
if att == True:
    banco = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='funeraria',
    )
    cursor = banco.cursor(buffered=True)
    interfacePrincipal.Inicio(banco, cursor, path)
else:
    sg.popup('Sistema DESATUALIZADO!\nExecute o exe da Atualização')