# Aula 08 · Exercício 04 (casa, OBRIGATÓRIO): veículos no pedágio
#
# Crie a classe abstrata Veiculo (herda de ABC):
#   __init__(placa)   guarda a placa em self._placa.
#   placa             @property SÓ DE LEITURA: a placa não muda.
#   tarifa()          método ABSTRATO.
#   recibo()          método concreto: RETORNA, por exemplo:  ABC1D23: R$ 7.50
#                     (use self.tarifa() e :.2f)
#
# E as três filhas, cada uma com tarifa() que RETORNA:
# Carro      7.5
# Moto       3.75
# Caminhao   o __init__ recebe placa e eixos. Se eixos for menor que 2,
#            raise ValueError("caminhão tem pelo menos 2 eixos") ANTES do
#            super(). Depois, chame super().__init__(placa) e guarde self.eixos.
#            Tarifa: 7.5 vezes o número de eixos.
#
# Exemplos:
#   Carro("ABC1D23").recibo()        ABC1D23: R$ 7.50
#   Moto("MOT4E56").recibo()         MOT4E56: R$ 3.75
#   Caminhao("CAM7F89", 3).recibo()  CAM7F89: R$ 22.50
#
# Por fim, mostre que o Veiculo genérico é recusado: dentro de um
# try/except TypeError, tente criar Veiculo("XYZ0A00") e, no except,
# imprima Veiculo recusado. Mostre também, com try/except, que
# Caminhao("CAM0A01", 1) é recusado e que carro.placa = "XXX0X00" dá
# AttributeError.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   classe abstrata ........ aula 08, slide 8  https://poo.leoad.com.br/aulas/aula-08/#s8
#   abstrato e concreto .... aula 08, slide 13  https://poo.leoad.com.br/aulas/aula-08/#s13
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   raise antes do super() . aula 06, slide 20  https://poo.leoad.com.br/aulas/aula-06/#s20
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
 
from abc import ABC, abstractmethod
 
 
class Veiculo(ABC):
    def __init__(self, placa):
        self._placa = placa
 
    @property
    def placa(self):
        return self._placa
 
    @abstractmethod
    def tarifa(self):
        pass
 
    def recibo(self):
        return f"{self.placa}: R$ {self.tarifa():.2f}"
 
 
class Carro(Veiculo):
    def tarifa(self):
        return 7.5
 
 
class Moto(Veiculo):
    def tarifa(self):
        return 3.75
 
 
class Caminhao(Veiculo):
    def __init__(self, placa, eixos):
        if eixos < 2:
            raise ValueError("caminhão tem pelo menos 2 eixos")
        super().__init__(placa)
        self.eixos = eixos
 
    def tarifa(self):
        return 7.5 * self.eixos
 
 
# ===== TESTE =====
carro = Carro("ABC1D23")
moto = Moto("MOT4E56")
caminhao = Caminhao("CAM7F89", 3)
 
print(carro.recibo())       # ABC1D23: R$ 7.50
print(moto.recibo())        # MOT4E56: R$ 3.75
print(caminhao.recibo())    # CAM7F89: R$ 22.50
 
try:
    Veiculo("XYZ0A00")
except TypeError:
    print("Veiculo recusado")
 
try:
    Caminhao("CAM0A01", 1)
except ValueError as erro:
    print("Caminhao recusado:", erro)
 
try:
    carro.placa = "XXX0X00"
except AttributeError:
    print("placa protegida:", carro.placa)
 
 
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-08. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:
# ABC1D23: R$ 7.50
# MOT4E56: R$ 3.75
# CAM7F89: R$ 22.50
# Veiculo recusado
# Caminhao recusado: caminhão tem pelo menos 2 eixos
# placa protegida: ABC1D23
