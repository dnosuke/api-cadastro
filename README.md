Projeto de: Alain Delon Machado da Cunha
email: alaindelonm@gmail.com

# Cadastro - API

Cadastro é uma Django api para cadastro de pessoas.

## Description

As informações cadastradas podem ser consultadas através do endpoint:
- /pessoas 

O utilizador poderá cadastrar pessoas fornecendo login, senha e data de nascimento no seguinte endpoint:
- /pessoas/new

## Instalação

criando ambiente virtual e instalando os requerimentos.

```bash
python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt
```

## Executando o programa

```bash

>> python manage.py makemigrations
>> python manage.py migrate
>> python manage.py runserver

```

## License
[MIT](https://choosealicense.com/licenses/mit/)
