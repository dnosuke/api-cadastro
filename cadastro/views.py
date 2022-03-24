from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Pessoa
import random

# Create your views here.
@api_view(['GET', 'POST'])
def pessoas_view(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        output = [{
            'login': cadastro.login,
            'senha': cadastro.senha,
            'data': cadastro.data
        }for cadastro in pessoas]
        return Response(output)


@api_view(['GET','POST'])
def nova_pessoa_view(request):
    if request.method == 'POST':
        
        senha2 = request.data.get('senha')

        if senha2 == '':
            caracteres = ('abcdefghijklmnopqrstuvxyz')
            lenght = 10
            for x in range(lenght):
                senha2 += random.choice(caracteres)

            pessoa = Pessoa.objects.create(login=request.data.get('login'),
            senha=senha2, data=request.data.get('data'))
        else:
            pessoa = Pessoa.objects.create(login=request.data.get('login'),senha=request.data.get('senha'), data=request.data.get('data'))
        

        output = {
            'senha': pessoa.senha,
            'login': pessoa.login,
            'data': pessoa.data
        }
        return Response(output)
    return Response(request.data)