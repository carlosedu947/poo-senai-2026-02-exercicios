# Aula 06 · Exercício 09 (grande): o estacionamento do shopping
#
# Um exercício maior, com tudo o que vimos das aulas 01 a 06. Faça por
# partes, na ordem, rodando a cada parte. O teste também está dividido por
# partes: quando ele parar com erro numa parte que você ainda não fez, é
# esperado. As linhas de cima continuam mostrando o que você já fez.
# Entrega até quinta, 29/10, às 18h35 (início da aula 07).
# Depois disso, não é aceito.
#
# PARTE 1 · A exceção e o veículo
#   EstacionamentoLotadoError: uma exceção própria (filha de Exception).
#   Veiculo tem dois atributos de classe:
#     tarifa_hora = 6.0    o preço da hora, igual para todo veículo
#     total = 0            conta quantos veículos foram criados
#   O __init__ recebe placa, modelo e horas, com horas = 1 como valor padrão.
#   O total só aumenta (pela classe: Veiculo.total) DEPOIS que tudo foi
#   guardado: veículo recusado não conta.
#
# PARTE 2 · As properties
#   placa  @property só de leitura (sem setter): o __init__ grava self._placa.
#   horas  @property e @horas.setter. O setter RECUSA menos de 1 hora:
#              raise ValueError("o mínimo é 1 hora")
#          O __init__ faz self.horas = horas: o setter roda na criação.
#
# PARTE 3 · Texto e construtor alternativo
#   valor()    RETORNA self.tarifa_hora vezes as horas.
#   __str__    RETORNA, por exemplo:  ABC1D23 Gol · 3h · R$ 18.00
#              (use self.valor() no texto, com :.2f)
#   __repr__   RETORNA, por exemplo:  Veiculo('UNO2E34', 'Uno', 1)
#   de_texto   @classmethod: recebe "HBV5F67;HB20;2" e RETORNA o veículo
#              (as horas viram int).
#
# PARTE 4 · As filhas
#   Moto é um Veiculo que SUBSTITUI o valor(): 3.0 por hora.
#   Caminhao é um Veiculo com eixos. O __init__ recebe placa, modelo, eixos
#   e horas (horas = 1 como padrão):
#     se eixos for menor que 2, raise ValueError("caminhão tem pelo menos 2 eixos")
#     ANTES do super(); depois, super().__init__ e guarde os eixos.
#   valor()    ESTENDE o do pai: o valor do pai vezes os eixos.
#   __str__    ESTENDE o do pai:  CAM9Z87 Scania · 2h · R$ 36.00 · 3 eixos
#
# PARTE 5 · O ticket e o estacionamento
#   Ticket guarda numero e veiculo (o veículo chega pronto).
#     __str__  RETORNA:  #1 ABC1D23 Gol · 3h · R$ 18.00
#   Estacionamento: o __init__ recebe nome e vagas (vagas = 3 como padrão)
#   e começa com a lista self.tickets vazia.
#     entrar(veiculo)  se já não houver vaga, raise EstacionamentoLotadoError
#                      com o texto "Shopping Flamboyant lotado" (o nome dele +
#                      " lotado"). Se houver, CRIA o Ticket (o número é a
#                      quantidade de tickets + 1), guarda na lista e RETORNA.
#
# PARTE 6 · As contas
#   faturamento()  RETORNA a soma do valor() de todos os veículos dos tickets.
#   motos()        RETORNA quantos veículos dos tickets são Moto (isinstance).
#
# PARTE 7 · O seu estacionamento (escreva você, embaixo do teste)
#   Crie um Estacionamento com o nome de um lugar real de Goiás que você
#   conhece (shopping, faculdade, hospital, feira...) e vagas à sua escolha.
#   Crie 3 veículos SEUS, todos com modelos reais e a cor no modelo:
#     um Veiculo, por exemplo  Veiculo("PQR4S56", "Onix prata", 2)
#     uma Moto e um Caminhao (com os eixos que quiser)
#   Invente as placas no formato novo: 3 letras, 1 número, 1 letra, 2 números.
#   Coloque os 3 no estacionamento com entrar() e mostre com print
#   cada ticket e o faturamento().
#
# SE TRAVAR, REVEJA:
#   exceção própria ........ aula 04, slide 34  https://poo.leoad.com.br/aulas/aula-04/#s34
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   contador ............... aula 05, slide 21  https://poo.leoad.com.br/aulas/aula-05/#s21
#   valor padrão ........... aula 05, slide 6  https://poo.leoad.com.br/aulas/aula-05/#s6
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   raise antes do super() . aula 06, slide 20  https://poo.leoad.com.br/aulas/aula-06/#s20
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25
#   composição ............. aula 05, slide 42  https://poo.leoad.com.br/aulas/aula-05/#s42
#   isinstance ............. aula 06, slide 35  https://poo.leoad.com.br/aulas/aula-06/#s35
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13


#PARTE 1 · A exceção e o veículo
class EstacionamentoLotadoError(Exception):
    pass


