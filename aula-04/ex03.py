# Aula 04 · Exercício 03 (sala): o Produto completo
#
# Uma classe pequena com tudo o que vimos até aqui.
#
# nome      @property só de leitura (sem setter). O __init__ já grava
#           direto em self._nome.
# preco     @property e @preco.setter. O setter RECUSA preço negativo:
#               raise ValueError("preço não pode ser negativo")
#           e só guarda em self._preco depois de validar. 0 vale (brinde).
#           O __init__ já faz self.preco = preco: o setter roda na criação.
# __str__   RETORNA, por exemplo:  Café · R$ 12.50   (o preço com :.2f)
# __repr__  RETORNA, por exemplo:  Produto('Café', 12.5)
#           (aspas simples em volta do nome; o preço sem formatar)
#
# SE TRAVAR, REVEJA:
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   setter ................. aula 03, slide 18  https://poo.leoad.com.br/aulas/aula-03/#s18
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27


class Produto:
    def __init__(self, nome, preco):
        self._nome = nome     # só de leitura: direto na gaveta
        self.preco = preco    # tem setter: passa por ele

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("preço não pode ser negativo")
        self._preco = valor

    def __str__(self):
        return f"{self._nome} . R$ {self.preco:.2F}"

    def __repr__(self):
        return f"Produto('{self._nome}', {self.preco})"


# ===== TESTE (não altere estas linhas) =====
cafe = Produto("Café", 12.5)
print(cafe)                 # Café · R$ 12.50
print(repr(cafe))           # Produto('Café', 12.5)
print(cafe.nome)            # Café

cafe.preco = 14
print(cafe)                 # Café · R$ 14.00

try:
    cafe.preco = -3
except ValueError as erro:
    print("recusado:", erro)    # recusado: preço não pode ser negativo
print(cafe.preco)               # 14

so_leitura = "não"
try:
    cafe.nome = "Chá"
except AttributeError:
    so_leitura = "sim"
print(so_leitura)               # sim

criados = 0
recusados = 0
for preco in [5, -1, 0]:
    try:
        Produto("Bala", preco)
        criados = criados + 1
    except ValueError:
        recusados = recusados + 1
print(criados, recusados)       # 2 1

lista = [Produto("Pão", 0.75), Produto("Leite", 6)]
print(lista)                    # [Produto('Pão', 0.75), Produto('Leite', 6)]

print(f"chave: {len(str(cafe))}-{len(repr(lista[0]))}-{cafe.preco}-{so_leitura}-{criados}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-04. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
# 
# Café . R$ 12.50
# Produto('Café', 12.5)
# Café
# Café . R$ 14.00
# recusado: preço não pode ser negativo
# 14
# sim
# 2 1
# [Produto('Pão', 0.75), Produto('Leite', 6)]
# chave: 15-20-14-sim-2