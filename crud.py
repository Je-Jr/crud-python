import sqlite3



conexao = sqlite3.connect("basededados.db")

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "nome TEXT,"
                "peso REAL"
                ") ")


def fecharConexao():
    cursor.close()
    conexao.close()


def mostrarDados():
    p = cursor.execute('SELECT * FROM clientes')
    for linha in p:
        print(linha)    

def inserirDados(name, weight):
    cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("{}", {})'.format(name, float(weight)))
    conexao.commit()

def deletarRegistro(id):
    cursor.execute("DELETE FROM clientes WHERE id = {}".format(int(id)))
    conexao.commit()

acao = input("1 - mostrar dados\n 2 - inserir dados\n 3 - deletar dados\n")

if acao == "1":
    mostrarDados()
elif acao == "2":
    nome = input("Digite um nome: ")
    peso = input("Digite um peso: ")
    inserirDados(nome, peso)
elif acao == "3":
    registro = input("Digite o identificador do registro: ")
    deletarRegistro(registro)



        
fecharConexao()

input("press enter to finish")
