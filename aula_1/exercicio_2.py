list_usuarios = [
  {
    "nome": "nfGVelWlILJEOjT",
    "idade": 32
  },
  {
    "nome": "uDRPRSHVoJokVwuR",
    "idade": 30
  },
  {
    "nome": "TnEMEWFhNFUbFVhvy",
    "idade": 43
  },
  {
    "nome": "ZwRzZeYRam",
    "idade": 26
  },
  {
    "nome": "mDOsqRmysEYmhQsVXg",
    "idade": 23
  },
  {
    "nome": "iqHMYKzJHgkVAnDkbHc",
    "idade": 35
  },
  {
    "nome": "RFyKuOeMIkLHb",
    "idade": 33
  },
  {
    "nome": "FZksBLrFBEpNCsEmB",
    "idade": 28
  },
  {
    "nome": "VHMWWJyZyLMKBYphvJq",
    "idade": 44
  },
  {
    "nome": "HCkcPvCjkJCPcmsCIlKH",
    "idade": 39
  },
  {
    "nome": "EPXKAHzEdVqUQsxUHea",
    "idade": 40
  },
  {
    "nome": "yOxoMtlSZlsGuU",
    "idade": 46
  },
  {
    "nome": "akfoJPtDbgqjfJ",
    "idade": 42
  },
  {
    "nome": "ADPTSubBPwYloFggX",
    "idade": 39
  },
  {
    "nome": "YBpEOkmiHwJQUgsJpsQN",
    "idade": 21
  },
  {
    "nome": "CdeRWIMIKtzxuoHuCSG",
    "idade": 25
  },
  {
    "nome": "TVvOiIkYXMATz",
    "idade": 48
  },
  {
    "nome": "uhyWGBPyiBRyLjYdcuk",
    "idade": 31
  },
  {
    "nome": "xdnsnLMhdVrYxYq",
    "idade": 24
  },
  {
    "nome": "KmUimTYUUUqJHTi",
    "idade": 32
  }
]

lista_opcoes = ['Cadastrar novo usuário', 'Listar usuário existentes', 'Deletar usuário', 'Sair']
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

        usuario_new = {
            'nome' : input('Informe o seu Nome: ' ),
            'idade' : input('Informe a sua Idade: ')
        }   

        list_usuarios.append( usuario_new )

    elif opcao == 2:
        print( '' )
        print( '------------ Imprimindo o Cadastro com idade maior que 30 ------------' )

        i = 0
        for n in list_usuarios:
            i += 1    
            if n['idade'] > 30:
                print( str(i) + ' - ' + n['nome'])
            
    elif opcao == 3:
        
        print( '' )
        print( '------------ Excluir o Cadastro ------------' )

        if len( list_usuarios) > 0:

            i = 0
            for n in usuarios:
                print( str(i) + ' - ' + n['nome'])
                i += 1

            opcao = int( input('Escolha uma opção para excluir: ') )

            if opcao > len( list_usuarios):
                print( '' )
                print( '------------ Opção escolhida é invalida ------------' ) 
            else:
                list_usuarios.__delitem__(opcao)
                print( '' )
                print( '------------ Usuário excluido ------------' ) 

        else:
            print( '' )
            print( '------------ Sem nenhum usuário cadastrado ------------' )

    else:
        print( '' )
        print( '------------ Saindo do Programa ------------' )
        break
    