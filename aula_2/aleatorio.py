import random
import string

# Constantes em python
ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gerar_nome_aleatorio():
    # Python <= 3.5
    #
    # string = ''
    # for n in range(random.randint(5,15)):
    #     string += random.choice(ASCII_LETTERS)
    # return string

    # Python >= 3.6
    return ''.join(
        random.choices(
            string.ascii_letters,
            k=random.randint(5, 25)
        )
    )

def gerar_email_aleatorio():
    return gerar_nome_aleatorio() + '@emailteste.com.br'

def gerar_idade_aleatorio():
    return random.randint(24,55)

def gerar_usuario_aleatorio():
    novo_usuario = {
        'nome' : gerar_nome_aleatorio(),
        'email': gerar_email_aleatorio(),
        'idade': gerar_idade_aleatorio()
    }

    return novo_usuario

# Garante que esses print's só vão quando este arquivo for testado.
if __name__ == '__name__':
    print( 'Rode seus testes sem erro de eles atrapalharem' )
    print( 'Arquivo aleatorio.py: {}'.format(__name__))