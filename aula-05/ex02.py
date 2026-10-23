# Aula 05 · Exercício 02 (sala): a classe Ingresso
#
# Crie a classe Ingresso com dois atributos de CLASSE:
#   taxa = 4        a taxa de serviço, a mesma para todos os ingressos
#   vendidos = 0    quantos ingressos já foram criados
# O __init__ recebe filme e preco, guarda os dois e soma 1 em vendidos.
#   Some pela classe (Ingresso.vendidos), não pelo self, e DEPOIS de guardar
#   o preço: ingresso recusado não conta.
# preco            @property e @preco.setter. O setter RECUSA preço negativo:
#                      raise ValueError("preço não pode ser negativo")
#                  O __init__ faz self.preco = preco: o setter roda na criação.
# total()          RETORNA o preço mais a taxa.
# de_texto(texto)  construtor alternativo, com @classmethod. Recebe um texto
#                  como "Wicked;25", corta no ; com split e RETORNA
#                  cls(filme, preco), com o preço convertido por int().
# __str__          RETORNA, por exemplo:  Coringa: R$ 26.00
#                  (o total, com :.2f)
#
# SE TRAVAR, REVEJA:
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   contador ............... aula 05, slide 21  https://poo.leoad.com.br/aulas/aula-05/#s21
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class Ingresso:
    taxa = 4
    vendidos = 0

    def __init__(self, filme, preco):
        self.filme = filme
        self.preco = preco          # o setter roda aqui e pode recusar
        Ingresso.vendidos += 1      # só chega aqui se o preço foi aceito

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("preço não pode ser negativo")
        self._preco = valor

    def total(self):
        return self.preco + self.taxa

    @classmethod
    def de_texto(cls, texto):
        filme, preco = texto.split(";")
        return cls(filme, int(preco))

    def __str__(self):
        return f"{self.filme}: R$ {self.total():.2f}"
    
# ===== TESTE (não altere estas linhas) =====
i1 = Ingresso("Duna", 30)
i2 = Ingresso.de_texto("Wicked;25")

print(i2.filme, i2.preco)          # Wicked 25
print(i1.total(), i2.total())      # 34 29
print(Ingresso.vendidos)           # 2

Ingresso.taxa = 6
i3 = Ingresso.de_texto("Coringa;20")
print(i1.total(), i3.total())      # 36 26
print(Ingresso.vendidos)           # 3
print(i3)                          # Coringa: R$ 26.00

try:
    Ingresso("Teste", -5)
except ValueError as erro:
    print("recusado:", erro)       # recusado: preço não pode ser negativo
print(Ingresso.vendidos)           # 3

print(f"chave: {i2.preco + i3.preco}-{i1.total()}-{i3.total()}-{Ingresso.vendidos}-{i1.vendidos}-{len(str(i3))}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:Wicked 25
#34 29
#2
#36 26
#3
#Coringa: R$ 26.00
#recusado: preço não pode ser negativo
#3
#chave: 45-36-26-3-3-17
