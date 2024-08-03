# definir funcoes
# nome seguido de underline e verbos

from flask import Flask, render_template, request, flash
import csv
from CSV import *
from reserva_app.app import *

# imports do csv:
cad_usuarios = 'CSV/cadastro-usuario.csv'
cad_sala = 'CSV/cadastro-sala.csv'
res_sala = 'CSV/reserva-sala.csv'


# funcoes de armazenamento dos dados dos formularios
def salvar_cadastro():
    if request.method == 'POST':
        #pega cada requisição do form
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        #escreve os dados de entrada no csv
        with open(cad_usuarios, 'a', newline='') as usuarios_cadastros:
            escrever = csv.writer(usuarios_cadastros)
            escrever.writerow([nome, email, senha])
        return render_template('reservas.html')

            
def salvar_sala():
    if request.method == 'POST':
        # se o forms for enviado, pega cada campo do formulário
        tipo = request.form['tipo']
        capacidade = request.form['capacidade']
        descricao = request.form['descricao']

        # escreve no CSV
        with open(cad_sala, 'a', newline='') as salas_cadastros:
            escrever = csv.writer(salas_cadastros)
            escrever.writerow([tipo, capacidade, descricao])
        

def salvar_reserva():
    if request.method == 'POST':
       # se o forms for enviado, pega cada campo do formulário
        sala = request.form['sala']
        inicio = request.form['inicio']
        final = request.form['final']

        # escreve no CSV       
        with open(res_sala, 'a', newline='') as reservas_salas:
            escrever = csv.writer(reservas_salas)
            escrever.writerow([sala, inicio, final])

        return {
            'sala' : sala,
            'inicio' : inicio,
            'final' : final
        }


# funcoes de leitura e exibição dos dados no csv
def ler_salas_csv():
    salas = []
    with open(cad_sala, 'r', newline='') as reservas_salas:
        leitor = csv.reader(reservas_salas)
        next(leitor)  # Pula o cabeçalho se houver

        for idx, linha in enumerate(leitor, start=1):
            sala = {
                'id': idx,
                'tipo': linha[0],
                'capacidade': linha[1],
                'descricao': linha[2]
            }
            salas.append(sala)

    return salas
# tentatva da leitura do cadastro-sala.csv
    



#def ler_reservas_csv():
#    reservas = []
#    with open(res_sala, 'r', newline='') as reservas_salas:
#        leitor = csv.reader(reservas_salas)
#        next(leitor)  # Pula o cabeçalho se houver
#        
#        for idx, linha in enumerate(leitor, start=1):
#            reserva = {
#                'sala': sala[0],
#                'inicio': inicio[1],
#                'final': final[2]
#            }
#            reservas.append(reserva)
#  
#   return reservas
#



