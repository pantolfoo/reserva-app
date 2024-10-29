from reserva_app.conexao_bd import conexao_fechar, conexao_abrir
from reserva_app.funcoes import *

def listar_reserva(con):
    cursor = con.cursor(dictionary=True)  # Criar o cursor com a opção de retorno como dicionário
    sqlcode = "SELECT * FROM reserva"
    cursor.execute(sqlcode)

    for reserva in cursor:
        print(f"{reserva['idReserva']} - Sala: {reserva['idSala']} - Início: {reserva['inicioReserva']} - Final: {reserva['finalReserva']} - Feita por usuario: {reserva['idUsuario']}")

    cursor.close()
    con.commit()

def inserir_reserva(con,idSala, inicio, final, idUsuario):
    cursor = con.cursor()
    sql = "INSERT INTO reserva (idSala, inicioReserva, finalReserva, idUsuario) VALUES (%s,%s,%s, %s)"
    cursor.execute(sql, (idSala ,inicio, final, idUsuario))
    con.commit()
    cursor.close()

def listar_salas(con):
    cursor = con.cursor(dictionary=True)  # Criar o cursor com a opção de retorno como dicionário
    sqlcode = "SELECT * FROM sala"
    cursor.execute(sqlcode)

    for sala in cursor:
        print(f"Sala: {sala['idSala']} - Tipo: {sala['tipoSala']} - Capacidade: {sala['capacidadeSala']} - Descrição: {sala['descricaoSala']}")

    cursor.close()
    con.commit()

def listar_usuarios(con):
    cursor = con.cursor(dictionary=True)  # Criar o cursor com a opção de retorno como dicionário
    sqlcode = "SELECT * FROM usuario"
    cursor.execute(sqlcode)

    for usuario in cursor:
        print(f"Usuario: {usuario['idUsuario']} - Nome: {usuario['nomeUsuario']} - Email: {usuario['emailUsuario']} - Senha: {usuario['senhaUsuario']} ")

    cursor.close()
    con.commit()


def main():
    con = conexao_abrir("localhost", "root", "1234", "ReservaApp")
    try:
        listar_reserva(con)
        listar_salas(con)
        listar_usuarios(con)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conexao_fechar(con)

if __name__ == "__main__":
    main()