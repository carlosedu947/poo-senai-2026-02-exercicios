# Aula 07 · Exercício 01 (sala): as formas e a área polimórfica
#
# A classe Forma já está pronta: não mexa nela.
# Crie três filhas de Forma, cada uma com o seu __init__ e a sua area():
#   Retangulo(largura, altura)   area() RETORNA largura * altura
#   Circulo(raio)                area() RETORNA 3.14 * raio * raio
#   Triangulo(base, altura)      area() RETORNA base * altura / 2
# No __init__ de cada filha:
#   1. Se alguma medida for 0 ou negativa, raise ValueError("medida inválida").
#      Isso vem ANTES do super(): forma com medida errada nem começa a nascer.
#   2. Chame super().__init__("Retângulo") (ou "Círculo", ou "Triângulo") para
#      a Forma guardar o nome.
#   3. Guarde as medidas com self.
# O método tem que se chamar area(), sem nenhum parâmetro além do self:
# é isso que faz o for do teste funcionar sem nenhum if.
#
# SE TRAVAR, REVEJA:
#   sobrescrita no for ..... aula 07, slide 8  https://poo.leoad.com.br/aulas/aula-07/#s8
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   raise antes do super() . aula 06, slide 20  https://poo.leoad.com.br/aulas/aula-06/#s20
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13


class Forma:
    def __init__(self, nome):
        self.nome = nome

    def area(self):
        return 0

    def descricao(self):
        return f"{self.nome} com área {self.area()}"


class Retangulo(Forma):
    def __init__(self, largura, altura):
        if largura <= 0 or altura <= 0:
            raise ValueError("medida inválida")
        super().__init__("Retângulo")
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


class Circulo(Forma):
    def __init__(self, raio):
        if raio <= 0:
            raise ValueError("medida inválida")
        super().__init__("Círculo")
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio


class Triangulo(Forma):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("medida inválida")
        super().__init__("Triângulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


# ===== TESTE (não altere estas linhas) =====
formas = [Retangulo(4, 3), Circulo(5), Triangulo(6, 5), Retangulo(2, 2)]

print(formas[0].descricao())    # Retângulo com área 12
print(formas[1].descricao())    # Círculo com área 78.5
print(formas[2].descricao())    # Triângulo com área 15.0
print(formas[3].area())         # 4

total = 0
for f in formas:                # o mesmo for para todas as formas, sem if
    total = total + f.area()
print(total)                    # 109.5

recusadas = 0
try:
    Retangulo(0, 3)
except ValueError as erro:
    print("recusado:", erro)    # recusado: medida inválida
    recusadas = recusadas + 1
try:
    Retangulo(4, -1)
except ValueError:
    recusadas = recusadas + 1
try:
    Circulo(0)
except ValueError:
    recusadas = recusadas + 1
try:
    Triangulo(6, 0)
except ValueError:
    recusadas = recusadas + 1
print(recusadas)                # 4

print(f"chave: {formas[1].area()}-{formas[3].area()}-{total}-{len(formas[2].descricao())}-{Circulo(2).area()}-{Triangulo(4, 3).area()}-{recusadas}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA:
# Retângulo com área 12
# Círculo com área 78.5
# Triângulo com área 15.0
# 4
# 109.5
# recusado: medida inválida
# 4
# chave: 78.5-4-109.5-23-12.56-6.0-4