class Veiculo:
    tarifa_hora = 6.0
    total = 0

    def __init__(self, placa, modelo, horas=1):
        self._placa = placa
        self.modelo = modelo
        self.horas = horas          # o setter roda aqui
        Veiculo.total = Veiculo.total + 1

    #PARTE 2 · As properties
    @property
    def placa(self):
        return self._placa

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):
        if valor < 1:
            raise ValueError("o mínimo é 1 hora")
        self._horas = valor

    # PARTE 3 · Texto e construtor alternativo
    def valor(self):
        return self.tarifa_hora * self.horas

    def __str__(self):
        return f"{self.placa} {self.modelo} · {self.horas}h · R$ {self.valor():.2f}"

    def __repr__(self):
        return f"Veiculo({self.placa!r}, {self.modelo!r}, {self.horas})"

    @classmethod
    def de_texto(cls, texto):
        placa, modelo, horas = texto.split(";")
        return cls(placa, modelo, int(horas))


# PARTE 4 · As filhas
class Moto(Veiculo):
    def valor(self):
        return 3.0 * self.horas


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, eixos, horas=1):
        if eixos < 2:
            raise ValueError("caminhão tem pelo menos 2 eixos")
        super().__init__(placa, modelo, horas)
        self.eixos = eixos

    def valor(self):
        return super().valor() * self.eixos

    def __str__(self):
        return f"{super().__str__()} · {self.eixos} eixos"


# PARTE 5 · O ticket e o estacionamento
class Ticket:
    def __init__(self, numero, veiculo):
        self.numero = numero
        self.veiculo = veiculo

    def __str__(self):
        return f"#{self.numero} {self.veiculo}"


class Estacionamento:
    def __init__(self, nome, vagas=3):
        self.nome = nome
        self.vagas = vagas
        self.tickets = []

    def entrar(self, veiculo):
        if len(self.tickets) >= self.vagas:
            raise EstacionamentoLotadoError(f"{self.nome} lotado")
        ticket = Ticket(len(self.tickets) + 1, veiculo)
        self.tickets.append(ticket)
        return ticket

    # PARTE 6 · As contas
    def faturamento(self):
        return sum(t.veiculo.valor() for t in self.tickets)

    def motos(self):
        return sum(1 for t in self.tickets if isinstance(t.veiculo, Moto))


# ===== TESTE (não altere estas linhas) =====
# --- PARTES 1 a 3: o Veiculo ---
gol = Veiculo("ABC1D23", "Gol", 3)
uno = Veiculo("UNO2E34", "Uno")                      
hb20 = Veiculo.de_texto("HBV5F67;HB20;2")

print(gol)                       
print(repr(uno))                 
print(hb20.valor())
print(Veiculo.total)             

recusas = 0
for horas in [0, -2]:
    try:
        Veiculo("ERR0R00", "Teste", horas)
    except ValueError as erro:
        print("recusado:", erro)  
        recusas = recusas + 1
try:
    gol.horas = 0
except ValueError:
    recusas = recusas + 1
print(gol.horas, recusas)        

# --- PARTE 4: as filhas ---
moto = Moto("MOT0A12", "CG 160", 4)
scania = Caminhao("CAM9Z87", "Scania", 3, 2)

print(moto)                      
print(scania)                    
print(Veiculo.total)             
try:
    Caminhao("ERR0R01", "Teste", 1)
except ValueError as erro:
    print("recusado:", erro)      
    recusas = recusas + 1
print(recusas)                   
print(isinstance(scania, Veiculo), isinstance(gol, Caminhao))              

# --- PARTES 5 e 6: o estacionamento ---
shopping = Estacionamento("Shopping Flamboyant")     
print(shopping.entrar(gol))      
shopping.entrar(moto)
shopping.entrar(scania)
try:
    shopping.entrar(uno)
except EstacionamentoLotadoError as erro:
    print("barrado:", erro)       
print(len(shopping.tickets), shopping.faturamento(), shopping.motos())    

print(f"chave: {Veiculo.total}-{gol.horas}-{recusas}-{shopping.faturamento()}-{shopping.motos()}-{len(str(scania))}-{isinstance(gol, Caminhao)}")


# ===== PARTE 7: o seu estacionamento (escreva aqui embaixo) =====

estacionamento = Estacionamento("Goiânia Shopping", 5)

onix = Veiculo("PQR4S56", "Onix prata", 2)
biz = Moto("QWE7R89", "Honda Biz vermelha", 3)
volvo = Caminhao("RTY2U34", "Volvo FH azul", 3, 4)

print(estacionamento.entrar(onix))
print(estacionamento.entrar(biz))
print(estacionamento.entrar(volvo))
print(f"Faturamento: R$ {estacionamento.faturamento():.2f}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex09.py.
# ============================================================
# SAÍDA:
# ABC1D23 Gol · 3h · R$ 18.00
# Veiculo('UNO2E34', 'Uno', 1)
# 12.0
# 3
# recusado: o mínimo é 1 hora
# recusado: o mínimo é 1 hora
# 3 3
# MOT0A12 CG 160 · 4h · R$ 12.00
# CAM9Z87 Scania · 2h · R$ 36.00 · 3 eixos
# 5
# recusado: caminhão tem pelo menos 2 eixos
# 4
# True False
# #1 ABC1D23 Gol · 3h · R$ 18.00
# barrado: Shopping Flamboyant lotado
# 3 66.0 1
# chave: 5-3-4-66.0-1-40-False
# #1 PQR4S56 Onix prata · 2h · R$ 12.00
# #2 QWE7R89 Honda Biz vermelha · 3h · R$ 9.00
# #3 RTY2U34 Volvo FH azul · 4h · R$ 72.00 · 3 eixos
# Faturamento: R$ 93.00