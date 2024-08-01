# definir funcoes
# nome seguido de underline e verbos

from flask import request, render_template, flash, redirect
import csv, CSV

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
        
        # condicional caso usuáio não preencha todos os campos
        if nome == '' or email == '' or senha == '':
            flash ("Preencha todos os campos!")
            return render_template('cadastro.html')

        else:
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

        # condicional caso usuáio não preencha todos os campos
        if tipo == '' or capacidade == '' or descricao == '':
            return render_template ('cadastrar-sala.html', erro = "Preencha todos os campos!")

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

        # condicional caso usuáio não preencha todos os campos
        if sala == '' or inicio == '' or final == '':
            return render_template ('cadastro.html', erro = "Preencha todos os campos!")

        
        # escreve no CSV
        with open(res_sala, 'a', newline='') as reservas_salas:
            escrever = csv.writer(reservas_salas)
            escrever.writerow([sala, inicio, final])
            
            

# funcoes de leitura e exibição dos dados no csv
#def ler_salas_csv():
#    salas = []
#    with open(cad_sala, 'r', newline='') as salas_cadastros:
#        leitor = csv.reader(salas_cadastros)
#        for linha in leitor:
#            salas.append({
#                'tipo': linha[0],
#                'capacidade': linha[1],
#                'descricao': linha[2]
#            })
#    return salas
# tentatva da leitura do cadastro-sala.csv
    


