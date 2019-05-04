
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    user='admin',
    password='4linux',
    host='127.0.0.1',
    database='projeto'
)

cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

def cadastrar_usuario(nome, email, idade):
    
    cursor.execute('''
        SELECT * FROM users WHERE email = '{}'
    '''.format(email))

    results = cursor.fetchall()
    
    if len(results) == 0:
        cursor.execute('''
            INSERT INTO users (nome, email, idade)
            VALUES ('{}', '{}', {})
        '''.format(nome, email, idade))
        conn.commit()

def extrair_usuarios():
    cursor.execute('SELECT * FROM users;')
    return cursor.fetchall()

cadastrar_usuario(
    'Lucas Ricciardi de Salles', 
    'lucas.salle@4linux.com.br',
    25
)

for usuario in extrair_usuarios():
    print(usuario)