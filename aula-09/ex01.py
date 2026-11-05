# Aula 09 · Exercício 01 (sala): a pizzaria
#
# Escreva a classe Pizza do diagrama (está no slide e neste endereço):
#   https://poo.leoad.com.br/images/aula-09/ex01-pizza.svg
# O diagrama diz O QUE existe. As regras abaixo dizem COMO funciona.
#
# taxa_entrega e total   sublinhados: atributos de classe. O total conta as
#                        pizzas criadas: some 1 no __init__, pela classe.
# _preco e preco         o __init__ grava self._preco; preco é uma @property
#                        só de leitura (sem setter).
# de_texto               sublinhado: @classmethod. Recebe um texto como
#                        "Frango com catupiry;M;42" (o preço vira float).
# com_entrega()          RETORNA o preço mais a taxa_entrega.
# __str__                RETORNA, por exemplo:  Pizza Calabresa (G): R$ 54.90
# __repr__               RETORNA, por exemplo:  Pizza('Frango com catupiry', 'M', 42.0)
#
# SE TRAVAR, REVEJA:
#   a caixa da classe ...... aula 09, slide 8  https://poo.leoad.com.br/aulas/aula-09/#s8
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27


class Pizza:
   taxa_entrega = 8.0
   total = 0

   def __init__ (self,sabor,tamanho, preco):
       self.sabor = sabor
       self.tamanho = tamanho
       self.preco = preco
       Pizza.total + 1

@property
def preco(self):
    return self._preco

@classmethod
def de_texto(cls, texto):
        sabor, tamanho, preco = texto.split(";")
        return cls(sabor, tamanho, float(preco))

def com_entrega(self):
        return self._preco + Pizza.taxa_entrega

def __str__(self):
        return f"Pizza {self.sabor} ({self.tamanho}): R$ {self._preco:.2f}"

def __repr__(self):
        return f"Pizza({self.sabor!r}, {self.tamanho!r}, {self._preco!r})"

# ===== TESTE (não altere estas linhas) =====
calabresa = Pizza("Calabresa", "G", 54.9)
frango = Pizza.de_texto("Frango com catupiry;M;42")

print(calabresa)                 # Pizza Calabresa (G): R$ 54.90
print(repr(frango))              # Pizza('Frango com catupiry', 'M', 42.0)
print(frango.com_entrega())      # 50.0
print(calabresa.preco)           # 54.9
print(Pizza.total)               # 2

try:
    calabresa.preco = 10
    print("mudou o preço")
except AttributeError:
    print("preço só de leitura")  # preço só de leitura

print(f"chave: {Pizza.total}-{frango.com_entrega()}-{len(str(calabresa))}-{len(repr(frango))}-{calabresa.preco}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA:
