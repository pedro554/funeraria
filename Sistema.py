import mysql.connector
import PySimpleGUI as sg
from interface import interfacePrincipal
import os
from modulos import version

path = os.path.dirname(__file__)

path = path.split('\\')
path.pop(-1)
a = ''
for x in path:
    a += x + '\\'

att = version.check(f"{a}\\version.json", a)
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