
from flask import Flask, render_template
from CSV import *
import csv
from reserva_app.funcoes import ler_salas_csv, salvar_sala, salvar_reserva, salvar_cadastro

app = Flask (__name__)


# definir rotas
# nome seguido de hifen e igual no html!

# login
@app.route('/')
def login_pag():
    return render_template('login.html') 
# cadastro usuario
@app.route('/cadastro')
def cadastro_pag():
    return render_template('cadastro.html')
# reservar sala
@app.route('/reservar-sala')
def reservar_sala_pag():
    return render_template ('reservar-sala.html')
# reservas
@app.route('/reservas')
def reservas_pag():
    return render_template ('reservas.html')
# detalhe reserva
@app.route('/detalhe-reserva')
def detalhe_reserva_pag():
    return render_template ('reserva/detalhe-reserva.html')
# cadastrar sala
@app.route('/cadastrar-sala')
def cadastro_sala_pag():
    return render_template ('cadastrar-sala.html')
# listar sala
@app.route('/listar-salas')
def listar_salas():
    salas = ler_salas_csv()
    return render_template('listar-salas.html', salas=salas)

#rotas ok, não mexer!



# ROTAS COM POST

@app.route('/cadastro', methods=['POST'])
def cadastro_post():
    salvar_cadastro()
    return render_template('reservas.html')

@app.route('/cadastrar-sala', methods=['POST'])
def salas_post():
    salvar_sala()
    return render_template('listar-salas.html')

@app.route('/reservar-sala', methods=['POST'])
def reservas_post():
    salvar_reserva()
    return render_template('reserva/detalhe-reserva.html')



# ROTAS DE LEITURA DO CSV

@app.route('/listar-salas')
def listar_salas():
    salas = ler_salas_csv()
    print(f"Salas carregadas: {salas}")  # Adiciona uma mensagem de depuração
    return render_template('listar-salas.html', salas=salas)

#tentatva da leitura do cadastro-sala.csv
    
