from conexao_bd import conexao_fechar, conexao_abrir
from funcoes import *

def listar_reserva(con):
    cursor = con.cursor(dictionary=True)  # Criar o cursor com a opção de retorno como dicionário
    sqlcode = "SELECT * FROM reserva"
    cursor.execute(sqlcode)

    for reserva in cursor:
        print(f"{reserva['idReserva']} - Sala: {reserva['idSala']} - Início: {reserva['inicioReserva']} - Final: {reserva['finalReserva']}")

    cursor.close()
    con.commit()

def inserir_reserva(con,inicio, final):
    cursor = con.cursor()
    sql = "INSERT INTO reserva (inicioReserva, finalReserva) VALUES (%s, %s)"
    cursor.execute(sql, (inicio, final))
    con.commit()
    cursor.close()

def main():
    con = conexao_abrir("localhost", "root", "1234", "ReservaApp")
    try:
        inserir_reserva(con, "2024-04-04 18:09:00", "2024-04-04 22:45:00")
        listar_reserva(con)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conexao_fechar(con)

if __name__ == "__main__":
    main()