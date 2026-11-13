# Aula 12 · Exercício 01 (sala): a lista de filmes em texto
#
# Filme: o __init__ recebe titulo, ano e nota e guarda os três.
#   para_linha()      RETORNA o filme como uma linha de texto, com ; entre os
#                     campos e o \n no fim. Exemplo:  Matrix;1999;8.7\n
#   de_linha(linha)   construtor alternativo (@classmethod): recebe uma linha
#                     como a do para_linha() e RETORNA cls(...). O ano volta
#                     como int e a nota como float.
#   __repr__          retorna, por exemplo:  Filme('Matrix', 1999, 8.7)
#
# salvar(filmes, caminho): abre o arquivo em "w" UMA vez (encoding="utf-8")
#   e escreve o para_linha() de cada filme.
# carregar(caminho): lê o arquivo linha por linha e RETORNA a lista de Filme
#   (use Filme.de_linha). Pule as linhas em branco.
# Nenhum print dentro da classe nem das funções.
#
# SE TRAVAR, REVEJA:
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   tudo é texto ........... aula 12, slide 5  https://poo.leoad.com.br/aulas/aula-12/#s5
#   de_linha e para_linha .. aula 12, slide 6  https://poo.leoad.com.br/aulas/aula-12/#s6
#   gravar a lista ......... aula 12, slide 7  https://poo.leoad.com.br/aulas/aula-12/#s7
#   ler a lista ............ aula 12, slide 8  https://poo.leoad.com.br/aulas/aula-12/#s8
#   linha em branco ........ aula 12, slide 12  https://poo.leoad.com.br/aulas/aula-12/#s12
 
from pathlib import Path
 
 
class Filme:
    def __init__(self, titulo, ano, nota):
        self.titulo = titulo
        self.ano = ano
        self.nota = nota
 
    def para_linha(self):
        return f"{self.titulo};{self.ano};{self.nota}\n"
 
    @classmethod
    def de_linha(cls, linha):
        titulo, ano, nota = linha.strip().split(";")
        return cls(titulo, int(ano), float(nota))
 
    def __repr__(self):
        return f"Filme({self.titulo!r}, {self.ano}, {self.nota})"
 
 
def salvar(filmes, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for filme in filmes:
            arquivo.write(filme.para_linha())
 
 
def carregar(caminho):
    filmes = []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.strip() == "":
                continue
            filmes.append(Filme.de_linha(linha))
    return filmes
 
 
# ===== TESTE (não altere estas linhas) =====
PASTA = Path(__file__).parent
 
filmes = [Filme("Matrix", 1999, 8.7), Filme("Central do Brasil", 1998, 8.0), Filme("Up", 2009, 8.3)]
salvar(filmes, PASTA / "filmes.txt")
 
with open(PASTA / "filmes.txt", "a", encoding="utf-8") as arquivo:    # alguém mexeu no arquivo:
    arquivo.write("\n")                                               # uma linha em branco
    arquivo.write("Bacurau;2019;7.4\n")                               # e um filme novo
 
de_volta = carregar(PASTA / "filmes.txt")
print(de_volta[1])                      # Filme('Central do Brasil', 1998, 8.0)
print(len(de_volta))                    # 4
 
mais_novo = de_volta[0]
for filme in de_volta:
    if filme.ano > mais_novo.ano:
        mais_novo = filme
print(mais_novo.titulo)                 # Bacurau
 
print(2026 - de_volta[1].ano)               # 28
print(de_volta[0].nota + de_volta[2].nota)  # 17.0
 
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-12. O nome tem que ser ex01.py.
#    (O arquivo filmes.txt que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
# Filme('Central do Brasil', 1998, 8.0)
# 4
# Bacurau
# 28
# 17.0
