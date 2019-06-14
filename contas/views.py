from django.shortcuts import render
from django.http import HttpResponse

import datetime

def home (request):
    data = {}
    data['transacoes'] = ['conta faculdade', 'conta oi', 'conta amil']
    
    data['now'] = datetime.datetime.now()
    #html = "<html><body>A Hora agora é: %s.</body></html>" % now
    
    return render(request, 'contas/home.html', data)
