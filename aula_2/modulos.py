import os
import datetime
import subprocess
import time
import random

def get_input_nome(mensagem):
    
    usuario = input(mensagem)
    
    return usuario
    

def get_input_email(mensagem):
    
    email = input(mensagem)

    return email

def get_input_idade(mensagem):
    
    idade = input(mensagem)

    return idade

def cadastrar_usuario():
    usuario = {
        'data_cadastro': datetime.datetime.now(),
        'nome': get_input_nome('Informe o nome do usuário: '),
        'email': get_input_email('Informe o e-mail do usuário: '),
        'idade': get_input_idade('Informe a idade do usuário: ')
    }

    return usuario

probabilidade = random.random()
if probabilidade < 0.5:
    cadastrar_usuario()
else:
    print('Opa, não deu sorte...')

exit()

list_cadastro = cadastrar_usuario()

subprocess.run(['clear']) # Serve para limpar a tela

start_time = time.clock()
time.sleep(10.0)  # pausa a aplicação por um determinado tempo
print('Tempo gasto = {}'.format(time.clock() - start_time))

d = list_cadastro['data_cadastro']
print( d.strftime('%d %m %Y'))