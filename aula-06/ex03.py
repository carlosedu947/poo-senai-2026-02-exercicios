# Aula 06 · Exercício 03 (sala): catálogo de filmes e séries
#
# Midia: o __init__ recebe titulo e minutos.
#   titulo     @property SÓ DE LEITURA (guarde em self._titulo): o título não muda.
#   minutos    @property e @minutos.setter. O setter RECUSA menos de 1 minuto:
#                  raise ValueError("minutos inválidos")
#              O __init__ faz self.minutos = minutos: o setter roda na criação.
#   duracao()  RETORNA os minutos.
#   __str__    retorna, por exemplo:  Duna (155 min)
#              (use self.duracao() no texto, não self.minutos)
#
# Filme é uma Midia e não muda nada: só herda.
#
# Serie é uma Midia com episódios (minutos é a duração de UM episódio):
#   o __init__ recebe titulo, minutos e episodios.
#     Se episodios for menor que 1, faça raise ValueError ANTES do super().
#     Depois, super().__init__ para titulo e minutos, e guarde os episodios.
#   duracao()  ESTENDE a do pai: a duração do pai vezes os episódios.
#   __str__    ESTENDE o do pai:  Dark (1560 min) em 26 episódios
#
# Função minutos_de_series(midias), fora das classes:
#   RETORNA a soma de duracao() só das mídias que são Serie (use isinstance).
#
# Minisserie é uma Serie (neta da Midia) e já vem pronta no arquivo: não mexa
# nela. Ela também conta como série na função.
#
# SE TRAVAR, REVEJA:
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25
#   raise antes do super() . aula 06, slide 20  https://poo.leoad.com.br/aulas/aula-06/#s20
#   isinstance ............. aula 06, slide 35  https://poo.leoad.com.br/aulas/aula-06/#s35
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25


class Midia:
    def __init__(self, titulo, minutos):
        self._titulo = titulo
        self.minutos = minutos          # passa pelo setter

    @property
    def titulo(self):
        return self._titulo             # sem setter: só leitura

    @property
    def minutos(self):
        return self._minutos

    @minutos.setter
    def minutos(self, valor):
        if valor < 1:
            raise ValueError("minutos inválidos")
        self._minutos = valor

    def duracao(self):
        return self.minutos

    def __str__(self):
        return f"{self.titulo} ({self.duracao()} min)"


class Filme(Midia):
    pass


class Serie(Midia):
    def __init__(self, titulo, minutos, episodios):
        if episodios < 1:
            raise ValueError("episódios inválidos")   # antes do super()
        super().__init__(titulo, minutos)
        self.episodios = episodios

    def duracao(self):
        return super().duracao() * self.episodios     # estende

    def __str__(self):
        return f"{super().__str__()} em {self.episodios} episódios"   # estende


def minutos_de_series(midias):
    total = 0
    for midia in midias:
        if isinstance(midia, Serie):
            total = total + midia.duracao()
    return total


class Minisserie(Serie):    # pronta: não mexa
    pass


# ===== TESTE (não altere estas linhas) =====
f = Filme("Duna", 155)
s1 = Serie("Dark", 60, 26)
s2 = Serie("Chernobyl", 65, 5)
s3 = Serie("Piloto", 50, 1)
m = Minisserie("Maid", 55, 10)
catalogo = [f, s1, s2, m]

print(f)                                 # Duna (155 min)
print(s1)                                # Dark (1560 min) em 26 episódios
print(s2.duracao())                      # 325
s3.minutos = 45
print(s3.duracao())                      # 45
print(m)                                 # Maid (550 min) em 10 episódios
print(minutos_de_series(catalogo))       # 2435
print(isinstance(m, Serie), isinstance(f, Serie), isinstance(s1, Filme))    # True False False

recusadas = 0
for episodios in [0, -1]:
    try:
        Serie("Vazia", 30, episodios)
    except ValueError:
        recusadas = recusadas + 1
try:
    Filme("Curta", 0)
except ValueError as erro:
    print("recusado:", erro)             # recusado: minutos inválidos
    recusadas = recusadas + 1
try:
    s2.minutos = -10
except ValueError:
    recusadas = recusadas + 1
try:
    f.titulo = "Duna 2"
except AttributeError:
    recusadas = recusadas + 1
print(recusadas, f, s2.duracao())        # 5 Duna (155 min) 325

print(f"chave: {s2.duracao()}-{minutos_de_series(catalogo)}-{s3.duracao()}-{len(str(s2))}-{isinstance(f, Midia)}-{isinstance(s1, Filme)}-{recusadas}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:Duna (155 min)
#Dark (1560 min) em 26 episódios
#325
#45
#Maid (550 min) em 10 episódios
#2435
#True False False
#recusado: minutos inválidos
#5 Duna (155 min) 325
#chave: 325-2435-45-34-True-False-5
