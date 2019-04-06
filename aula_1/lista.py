lista_opcoes = ['Cadastrar novo usuário', 'Listar usuário existentes', 'Deletar usuário', 'Sair']
list_Novo = []
i = 0

while True:
    
    print( '' )
    print( '------------ Programa de Cadastros ------------' )
    print( '' )

    i = 0
    for n in lista_opcoes:
        i +=1
        print( ('{} - ' + n).format(++i) )

    print( '' )
    print( '' )
    
    opcao = int( input('Escolha uma opção: ') )

    if opcao > len(lista_opcoes):
        print( '' )
        print( '------------ Opção escolhida e invalida ------------' )
        print( '' ) 
    
    elif opcao == 1:
        
        print( '' )
        print( '------------ Novo Cadastro ------------' )
        print( '' )

        usuario = {
            'nome' : input('Informe o seu Nome: ' ),
            'idade' : input('Informe a sua Idade: '),
            'email' : input('Informe o seu E-Mail: ')
        }   

        list_Novo.append( usuario )

    elif opcao == 2:
        print( '' )
        print( '------------ Imprimindo o Cadastro ------------' )

        i = 0
        for n in list_Novo:
            i += 1    
            print( str(i) + ' - ' + n['nome'])
            
    elif opcao == 3:
        
        print( '' )
        print( '------------ Excluir o Cadastro ------------' )

        if len( list_Novo) > 0:

            i = 0
            for n in list_Novo:
                print( str(i) + ' - ' + n['nome'])
                i += 1

            opcao = int( input('Escolha uma opção para excluir: ') )

            if opcao > len( list_Novo):
                print( '' )
                print( '------------ Opção escolhida é invalida ------------' ) 
            else:
                list_Novo.__delitem__(opcao)
                print( '' )
                print( '------------ Usuário excluido ------------' ) 

        else:
            print( '' )
            print( '------------ Sem nenhum usuário cadastrado ------------' )

    else:
        print( '' )
        print( '------------ Saindo do Programa ------------' )
        break


exit()

#----------------------------------------------------------------


list_cadUsuario = []

for n in range(10):

    print( '' )
    print( '------------ Novo Cadastro ------------' )
    print( '' )

    usuario = {
        'nome' : input('Informe o seu Nome: ' ),
        'idade' : input('Informe a sua Idade: '),
        'email' : input('Informe o seu E-Mail: ')
    }   

    list_cadUsuario.append( usuario )


print( '' )
print( '------------ Imprimindo o Cadastro ------------' )

for n in list_cadUsuario:
    print('O nome do usuario e {}'.format(n['nome']))


exit()

#----------------------------------------------------------------

lista_porpulada = [1,2,3,4,5,6,7,8,9,10]
lista_vazia = []

#Populando a lista vazia
lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)
lista_vazia.append(4)
lista_vazia.append(5)
lista_vazia.append(6)
lista_vazia.append(7)
lista_vazia.append(8)
lista_vazia.append(9)
lista_vazia.append(10)

#Imprimindo as listas
print(lista_porpulada)
print(lista_vazia)

print("")

#Imprimindo apenas o Quinto elemento da lista.
print('Este e {} o quinto elemento da lista populada'.format(lista_porpulada[4]))
print('Este e {} o quinto elemento da lista vazia'.format(lista_vazia[4]))

print("")

print("Inicio do For")

#Imprimindo todos os elementos da lista
for n in lista_vazia:
    print('Imprimindo o numero ' + str(n) )

print('Fim do For')
