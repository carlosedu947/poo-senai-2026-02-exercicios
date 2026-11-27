# Aula 15 · Exercício 01 (sala): os ingressos do cinema no banco
#
# As classes e quase todo o repositório já estão prontos. Falta o molde do
# tipo, para cada ingresso voltar da classe certa:
#
# 1. Em Inteira e em Meia, crie o atributo de classe tipo, com estes textos:
#    "inteira" e "meia". É o texto que vai para a coluna tipo.
# 2. Crie o dicionário TIPOS, que liga cada texto à sua classe.
# 3. Complete criar_ingresso(linha). A linha vem do banco assim:
#    (id, tipo, filme, valor_base). Pegue o tipo (linha[1]); se ele não
#    estiver no TIPOS, levante ValueError(f"tipo desconhecido: {tipo}");
#    senão, devolva o objeto montado pela classe certa, com from_row.
# 4. Escreva o método listar() do repositório: SELECT id, tipo, filme,
#    valor_base em ordem de id, e cada linha vira um objeto com criar_ingresso.
#
# SE TRAVAR, REVEJA:
#   o tipo em cada filha ... aula 15, slide 8  https://poo.leoad.com.br/aulas/aula-15/#s8
#   TIPOS e a fábrica ...... aula 15, slide 9  https://poo.leoad.com.br/aulas/aula-15/#s9
#   quem é o cls ........... aula 15, slide 11  https://poo.leoad.com.br/aulas/aula-15/#s11
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   comprehension .......... aula 10, slide 27  https://poo.leoad.com.br/aulas/aula-10/#s27
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18

import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path


class Ingresso(ABC):
    def __init__(self, filme, valor_base, id=None):
        self.id = id
        self.filme = filme
        self.valor_base = valor_base

    @abstractmethod
    def preco(self):
        pass

    def to_params(self):
        return (self.tipo, self.filme, self.valor_base)

    @classmethod
    def from_row(cls, linha):
        id, tipos, filme, valor_base = linha
        return cls(filme, valor_base, id)

    def __repr__(self):
        return f"#{self.id} {self.filme} ({self.tipos})"


class Inteira(Ingresso):
    tipos = "inteira"

    def preco(self):
        return self.valor_base


class Meia(Ingresso):
    tipos = "meia"

    def preco(self):
        return self.valor_base / 2

TIPOS = {"inteira": Inteira, "meia": Meia}


def criar_ingresso(linha, TIPOS):
    tipo = linha[1]
    if tipo not in TIPOS:
        raise ValueError(f"tipo desconhecido: {tipo}")
    return TIPOS[tipo].from_row(linha)

def listar(self):
    with sqlite3.connect(self.caminho) as conexao:
        linhas = conexao.execute(
            "SELECT id, tipo, filme, valor_base FROM ingressos ORDER BY id"
        ).fetchall(),
    return [criar_ingresso(linha, TIPOS) for linha in linhas]

class RepositorioIngressos:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS ingressos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    filme TEXT NOT NULL,
                    valor_base REAL NOT NULL
                )
            """)

    def salvar(self, ingresso):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "INSERT INTO ingressos (tipo, filme, valor_base) VALUES (?, ?, ?)",
                ingresso.to_params()
            )
            ingresso.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, tipo, filme, valor_base FROM ingressos ORDER BY id"
            ).fetchall()
        return [criar_ingresso(linha, TIPOS) for linha in linhas]


# ===== TESTE (não altere estas linhas) =====
BANCO = Path(__file__).parent / "ex01.db"
with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS ingressos")    # começa do zero a cada execução

repo = RepositorioIngressos(BANCO)
repo.salvar(Inteira("Divertida Mente", 30))
repo.salvar(Meia("Divertida Mente", 30))
repo.salvar(Meia("Duna", 35))

outro = RepositorioIngressos(BANCO)    # como se o programa fechasse e abrisse de novo
lista = outro.listar()
print(lista)    # [#1 Divertida Mente (inteira), #2 Divertida Mente (meia), #3 Duna (meia)]
print(lista[2].preco(), lista[0].preco())    # 17.5 30.0
print(TIPOS["meia"])                          # <class '__main__.Meia'>

mensagem = "nenhum erro"
try:
    criar_ingresso((9, "cortesia", "Duna", 35))
except ValueError as erro:
    mensagem = str(erro)
print("Erro:", mensagem)    # Erro: tipo desconhecido: cortesia


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-15. O nome tem que ser ex01.py.
#    (O arquivo ex01.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
