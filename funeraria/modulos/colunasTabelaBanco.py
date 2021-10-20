def colunas(cursor, tabela):
    sql = f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{tabela}'"
    cursor.execute(sql)
    r = cursor.fetchall()
    colunas = []
    for x in r:
        colunas.append(x[3])
    
    return colunas