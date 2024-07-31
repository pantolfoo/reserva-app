# definir funcoes
# nome seguido de underline e verbos

from flask import request 
import csv, CSV


cad_usuarios = 'CSV/cadastro-usuario.csv'

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