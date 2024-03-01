from django.shortcuts import render, redirect
from selenium import webdriver
from django.contrib import messages
import time

def automação():
    try:
        driver = webdriver.Chrome()
        driver.get('https://pncp.gov.br/app/editais?q=&status=recebendo_proposta&pagina=1')
        time.sleep(1)
        driver.close()
        return True
    except Exception:
        return False

def pagina_inicial(request):
    return render(request, 'index.html')
    
def buscar_dados(request):
    if request.method == 'GET':
        modalidade = request.GET.get('modalidade')
        uf = request.GET.get('uf')
        print(modalidade, uf)
        automacao = automação()
        if automacao:
            messages.success(request, 'Dados recuperados com sucesso')
            return redirect('/')
        else:
            messages.warning(request, 'Erro ao recuperar os dados')
            return redirect('/')
    else:
        return render(request, 'index.html')
