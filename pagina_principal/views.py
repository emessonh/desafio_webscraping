from django.shortcuts import render, redirect
from selenium import webdriver
from django.contrib import messages
import time
import pandas as pd
import os
from .models import SETOP
import requests

usuario = os.getlogin()
sequencia_mes = {'Janeiro':'01', 'Marco':'03', 'Abril':'04', 'Junho':'06', 'Julho':'07', 'Agosto':'08', 'Setembro':'09',
                         'Outubro':'10'}

def pagina_inicial(request):
    return render(request, 'index.html')

def ler_excel(regiao, ano, mes, desoneracao):
    excel = pd.read_excel(rf'C:\Users\{usuario}\Downloads\{ano}{sequencia_mes[mes]}_Planilha_Precos_SETOP_{regiao}_{desoneracao}.xlsx', sheet_name='Relatório')
    return excel

def automacao(regiao, referencia, desoneracao, link):
    driver = webdriver.Chrome()
    try:
        regiao_dividida = regiao.split('_')
        regiao_nome_link = regiao_dividida[0]
        referencia_dividida = referencia.split('/')
        ano = referencia_dividida[0]
        mes = referencia_dividida[1]
        desoneracao_traco = desoneracao.replace('_', '-')
        desoneracao_maiusculo = desoneracao.upper()
        driver.get(link)
        time.sleep(15)
        driver.close()
        return True
    except Exception:
        driver.close()
        return False
    
# Escreve no banco
def banco(regiao, ano, mes, desoneracao):
    excel = ler_excel(regiao, ano, mes, desoneracao)
    c = 0
    colunas_puladas = []
    while True:
        colunas_puladas.append(c)
        if str(excel.iloc[c, 0]).lower() == 'código':
            break
        c += 1

    excel_tratado = pd.read_excel(rf'C:\Users\{usuario}\Downloads\{ano}{sequencia_mes[mes]}_Planilha_Precos_SETOP_{regiao}_{desoneracao}.xlsx', sheet_name='Relatório', skiprows=colunas_puladas).rename(columns={'CÓDIGO':'codigo', 'DESCRIÇÃO DO SERVIÇO':'descricao', 'UNIDADE':'unidade', 'CUSTO UNITÁRIO':'custo_unitario'})
    excel_tratado = excel_tratado.drop(index=len(excel_tratado)-1)
    colunas_excel = excel_tratado.columns

    if len(colunas_excel) > 4:
        for coluna in colunas_excel.values:
            if coluna not in ['codigo', 'descricao', 'unidade', 'custo_unitario']:
                excel_tratado = excel_tratado.drop(columns=[coluna])

    # adiciona no banco
    SETOP.objects.bulk_create([SETOP(codigo=row['codigo'], descricao=row['descricao'], unidade=row['unidade'], custo_unitario=row['custo_unitario']) for index, row in excel_tratado.iterrows()])
    return True
    
def buscar_dados(request):
    if request.method == 'GET':
        regiao = request.GET.get('regiao')
        referencia = request.GET.get('referencia')
        desoneracao = request.GET.get('desoneracao')

        regiao_dividida = regiao.split('_')
        regiao_nome_link = regiao_dividida[0]
        desoneracao_maiusculo = desoneracao.upper()
        desoneracao_traco = desoneracao.replace('_', '-') 
        referencia_dividida = referencia.split('/')
        ano = referencia_dividida[0]
        mes = referencia_dividida[1]

        # Verifica qual o link e aciona a automação
        link = f'http://www.infraestrutura.mg.gov.br/images/documentos/precosetop/{ano}/Planilha-Precos-SETOP-{ano}/{sequencia_mes[mes]}-{mes}/{desoneracao_traco}/{ano}{sequencia_mes[mes]}_Planilha_Precos_SETOP_{regiao_nome_link}_{desoneracao_maiusculo}.xlsx'
        resposta = requests.get(link)
        resposta_auto = None
        if resposta.status_code == 200:
            resposta_auto = automacao(regiao, referencia, desoneracao, link)

        extracao_banco = banco(regiao_nome_link, ano, mes, desoneracao_maiusculo)
        if resposta_auto == True and extracao_banco == True:
            messages.success(request, 'Dados recuperados com sucesso')
            return redirect('/')
        else:
            messages.warning(request, 'Erro ao recuperar os dados')
            return redirect('/')

    else:
        return render(request, 'index.html')