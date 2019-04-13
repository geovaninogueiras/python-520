# Exercicos Aula 02

# Missão 1
# Criar uma função 'cadastrar_usuario'
# que retorno um dicionario de usuário,
# O dicionário deve conter a propriedades:
#
#   - nome
#   - email
#   - idade
#
# e os valores devem ser digitados 
# pelo usuário através do terminal


lista_de_cadastros = []

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


lista_de_cadastros.append( cadastrar_usuario() )


