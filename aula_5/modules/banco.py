import os
import time

import pymongo
import dotenv

dotenv.load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL')

try:

    client = pymongo.MongoClient(MONGODB_URL)

    db = client.chat

except Exception as err:
    print('Erro: {}'.format(err))
    exit()

def cadastrar_mensagem(nome, mensagem):
    db.mensagens.insert({
        'nome': nome,
        'mensagem': mensagem,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    })

def ler_mensagem():
    ultima = [
        x for x in db.mensagens.find().sort('_id', pymongo.DESCENDING)
    ]

    while True:
        atual = [
            x for x in db.mensagens.find().sort('_id', pymongo.DESCENDING)
        ]

        if atual != ultima:
            ultima = atual
            print('[{}] {} : {} \n'.format(
                atual[0]['hora'], atual[0]['nome'], atual[0]['mensagem']
            ))

        time.sleep(1.0/30.0)
