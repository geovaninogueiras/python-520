
import aleatorio
import json

def gera_csv( lista ):
    TEMPLATE  = '{};{};{}'
    CABECALHO  = TEMPLATE.format('nome', 'idade', 'email')
    print(CABECALHO)
    for email in lista:
        email_formatado = TEMPLATE.format(
            email['nome'],
            email['idade'],
            email['email']
        )
        print(email_formatado)

def imprimir_bonito(obj):
    print(json.dumps(obj, indent=2))

def gerar_lista_usuarios(n):
    lista = []
    for i in range(n):
        u = aleatorio.gerar_usuario_aleatorio()
        lista.append(u)
    
    return lista


lista_de_usuario = gerar_lista_usuarios(100)

lista_1 = [0,1,2,3,4,5,6,7,8,9]
lista_2 = [x * 2 for x in lista_1 if x % 2 == 0 ]

# 1 - Imprima somente os usuário com mais de 30 anos
for usuario in lista_de_usuario:
    if usuario['idade'] > 30:
        # print(usuario)
        # print('O usuário {} tem mais de {} anos'.format(usuario['nome'], usuario['idade']))
        # imprimir_bonito(usuario)
        pass

# 2 - Filtrem somente pelos email que contém 'a'ou 'd'
#       e imprimam um arquivo 'relatorio.cvs' separado por :
#   

def valid_email(x):
    email = x['email'].lower()
    if 'a' in email or 'd' in email:
        return True
    
    return False

# lista_filtrada = [ x for x in lista_de_usuario if valid_email(x) == True ]
# gera_csv( lista_filtrada )
gera_csv( u for u in lista_de_usuario if valid_email(u) ) # forma mais eficiente


#Ver compreenção de lista!!!
