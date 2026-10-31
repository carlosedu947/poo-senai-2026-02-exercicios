# Aula 08 · Exercício 02 (sala): as hospedagens da pousada
#
# A classe abstrata Hospedagem já está pronta: não mexa nela.
# Ela exige duas coisas de cada filha: diaria() e descricao().
# Rode do jeito que está e leia a mensagem do erro: ela diz o que falta.
#
# Escreva as três filhas, cada uma com diaria() e descricao(), que RETORNAM:
# Quarto   diária 150.   descricao: Quarto
# Suite    diária 250.   descricao: Suíte
# Chale    o __init__ recebe noites e pessoas. Se pessoas for menor que 1,
#          raise ValueError("pessoas inválidas") ANTES do super(). Depois,
#          chame super().__init__(noites) e guarde self.pessoas.
#          Até 2 pessoas, diária 200. Mais de 2 pessoas, diária 280.
#          descricao: Chalé para 4 (com o número de pessoas)
# Nenhum print dentro dos métodos.
#
# SE TRAVAR, REVEJA:
#   classe abstrata ........ aula 08, slide 8  https://poo.leoad.com.br/aulas/aula-08/#s8
#   abstrato e concreto .... aula 08, slide 13  https://poo.leoad.com.br/aulas/aula-08/#s13
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   raise antes do super() . aula 06, slide 20  https://poo.leoad.com.br/aulas/aula-06/#s20
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13

from abc import ABC, abstractmethod


class Hospedagem(ABC):
    def __init__(self, noites):
        self.noites = noites

    @abstractmethod
    def diaria(self):
        pass

    @abstractmethod
    def descricao(self):
        pass

    def total(self):
        return self.noites * self.diaria()

    def recibo(self):
        return f"{self.descricao()}, {self.noites} noite(s): R$ {self.total():.2f}"


class Quarto(Hospedagem):
    def diaria(self):
        return 150

    def descricao(self):
        return super().descricao()


class Suite(Hospedagem):
    def diaria(self):
        return 250

    def descricao(self):
        return super().descricao()


class Chale(Hospedagem):
    def __init__(self, noites, pessoas):
        if pessoas < 1:
            raise ValueError("pessoas inválidas")
        super().__init__(noites)
        self.pessoas = pessoas
 
    def diaria(self):
        if self.pessoas <= 2:
            return 200
        return 280
 
    def descricao(self):
        return f"Chalé para {self.pessoas}"



# ===== TESTE (não altere estas linhas) =====
quarto = Quarto(2)
suite = Suite(1)
chale2 = Chale(3, 2)
chale10 = Chale(3, 10)

print(quarto.recibo())    # Quarto, 2 noite(s): R$ 300.00
print(suite.recibo())     # Suíte, 1 noite(s): R$ 250.00
print(chale2.recibo())    # Chalé para 2, 3 noite(s): R$ 600.00
print(chale10.recibo())   # Chalé para 10, 3 noite(s): R$ 840.00

soma = 0
for h in [quarto, suite, chale2, chale10]:
    soma = soma + h.total()
print(soma)               # 1990
print(Chale(1, 1).recibo())    # Chalé para 1, 1 noite(s): R$ 200.00

try:
    Chale(2, 0)
    vazio = "aceito"
except ValueError as erro:
    print("recusado:", erro)    # recusado: pessoas inválidas
    vazio = "recusado"
print(vazio)              # recusado

print(f"chave: {quarto.diaria()}-{suite.total()}-{chale2.diaria()}-{chale10.total()}-{len(quarto.recibo() + suite.recibo() + chale2.recibo() + chale10.recibo())}-{vazio}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-08. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA: 
# Quarto, 2 noite(s): R$ 300.00
# Suíte, 1 noite(s): R$ 250.00
# Chalé para 2, 3 noite(s): R$ 600.00
# Chalé para 10, 3 noite(s): R$ 840.00
# 1990
# Chalé para 1, 1 noite(s): R$ 200.00
# recusado: pessoas inválidas
# recusado
# chave: 150-250-200-840-128-recusado
