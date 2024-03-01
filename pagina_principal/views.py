from django.shortcuts import render
from selenium import webdriver
import time

def automação():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.selenium.dev/selenium/web/web-form.html')
        time.sleep(1)
        driver.close()
        return True
    except Exception:
        return False

def pagina_inicial(request):
    # if request.method == 'GET':
    #     automacao = automação()
    #     if automacao:
    #         return render(request, 'index.html', {'msg': 'Dados recuperados com sucesso'})
    #     else:
    #         return render(request, 'index.html', {'msg': 'Erro ao recuperar dados'})
    # else:
    return render(request, 'index.html')
    
def buscar_dados(request):
    if request.method == 'GET':
        automacao = automação()
        if automacao:
            return render(request, 'index.html', {'msg': 'Dados recuperados com sucesso'})
        else:
            return render(request, 'index.html', {'msg': 'Erro ao recuperar dados'})
    else:
        return render(request,{'msg': 'Erro ao processar envio do formulário'})
