# Aula 02 - Revisão da aula 01
lista_de_gatos = [
    {
        'nome' : 'gato',
        'peso': 5000,
        'idade': 6,
        'apelido' : 'sedoso'
    }, 
    {
        'nome':'fernando',
        'peso': 3750,
        'idade':3,
        'apelido':'brilhoso'
    }]

def get_input_as_num( mensagem, erro ):
    
    userinput = input(mensagem)
    # 
    # for token in userinput:
    #     if token not in '0123456789':
    #         return -1
    #
    # return int(userinput)
    try:
        return int( userinput)
    except ValueError:
        raise ValueError(erro)

def tratamento_de_tentativas(numeto_tentativas, mensagem, error):
    for tentativa in range(numeto_tentativas):
        try:
            return get_input_as_num(mensagem, error)
        except ValueError as erro:
            restantes - numeto_tentativas - (tentativa+1)
            print('Um erro aconteceu')
            print(erro)

    print( 'Você errou o input {} vezes.'.format(numeto_tentativas) )
    print( 'Vou encerar o programa' )
    exit()

novo_gato = {
    'nome':input('Informe o nome do gato: '),
    'peso': tratamento_de_tentativas(
        5, 'Informe o peso do gato: ', 'O peso deve ser um número maior que ZERO.'
    ),
    'idade': tratamento_de_tentativas(
        5, 'Informe a idade do gato: ', 'A idade deve ser um número maior que ZERO.'
    ),
    'apelido':input('Informe o pelido do gato: ')
}

lista_de_gatos.append( novo_gato )

for gato in lista_de_gatos:
    print('Peso do gato: {}'.format(gato['peso']))
    if gato['peso'] > 4000:
        print('Ele é o gato')
    else:
        print('Ela é a Malawi')

exit()

# packing
ponto = 4, 5

# Teste de sanidade do interpretador
print('hello, world')