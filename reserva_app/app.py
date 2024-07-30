from flask import Flask, render_template, Request
import csv
from funcoes import salva_cadastro

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
def listar_salas_pag():
    return render_template ('listar-salas.html')

#rotas ok, não mexer!






# ROTAS COM POST

@app.route('/cadastro', methods=['POST'])
def cadastro_post():
    salva_cadastro()
    return render_template('reservas.html')

