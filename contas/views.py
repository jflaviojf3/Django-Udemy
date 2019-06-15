from django.shortcuts import render
from .models import Transacao
from django.http import HttpResponse

import datetime

def home (request):
    data = {}
    data['transacoes'] = ['conta faculdade', 'conta oi', 'conta amil']
    
    data['now'] = datetime.datetime.now()
    #html = "<html><body>A Hora agora é: %s.</body></html>" % now
    
    return render(request, 'contas/home.html', data)

def listagem (request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)
