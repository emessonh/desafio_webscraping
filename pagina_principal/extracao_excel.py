import pandas as pd
import sqlite3
from sqlite3 import Error


def ler_excel(ano, mes):
    excel = pd.read_excel(r'fonte_dados_excel\central\2023_agosto.xlsx', sheet_name='Relatório')
    return excel

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

excel = ler_excel(2023, 'abril')
c = 0
colunas_puladas = []
while True:
    colunas_puladas.append(c)
    if str(excel.iloc[c, 0]).lower() == 'código':
        break
    c += 1

excel_tratado = pd.read_excel(r'fonte_dados_excel\central\2023_agosto.xlsx', sheet_name='Relatório', skiprows=colunas_puladas).rename(columns={'CÓDIGO':'codigo', 'DESCRIÇÃO DO SERVIÇO':'descricao', 'UNIDADE':'unidade', 'CUSTO UNITÁRIO':'custo_unitario'})

excel_tratado = excel_tratado.drop(index=len(excel_tratado)-1)
colunas_excel = excel_tratado.columns

if len(colunas_excel) > 4:
    for coluna in colunas_excel.values:
        if coluna not in ['codigo', 'descricao', 'unidade', 'custo_unitario']:
            excel_tratado = excel_tratado.drop(columns=[coluna])

# adiciona no banco
database = r'web_scraping\db.sqlite3'
conn = create_connection(database)
excel_tratado.to_sql('pagina_principal_setop',conn,index=False,if_exists='append')
conn.close()
print(excel_tratado)
# print(colunas_excel.values)

