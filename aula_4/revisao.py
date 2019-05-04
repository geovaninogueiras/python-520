# Revisão da Aula 03
# Escrever uma função que recebe 
# um número inteiro e retornar uma listar com os números
# menores ou iguais à esses menos o zero

# Ex: gerar_lista(5) -> [1,2,3,4,5]
#     gerar_lista(9) -> [1,2,3,4,5,6,7,8,9]

# Segundo Exercicio
def par(x):
    if x % 2 == 0:
        return True
    return False

def incremental(x):
    return x + 1

def gerar_lista_numeros_pares(numero):
    return[ ( i + 1 )  for i in range(numero+1) if par( i + 1)]

lista_de_numero_gerados = gerar_lista_numeros_pares(10)
for x in lista_de_numero_gerados:
    if not par(x):
        raise Exception('{} não é um número par'.format(x))


print(lista_de_numero_gerados)

exit()

# Primeiro Exercicio

# Geovani
def gerar_lista(tamanholista):
    lista = []
    
    for x in range(tamanholista):
        lista.append(x+1) 
    
    return lista

# 1 
def gerar_lista(n):
    lista, x = [], 1
    while x <= n:
        lista.append(x)
        x += 1

    return lista

# 2
def gerar_lista(tamanholista):
    lista = []
    
    for x in range(tamanholista):
        lista.append(x+1) 
    
    return lista

# 3 
def gerar_lista(tamanholista):
    return[ i + 1 for i in range(tamanholista)]

# 4 - Lambida
gerar_lista = lambda n: [ i + 1 for i in range(n)]

tamanholista = int(input('Informe o tamanho da lista: '))
lista_gerada = gerar_lista(tamanholista)
print(lista_gerada)