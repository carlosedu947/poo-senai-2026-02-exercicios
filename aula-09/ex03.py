# Aula 09 · Exercício 03 (sala): formas de pagamento
#
# Escreva as classes do diagrama (está no slide e neste endereço):
#   https://poo.leoad.com.br/images/aula-09/ex03-pagamento.svg
# Pagamento é abstrata («abstract», nome em itálico): herda de ABC.
#   taxa()      em itálico: método ABSTRATO.
#   total()     RETORNA o valor mais a taxa().
#   __str__     RETORNA, por exemplo:  R$ 150.00   (o total, com :.2f)
# Pix           taxa() RETORNA 0.
# Cartao        tem parcelas: o __init__ recebe valor e parcelas, chama
#               super().__init__(valor) e guarda as parcelas.
#   taxa()      RETORNA 2% do valor por parcela:  valor * 2 / 100 * parcelas
#   __str__     ESTENDE o do pai:  R$ 212.00 em 3x
#
# Função soma_totais(pagamentos), fora das classes: RETORNA a soma do
# total() de cada pagamento da lista.
#
# SE TRAVAR, REVEJA:
#   o triângulo ............ aula 09, slide 21  https://poo.leoad.com.br/aulas/aula-09/#s21
#   «abstract» ............. aula 09, slide 27  https://poo.leoad.com.br/aulas/aula-09/#s27
#   classe abstrata ........ aula 08, slide 8  https://poo.leoad.com.br/aulas/aula-08/#s8
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25


from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def taxa(self):
        pass

    def total(self):
        return self.valor + self.taxa()

    def __str__(self):
        return f"R$ {self.total():.2f}"


class Pix(Pagamento):
    def taxa(self):
        return 0


class Cartao(Pagamento):
    def __init__(self, valor, parcelas):
        super().__init__(valor)
        self.parcelas = parcelas

    def taxa(self):
        return self.valor * 2 / 100 * self.parcelas

    def __str__(self):
        return f"{super().__str__()} em {self.parcelas}x"


def soma_totais(pagamentos):
    soma = 0
    for pagamento in pagamentos:
        soma += pagamento.total()
    return soma

# ===== TESTE (não altere estas linhas) =====
pix = Pix(150)
cartao = Cartao(200, 3)

print(pix)                              # R$ 150.00
print(cartao)                           # R$ 212.00 em 3x
print(cartao.taxa())                    # 12.0
print(soma_totais([pix, cartao]))       # 362.0
print(isinstance(cartao, Pagamento))    # True

recusado = 0
try:
    Pagamento(100)
except TypeError:
    recusado = recusado + 1
print(recusado)                         # 1

print(f"chave: {pix.total()}-{cartao.total()}-{soma_totais([pix, cartao])}-{len(str(cartao))}-{recusado}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
