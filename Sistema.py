import mysql.connector
import PySimpleGUI as sg
from interface import interfacePrincipal
import os



banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='funeraria',
)
path = os.path.dirname(__file__)
cursor = banco.cursor(buffered=True)
interfacePrincipal.Inicio(banco, cursor, path)