# Selenioum

usuario = {
    'nome' : input('Informe o seu Nome: ' ),
    'idade' : input('Informe a sua Idade: '),
    'email' : input('Informe o seu E-Mail: '),
}

nome = usuario['nome']

print('Usuario {} cadastrado com sucesso!'.format(usuario))

print(usuario)
print(type(usuario))

print(usuario['nome'])
print(type(usuario['nome']))

print(usuario['idade'])
print(type(usuario['idade']))

exit()

#----------------------------------------------------------------

# Nomes de variaveos

# Constante
GRAVIDADE = 9.8

# Variaveis
primeiro_nome = 'Geovani'
segundo_nome = 'Nogueira'
ultimo_nome = 'Santos'

idade = '25'
idade = 25

professor  = True

# Verificando typeOf
print( type(GRAVIDADE));

variavel = 'string'
print(type(variavel))

variavel = 121
print(type(variavel))

variavel = True
print(type(variavel))

exit()

#----------------------------------------------------------------

print('hello, world')

condicao = 'Geovani Nogueira Santos'
print(type(condicao))

condicao = 24
print(type(condicao))

condicao = True
print(type(condicao))

if condicao:
    print('Verdade')
else:
    erro