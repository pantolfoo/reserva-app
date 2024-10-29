from flask import Flask, render_template
from reserva_app.funcoes import salvar_sala, salvar_reserva, salvar_cadastro, ler_salas

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
    print(ler_salas())
    return render_template ('reservar-sala.html', salas = ler_salas())
# , salas = ler_salas_csv()
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

#rotas ok, não mexer!



# ROTAS COM POST

@app.route('/cadastro', methods=['POST'])
def cadastro_post():
    salvar_cadastro()
    return render_template('reservas.html')

@app.route('/cadastrar-sala', methods=['POST'])
def salas_post():
    salvar_sala()
    return render_template('listar-salas.html', salas = ler_salas())

@app.route('/reservar-sala', methods=['POST'])
def reservas_post():
    reserva = salvar_reserva()
    return render_template('reserva/detalhe-reserva.html', reserva = reserva)



# ROTAS DE LEITURA DO CSV

@app.route('/listar-salas')
def listar_salas():
    salas = ler_salas()
    print(f"Salas carregadas: {salas}")
    return render_template('listar-salas.html', salas=salas)
#tentatva da leitura do cadastro-sala.csv
    
