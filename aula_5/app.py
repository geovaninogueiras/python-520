import threading

from modules import banco

if __name__ == '__main__':

    try:
        thread = threading.Thread(target=banco.ler_mensagem)
        thread.start()
        
    except Exception as err:
        print('Erro: {}'.format(err))
        exit()


    nickname = input('Informe o seu nome: ')
    
    while True:
        mensagem = input('Digite a sua mensagem: ')
        banco.cadastrar_mensagem(nickname, mensagem)
        