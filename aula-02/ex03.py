# Aula 02 · Exercício 03 (sala): a classe Jogo
#
# O _init_ recebe titulo, preco e plataforma e guarda os três.
# _str_   retorna, por exemplo:  Minecraft (PC) por R$ 99.90
#           (o preço sempre com 2 casas decimais: :.2f)
# _repr_  retorna, por exemplo:  Jogo('Minecraft', 99.9, 'PC')
#           (aspas simples em volta dos textos, o preço sem formatar)


class Jogo:
    def __init__(self, titulo, preco, plataforma):
        self.titulo = titulo
        self.preco = preco
        self.plataforma = plataforma

    def __str__(self):
        return f"{self.titulo} ({self.plataforma}) por R$ {self.preco:.2f}"

    def __repr__(self):
        return f"Jogo('{self.titulo}', {self.preco}, '{self.plataforma}')"


# ===== TESTE (não altere estas linhas) =====
j1 = Jogo("Minecraft", 99.9, "PC")
j2 = Jogo("FIFA", 250, "PS5")

print(j1)                   # Minecraft (PC) por R$ 99.90
print(f"Promoção: {j2}")    # Promoção: FIFA (PS5) por R$ 250.00
print(repr(j1))             # Jogo('Minecraft', 99.9, 'PC')
print([j1, j2])             # [Jogo('Minecraft', 99.9, 'PC'), Jogo('FIFA', 250, 'PS5')]

print(f"chave: {len(str(j1))}-{len(repr([j1, j2]))}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
#Minecraft (PC) por R$ 99.90
#Promoção: FIFA (PS5) por R$ 250.00
#Jogo('Minecraft', 99.9, 'PC')
#[Jogo('Minecraft', 99.9, 'PC'), Jogo('FIFA',250, 'PS5')]
#chave: 27-57