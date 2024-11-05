from reserva_app.conexao_bd import conexao_fechar, conexao_abrir
from reserva_app.funcoes import *


# METODOS DE RESERVA


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

#  METODOS DE USUARIO

def inserir_usuario(con, nome, email, senha):
    cursor = con.cursor()
    sql = "INSERT INTO usuario (nomeUsuario, emailUsuario, senhaUsuario) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, email, senha))
    con.commit()
    cursor.close()


def listar_usuarios(con):
    cursor = con.cursor(dictionary=True)  # Criar o cursor com a opção de retorno como dicionário
    sqlcode = "SELECT * FROM usuario"
    cursor.execute(sqlcode)

    for usuario in cursor:
        print(f"Usuario: {usuario['idUsuario']} - Nome: {usuario['nomeUsuario']} - Email: {usuario['emailUsuario']} - Senha: {usuario['senhaUsuario']} ")

    cursor.close()
    con.commit()

# METODOS DE SALA

def listar_salas(con):
    cursor = con.cursor(dictionary=True)  # Criar o cursor com a opção de retorno como dicionário
    sqlcode = "SELECT * FROM sala"
    cursor.execute(sqlcode)

    salaslista = []
    for sala in cursor:
        print(f"Sala: {sala['idSala']} - Tipo: {sala['tipoSala']} - Capacidade: {sala['capacidadeSala']} - Descrição: {sala['descricaoSala']}")
        salaslista.append(sala)
    
    cursor.close()
    con.commit()
    return salaslista

def inserir_sala(con, tipo, capacidade, descricao):
    cursor = con.cursor()
    sql = "INSERT INTO sala (tipoSala, capacidadeSala, descricaoSala) VALUES (%s,%s, %s)"
    cursor.execute(sql, (tipo, capacidade, descricao))
    con.commit()
    cursor.close()

def deletar_sala(con, id):
    cursor = con.cursor()
    sql = "DELETE from sala WHERE idSala = %s"
    cursor.execute(sql, (id))
    con.commit()
    cursor.close()

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