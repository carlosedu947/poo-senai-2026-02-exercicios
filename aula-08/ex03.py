# Aula 08 · Exercício 03 (sala): ingressos com property abstrata
#
# Crie a classe abstrata Ingresso (herda de ABC):
#   __init__(evento, preco_base) guarda o evento e faz self.preco_base = preco_base:
#              o setter roda na criação.
#   preco_base @property e @preco_base.setter. O setter RECUSA preço negativo:
#                  raise ValueError("preço não pode ser negativo")
#              e guarda em self._preco_base.
#   tipo       property ABSTRATA (texto).
#   desconto   property ABSTRATA (número de 0 a 1: 0.5 é metade).
#   preco      property CONCRETA: RETORNA preco_base * (1 - desconto).
#   __str__    retorna, por exemplo:  Show (meia): R$ 40.00
# Lembre: @property em cima, @abstractmethod embaixo, colado no def.
# Dentro da classe, property se usa sem parênteses: self.desconto.
#
# E as três filhas, com tipo e desconto como property:
# Inteira       tipo "inteira", desconto 0.
# Meia          tipo "meia", desconto 0.5.
# Promocional   o __init__ recebe evento, preco_base e percentual: chame
#               super().__init__(evento, preco_base) e guarde self.percentual.
#               tipo "promocional", desconto percentual / 100 (25 vira 0.25).
#
# SE TRAVAR, REVEJA:
#   property abstrata ...... aula 08, slide 21  https://poo.leoad.com.br/aulas/aula-08/#s21
#   ordem dos decoradores .. aula 08, slide 22  https://poo.leoad.com.br/aulas/aula-08/#s22
#   abstrato e concreto .... aula 08, slide 13  https://poo.leoad.com.br/aulas/aula-08/#s13
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

from abc import ABC, abstractmethod


class Ingresso(ABC):
    def __init__(self, evento, preco_base):
        self.evento = evento
        self.preco_base = preco_base

    @property
    def preco_base(self):
        return self._preco_base

    @preco_base.setter
    def preco_base(self, valor):
        if valor < 0:
            raise ValueError("preço não pode ser negativo")
        self._preco_base = valor

    @property
    @abstractmethod
    def tipo(self):
        pass

    @property
    @abstractmethod
    def desconto(self):
        pass

    @property
    def preco(self):
        return self.preco_base * (1 - self.desconto)

    def __str__(self):
        return f"{self.evento} ({self.tipo}): R$ {self.preco:.2f}"

        
class Inteira(Ingresso):
    @property
    def tipo(self):
        return "inteira"

    @property
    def desconto(self):
        return 0


class Meia(Ingresso):
    @property
    def tipo(self):
        return "meia"

    @property
    def desconto(self):
        return 0.5


class Promocional(Ingresso):
    def __init__(self, evento, preco_base, percentual):
        super().__init__(evento, preco_base)
        self.percentual = percentual
 
    @property
    def tipo(self):
        return "promocional"
 
    @property
    def desconto(self):
        return self.percentual / 100



# ===== TESTE (não altere estas linhas) =====
i = Inteira("Show", 80)
m = Meia("Show", 120)
p1 = Promocional("Show", 80, 25)
p2 = Promocional("Teatro", 50, 10)

print(i)                    # Show (inteira): R$ 80.00
print(m)                    # Show (meia): R$ 60.00
print(p1)                   # Show (promocional): R$ 60.00
print(m.preco + p2.preco)   # 105.0
print(Inteira("Cortesia", 0))    # Cortesia (inteira): R$ 0.00

try:
    Ingresso("Show", 80)
    base = "aceito"
except TypeError:
    base = "recusado"
print(base)                 # recusado


class SoTipo(Ingresso):     # filha de teste: só escreve o tipo
    @property
    def tipo(self):
        return "teste"


class SoDesconto(Ingresso):     # filha de teste: só escreve o desconto
    @property
    def desconto(self):
        return 0


try:
    SoTipo("Show", 80)
    so_tipo = "aceito"
except TypeError:
    so_tipo = "recusado"
print(so_tipo)              # recusado

try:
    SoDesconto("Show", 80)
    so_desconto = "aceito"
except TypeError:
    so_desconto = "recusado"
print(so_desconto)          # recusado

recusadas = 0
try:
    Inteira("Show", -10)
except ValueError as erro:
    print("recusado:", erro)    # recusado: preço não pode ser negativo
    recusadas = recusadas + 1
try:
    i.preco_base = -1
except ValueError:
    recusadas = recusadas + 1
print(recusadas, i.preco)   # 2 80

print(f"chave: {i.preco:.2f}-{m.desconto}-{p2.preco}-{base}-{so_tipo}-{so_desconto}-{len(str(i)) + len(str(m)) + len(str(p2))}-{recusadas}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-08. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
# Show (inteira): R$ 80.00
# Show (meia): R$ 60.00
# Show (promocional): R$ 60.00
# 105.0
# Cortesia (inteira): R$ 0.00
# recusado
# recusado
# recusado
# recusado: preço não pode ser negativo
# 2 80
# chave: 80.00-0.5-45.0-recusado-recusado-recusado-75-2
