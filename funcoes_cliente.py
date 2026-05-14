from banco import conectar
import sqlite3

def cadastrar_cliente():
    try:
        print("--- NOVO CLIENTE ---")
        nome = input("Digite o nome: ").strip()
        email = input("Digite o e-mail: ").strip()

        if not nome or not email:
            print("❌ ERRO: O nome e o e-mail não podem ficar em branco.")
            return
        
        conexao = conectar()
        cursor = conexao.cursor()

        cmd_sql = "INSERT INTO clientes (nome, email) VALUES (?, ?)"

        cursor.execute(cmd_sql, (nome, email))
        conexao.commit()

        if cursor.rowcount == 0:
            print("⚠️ Cliente não inserido no banco")
        else:
            print("✅ Cliente cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")

    finally:
        if conexao:
            conexao.close()


def listar_clientes():
    try:
        print("--- LISTA DE CLIENTES ---")

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()

        if len(resultados) == 0:
            print("Nenhum cliente cadastrado ainda.")
        else:
            for cliente in resultados:
                print(f"ID: {cliente[0]} | Nome: {cliente[1]} | E-mail: {cliente[2]}")
    
    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")

    finally:
        if conexao:
            conexao.close()


def atualizar_email():
    try:
        print("--- ATUALIZAR E-MAIL ---")
        conexao = conectar()
        cursor = conexao.cursor()

        id_cliente = int(input("Digite o ID do cliente: "))
        novo_email = input("Digite o novo e-mail: ").strip()

        if not novo_email:
            print("❌ ERRO: O e-mail não pode ficar em branco.")
            return

        cmd_sql = "UPDATE clientes SET email = ? WHERE id = ?"
        cursor.execute(cmd_sql, (novo_email, id_cliente))
        conexao.commit()

        if cursor.rowcount == 0:
            print("❌ ERRO: Cliente não encontrado.")
        else:
            print("✅ E-mail atualizado com sucesso!")

    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")
    except ValueError:
        print("❌ ERRO: O ID precisa ser um número inteiro.")
    finally:
        if conexao:
            conexao.close()


def excluir_cliente():
    try:
        print("--- EXCLUIR CLIENTE ---")
        conexao = conectar()
        cursor = conexao.cursor()

        id_cliente = int(input("Digite o ID do cliente a ser excluído: "))

        cmd_sql = "DELETE FROM clientes WHERE id = ?"
        cursor.execute(cmd_sql, (id_cliente, ))
        conexao.commit()

        if cursor.rowcount == 0:
            print("❌ ERRO: Cliente não existe.")
        else:
            print("✅ Cliente excluido do sistema.")

    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")
    except ValueError:
        print("❌ ERRO: O ID precisa ser um número inteiro.")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    # cadastrar_cliente()
    listar_clientes()
    # atualizar_email()
    # excluir_cliente()