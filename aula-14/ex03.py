# Aula 14 · Exercício 03 (sala): buscar, atualizar e remover jogadoras
#
# A classe Jogadora e o começo do RepositorioJogadoras (__init__, salvar e
# listar) já estão prontos. Escreva os três métodos que faltam:
#   buscar(id)          SELECT ... WHERE id = ? com fetchone(). RETORNA a Jogadora
#                       (Jogadora.from_row), ou None se não existir esse id.
#   atualizar(jogadora) UPDATE jogadoras SET nome = ?, posicao = ?, gols = ?
#                       WHERE id = ?   com os dados e o id da jogadora.
#   remover(id)         DELETE ... WHERE id = ?. RETORNA True se apagou uma linha
#                       e False se não existia (cursor.rowcount diz quantas apagou).
# Cada método abre o banco com:  with sqlite3.connect(self.caminho) as conexao:
# Nenhum print dentro da classe.
#
# SE TRAVAR, REVEJA:
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   atualizar e remover .... aula 14, slide 26  https://poo.leoad.com.br/aulas/aula-14/#s26
#   sem WHERE .............. aula 14, slide 27  https://poo.leoad.com.br/aulas/aula-14/#s27
#   WHERE e fetchone ....... aula 14, slide 11  https://poo.leoad.com.br/aulas/aula-14/#s11
#   ? e não f-string ....... aula 14, slide 16  https://poo.leoad.com.br/aulas/aula-14/#s16

import sqlite3
from pathlib import Path


class Jogadora:
    def __init__(self, nome, posicao, gols, id=None):
        self.id = id
        self.nome = nome
        self.posicao = posicao
        self.gols = gols

    @classmethod
    def from_row(cls, linha):
        id, nome, posicao, gols = linha
        return cls(nome, posicao, gols, id)

    def to_params(self):
        return (self.nome, self.posicao, self.gols)

    def __repr__(self):
        return f"Jogadora('{self.nome}', '{self.posicao}', {self.gols}, {self.id})"


class RepositorioJogadoras:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS jogadoras (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    posicao TEXT NOT NULL,
                    gols INTEGER NOT NULL
                )
            """)

    def salvar(self, jogadora):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "INSERT INTO jogadoras (nome, posicao, gols) VALUES (?, ?, ?)",
                jogadora.to_params(),
            )
            jogadora.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, nome, posicao, gols FROM jogadoras ORDER BY id"
            ).fetchall()
        jogadoras = []
        for linha in linhas:
            jogadoras.append(Jogadora.from_row(linha))
        return jogadoras

    def buscar(self, id):
        with sqlite3.connect(self.caminho) as conexao:
            linha = conexao.execute(
                "SELECT id, nome, posicao, gols FROM jogadoras WHERE id = ?",
                (id,)
            ).fetchone()
        if linha is None:
            return None
        return Jogadora.from_row(linha)

    def atualizar(self, jogadora):
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute(
                "UPDATE jogadoras SET nome = ?, posicao = ?, gols = ? WHERE id = ?",
                (jogadora.nome, jogadora.posicao, jogadora.gols, jogadora.id)
            )

    def remover(self, id):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "DELETE FROM jogadoras WHERE id = ?",
                (id,)
            )
        return cursor.rowcount > 0

# ===== TESTE (não altere estas linhas) =====
BANCO = Path(__file__).parent / "ex03.db"

with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS jogadoras")    # começa do zero a cada execução

repo = RepositorioJogadoras(BANCO)
ana = Jogadora("Ana D'Ávila", "atacante", 2)
repo.salvar(ana)
repo.salvar(Jogadora("Bia", "goleira", 0))
repo.salvar(Jogadora("Duda", "meia", 1))

print(repo.buscar(2))          # Jogadora('Bia', 'goleira', 0, 2)
print(repo.buscar(9))          # None
# "ids" que tentam virar comando: com ? cada um é só um texto e não acha nada
truque1 = "9 OR 1=1"
truque2 = "9' OR '1'='1"
truque3 = '9" OR "1"="1'
print(repo.buscar(truque1))    # None
print(repo.buscar(truque2))    # None
print(repo.buscar(truque3))    # None

ana.gols = ana.gols + 3        # a Ana marcou mais 3
repo.atualizar(ana)
print(repo.buscar(1).gols)     # 5
print(repo.buscar(3).gols)     # 1

duda = repo.buscar(3)
duda.nome = 'Duda "Furacão"'   # um apelido com aspas duplas
repo.atualizar(duda)
print(repo.buscar(3).nome)     # Duda "Furacão"

print(repo.remover(truque1))   # False
print(repo.remover(truque2))   # False
print(repo.remover(truque3))   # False
saiu = repo.remover(2)         # a Bia sai do time
print(saiu)                    # True
de_novo = repo.remover(2)      # a Bia já não existe
print(de_novo)                 # False
print(repo.listar())           # [Jogadora('Ana D'Ávila', 'atacante', 5, 1), Jogadora('Duda "Furacão"', 'meia', 1, 3)]

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex03.py.
#    (O arquivo ex03.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA: Jogadora('Bia', 'goleira', 0, 2)
# None
# None
# None
# None
# 5
# 1
# Duda "Furacão"
# False
# False
# False
# True
# False
#[Jogadora('Ana D'Ávila', 'atacante', 5, 1), Jogadora('Duda "Furacão"', 'meia', 1, 3)]
