
import users

def cadastrar_usuario():

    name = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    idade = input('Digite sua idade: ')

    user = users.User(name, email, idade)

    if not user.exists():
        user.save()
        print('Usuário cadastrado com sucesso')
    else:
        print('Usuário já existe')

def adicionar_role():

    email = input('Digite seu email: ')

    user = users.User.find_by_email(email)
    if not user:
        print('Usuário não encontrado')
        exit()

    role = input('Digite o nome da permissão: ')

    user.add_role(role)
    user.save()

    print('Role adicionada com sucesso')

done = False
while not done:

    print('1 - Adicionar novo usuário: ')
    print('2 - Adicionar role a usuário existente')
    print('3 - Sair')

    option = int(input('Selecione uma das opções acima: '))

    if option == 1:
        cadastrar_usuario()

    elif option == 2:
        adicionar_role()

    else:
        done = True