# Aula 02 · Exercício 01 (sala): a classe Livro
#
# Crie a classe Livro.
# O _init_ recebe titulo, autor e paginas, nessa ordem, e guarda os três
# como atributos (self.titulo, self.autor, self.paginas).
# Todo livro nasce sem ter sido lido: self.lido = False.
# Nada de valor fixo no lugar dos parâmetros.


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.lido = False

# ===== TESTE (não altere estas linhas) =====
l1 = Livro("Dom Casmurro", "Machado de Assis", 256)
l2 = Livro("Laços de Família", "Clarice Lispector", 160)

print(l1.titulo, l1.paginas)     # Dom Casmurro 256
print(l2.titulo, l2.paginas)     # Laços de Família 160
print(l1.autor == l2.autor)      # False

l2.lido = True
print(l1.lido, l2.lido)          # False True

print(f"chave: {len(l2.titulo)}-{l1.paginas + l2.paginas}-{l1.lido}-{len(l2.autor)}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA:
#Dom Casmurro 256
#Laços de Família 160
#False
#False True
#chave: 16-416-False-17