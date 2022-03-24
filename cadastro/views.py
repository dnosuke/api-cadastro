from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Pessoa
import random

# Create your views here.
@api_view(['GET'])
def pessoas_view(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        output = [{
            'login': cadastro.login,
            'senha': cadastro.senha,
            'data': cadastro.data
        }for cadastro in pessoas]
        return Response(output)

def generate_random_password (length):
    characters = ('abcdefghijklmnopqrstuvxyz')
    random_password = ''
    for x in range(length):
        random_password+= random.choice(characters)
    return random_password   

@api_view(['POST'])
def new_pessoa_view(request):
    if request.method == 'POST':
        login=request.data.get('login')
        requested_password = request.data.get('senha')
        date = request.data.get('data')

        password = requested_password if requested_password != '' else generate_random_password(10)

        pessoa = Pessoa.objects.create(login=login,
            senha=password, data=date)
        
        return Response({
            'login': pessoa.login,
            'senha': pessoa.senha,
            'data': pessoa.data
        })
    return Response(request.data)