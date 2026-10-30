# Aula 07 · Exercício 02 (sala): formas de pagamento com duck typing
#
# Crie três classes SEM herança (nenhuma é filha de outra):
#   Pix()              descricao()  RETORNA "Pix"
#                      taxa(valor)  RETORNA 0
#   Cartao(parcelas)   descricao()  RETORNA, por exemplo, "Cartão 3x"
#                      taxa(valor)  RETORNA 1% do valor por parcela: valor * parcelas / 100
#   Boleto()           descricao()  RETORNA "Boleto"
#                      taxa(valor)  RETORNA 3.5 (a mesma, qualquer que seja o valor)
# As três têm os MESMOS métodos, com os MESMOS parâmetros: descricao() só com
# o self, e taxa(self, valor). As parcelas são só do cartão: chegam no __init__.
# A função total_a_pagar, no teste, não sabe qual forma recebeu e não tem if.
#
# No Cartao, parcelas é protegida:
#   parcelas   @property e @parcelas.setter. O setter RECUSA menos de 1 ou
#              mais de 12 parcelas:  raise ValueError("parcelas de 1 a 12")
#              O __init__ faz self.parcelas = parcelas: o setter roda na criação.
#
# SE TRAVAR, REVEJA:
#   duck typing ............ aula 07, slide 13  https://poo.leoad.com.br/aulas/aula-07/#s13
#   assinatura ............. aula 07, slide 19  https://poo.leoad.com.br/aulas/aula-07/#s19
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13


class Pix:
    def descricao(self):
        return "Pix"

    def taxa(self, valor):
        return 0


class Cartao:
    def __init__(self, parcelas):
        self.parcelas = parcelas  

    @property
    def parcelas(self):
        return self._parcelas

    @parcelas.setter
    def parcelas(self, valor):
        if valor < 1 or valor > 12:
            raise ValueError("parcelas de 1 a 12")
        self._parcelas = valor

    def descricao(self):
        return f"Cartão {self.parcelas}x"

    def taxa(self, valor):
        return valor * self.parcelas / 100


class Boleto:
    def descricao(self):
        return "Boleto"

    def taxa(self, valor):
        return 3.5


# ===== TESTE (não altere estas linhas) =====
def total_a_pagar(forma, valor):
    return valor + forma.taxa(valor)

formas = [Pix(), Cartao(3), Boleto(), Cartao(12)]

print(formas[0].descricao(), total_a_pagar(formas[0], 200))    # Pix 200
print(formas[1].descricao(), total_a_pagar(formas[1], 200))    # Cartão 3x 206.0
print(formas[2].descricao(), total_a_pagar(formas[2], 200))    # Boleto 203.5
print(formas[3].descricao(), formas[3].taxa(50))               # Cartão 12x 6.0

soma_taxas = 0
for f in formas:                # o mesmo for para todas as formas, sem if
    soma_taxas = soma_taxas + f.taxa(100)
print(soma_taxas)               # 18.5

cartao = Cartao(2)
cartao.parcelas = 6
print(cartao.descricao(), cartao.taxa(100))    # Cartão 6x 6.0

recusadas = 0
for parcelas in [0, 13]:
    try:
        Cartao(parcelas)
    except ValueError as erro:
        print("recusado:", erro)    # recusado: parcelas de 1 a 12
        recusadas = recusadas + 1
try:
    cartao.parcelas = -2
except ValueError:
    recusadas = recusadas + 1
print(recusadas, cartao.parcelas)   # 3 6

print(f"chave: {formas[1].taxa(500)}-{total_a_pagar(Boleto(), 10)}-{soma_taxas}-{len(formas[3].descricao())}-{formas[0].descricao()}{formas[2].descricao()}-{cartao.taxa(100)}-{recusadas}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:
# Pix 200
# Cartão 3x 206.0
# Boleto 203.5
# Cartão 12x 6.0
# 18.5
# Cartão 6x 6.0
# recusado: parcelas de 1 a 12
# recusado: parcelas de 1 a 12
# 3 6
# chave: 15.0-13.5-18.5-10-PixBoleto-6.0-3