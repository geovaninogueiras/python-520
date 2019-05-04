
usuario = {
    'data_cadastro': datetime.datetime.now(),
    'nome': input('Digite seu nome: '),
    'email': input('Digite seu email: '),
    'idade': input('Digite sua idade: '),        
}

# o objeto deve ter um método
# e_maior_de_idade()

class Usuario:
    
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def maior_de_idade(self):
        if self.idade > 17:
            return True
        return False

class Cadastrador:

    def cadastrar_usuario(self):

        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        idade = int(input('Digite sua idade: '))

        return Usuario(nome, email, idade)

cadastrador = Cadastrador()

usuario = cadastrador.cadastrar_usuario()

if not usuario.maior_de_idade():
    print('Requer mais de 18 anos')
else:
    print('Permitido')
