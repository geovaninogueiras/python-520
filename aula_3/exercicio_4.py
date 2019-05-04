
import pymongo

client = pymongo.MongoClient()
db = client.projeto


def extrair_usuarios():
    return list(db.users.find())

def cadastrar_usuario(nome, email, idade):
    usuario = db.users.find_one({ 'email': email })
    if not usuario:
        db.users.insert({
            'nome': nome,
            'email': email,
            'idade': idade
        })
    
cadastrar_usuario(
    'Lucas Ricciardi de Salles', 
    'lucas.salle@4linux.com.br',
    25
)

for usuario in extrair_usuarios():
    print(usuario)