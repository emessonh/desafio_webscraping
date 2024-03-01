from django.shortcuts import render

def pagina_inicial(request):
    if request.method == 'POST':
        return render(request, 'index.html', {'msg': 'Recuperando dados...'})
    else:
        return render(request, 'index.html')
