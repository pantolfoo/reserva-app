from flask import Flask, render_template, request, flash

# Classe para gerenciar dados de usuários, salas e reservas
class DadosReservas:
    def __init__(self):
        self.usuarios = []
        self.salas = []
        self.reservas = []

    def salvar_usuario(self, nome, email, senha):
        self.usuarios.append({'nome': nome, 'email': email, 'senha': senha})

    def salvar_sala(self, tipo, capacidade, descricao):
        self.salas.append({'tipo': tipo, 'capacidade': capacidade, 'descricao': descricao})

    def salvar_reserva(self, sala, inicio, final):
        self.reservas.append({'sala': sala, 'inicio': inicio, 'final': final})

    def retornar_usuarios(self):
        return self.usuarios

    def retornar_salas(self):
        return self.salas

    def retornar_reservas(self):
        return self.reservas

# Instanciando a classe
dados_reservas = DadosReservas()

# Funções de armazenamento dos dados dos formulários
def salvar_cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        # Salva usuário na lista
        dados_reservas.salvar_usuario(nome, email, senha)
        return render_template('reservas.html')

def salvar_sala():
    if request.method == 'POST':
        tipo = request.form['tipo']
        capacidade = request.form['capacidade']
        descricao = request.form['descricao']
        
        # Salva sala na lista
        dados_reservas.salvar_sala(tipo, capacidade, descricao)

def salvar_reserva():
    if request.method == 'POST':
        sala = request.form['sala']
        inicio = request.form['inicio']
        final = request.form['final']
        
        # Salva reserva na lista
        dados_reservas.salvar_reserva(sala, inicio, final)
        
        return {
            'sala': sala,
            'inicio': inicio,
            'final': final
        }

# Funções de leitura e exibição dos dados
def ler_salas():
    return dados_reservas.retornar_salas()
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



