import CSV, csv
from flask import Flask, request ,csv


# definir funcoes
# nome seguido de underline 

usuarios = 'cadastro-usuario.csv'

def salva_cadastro(nome,email,senha):
    if request.method == 'POST':
        #pega cada requisição do form
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        #escreve os dados de entrada no csv
        with open(usuarios, 'a', newline='') as arquivo_cadastros:
            escrever = csv.writer(arquivo_cadastros)
            escrever.writerow([nome, email, senha])