
try:
    idade = int(input('Digite sua idade: '))
    print('Sua idade é {}'.format(idade))
except:
    print('Idade inválida')

print('Sempre será executado')

exit()

variavel = 5
variavel = 5 + 5

def soma(a, b):
    return a + b

variavel = soma(5, 5)

apelido = soma
variavel = apelido(2, 2)

resultado_bool = variavel < 10

if resultado_bool:
    print('Entre 5 e 10')
elif variavel < 5:
    print('Menor do que 5')
else:
    print('Maior do que 10')

lista_de_numeros = [ resultado_bool, apelido, variavel, 4, 5 ]
for numero in lista_de_numeros:
    if numero % 2 == 0:
        print('Par')
else:
    print('Impar')
    
x = 0
while x < 10:
    print('Hello, world de novo')
    x = x + 1

