# Aula 13 · Exercício 04 (casa, OBRIGATÓRIO): a corrida e as tarifas
#
# Comece o arquivo com:  from abc import ABC, abstractmethod
#
# Tarifa: classe abstrata (ABC) com o método abstrato calcular(km).
#   Comum      calcular(km) RETORNA 5 + 2 * km
#   Noturna    o __init__ recebe adicional (em %).
#              calcular(km) RETORNA (5 + 2 * km) * (1 + self.adicional / 100)
#   Fixa       o __init__ recebe valor. calcular(km) RETORNA sempre esse valor.
#
# Corrida: o __init__ recebe passageiro, km e tarifa (um OBJETO Tarifa) e guarda os três.
#   valor()    RETORNA o valor da corrida, delegando para self.tarifa.calcular(...).
#   __str__    retorna, por exemplo:  Ana: 10 km por R$ 25.00
#
# Exemplos:
#   Corrida("Ana", 10, Comum())        Ana: 10 km por R$ 25.00
#   a mesma corrida, depois de trocar a tarifa por Noturna(20):
#                                      Ana: 10 km por R$ 30.00
#   Corrida("Caio", 3, Fixa(15))       Caio: 3 km por R$ 15.00
#   Tarifa() dá TypeError: a classe abstrata não cria objeto.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   classe abstrata ........ aula 08, slide 8  https://poo.leoad.com.br/aulas/aula-08/#s8
#   Strategy com classe .... aula 13, slide 18  https://poo.leoad.com.br/aulas/aula-13/#s18
#   delegar ................ aula 13, slide 19  https://poo.leoad.com.br/aulas/aula-13/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25


from abc import ABC, abstractmethod
 
 
class Tarifa(ABC):
    @abstractmethod
    def calcular(self, km):
        pass
 
 
class Comum(Tarifa):
    def calcular(self, km):
        return 5 + 2 * km
 
 
class Noturna(Tarifa):
    def __init__(self, adicional):
        self.adicional = adicional
 
    def calcular(self, km):
        return (5 + 2 * km) * (1 + self.adicional / 100)
 
 
class Fixa(Tarifa):
    def __init__(self, valor):
        self.valor = valor
 
    def calcular(self, km):
        return self.valor
 
 
class Corrida:
    def __init__(self, passageiro, km, tarifa):
        self.passageiro = passageiro
        self.km = km
        self.tarifa = tarifa
 
    def valor(self):
        return self.tarifa.calcular(self.km)
 
    def __str__(self):
        return f"{self.passageiro}: {self.km} km por R$ {self.valor():.2f}"
 
 
# ----- Teste -----
corrida = Corrida("Ana", 10, Comum())
print(corrida)
 
corrida.tarifa = Noturna(20)
print(corrida)
 
print(Corrida("Caio", 3, Fixa(15)))
 
try:
    Tarifa()
except TypeError as erro:
    print("TypeError:", erro)


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA: Ana: 10 km por R$ 25.00
# Ana: 10 km por R$ 30.00
# Caio: 3 km por R$ 15.00
# TypeError: Can't instantiate abstract class Tarifa without an implementation for abstract method 'calcular'
