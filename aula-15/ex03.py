# Aula 15 · Exercício 03 (sala): a biblioteca, com a revista que tem edição
#
# Item (abstrata) e Livro já estão prontos. A Revista é um Item que tem também
# o número da edição. Escreva:
#
# 1. A classe Revista: tipo "revista", recebe titulo, edicao e id=None
#    (use o super().__init__), prazo_dias() RETORNA 7. Como só ela tem
#    edicao, ela sobrescreve to_params() e from_row() para levar e trazer
#    a coluna edicao.
# 2. O dicionário TIPOS e a função criar_item(linha), com o mesmo
#    ValueError de tipo desconhecido do exercício 01.
# 3. No repositório: o CREATE TABLE IF NOT EXISTS itens no __init__, com as
#    colunas id (gerado pelo banco), tipo e titulo (textos que todo item
#    tem) e edicao (número que só a revista tem: pense no NOT NULL);
#    salvar(item), que guarda o id gerado; e buscar_por_id(id), que RETORNA
#    o item da classe certa, ou None se não existir.
# A linha de um item vem do banco assim: (id, tipo, titulo, edicao).
#
# SE TRAVAR, REVEJA:
#   filha com coluna a mais . aula 15, slide 33  https://poo.leoad.com.br/aulas/aula-15/#s33
#   a hierarquia na tabela . aula 15, slide 32  https://poo.leoad.com.br/aulas/aula-15/#s32
#   TIPOS e a fábrica ...... aula 15, slide 9  https://poo.leoad.com.br/aulas/aula-15/#s9
#   o repositório com tipo . aula 15, slide 14  https://poo.leoad.com.br/aulas/aula-15/#s14
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   __init__ e salvar ...... aula 14, slide 24  https://poo.leoad.com.br/aulas/aula-14/#s24
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25

import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path


class Item(ABC):
    def __init__(self, titulo, id=None):
        self.id = id
        self.titulo = titulo

    @abstractmethod
    def prazo_dias(self):
        pass

    def to_params(self):
        return (self.tipo, self.titulo, None)    # quem não tem edição grava NULL

    @classmethod
    def from_row(cls, linha):
        id, tipo, titulo, edicao = linha
        return cls(titulo, id)

    def __repr__(self):
        return f"#{self.id} {self.titulo} ({self.tipo})"


class Livro(Item):
    tipo = "livro"

    def prazo_dias(self):
        return 14


class Revista(Item):
    tipo = "revista"

    def __init__(self, titulo, edicao, id=None):
        super().__init__(titulo, id)
        self.edicao = edicao

    def prazo_dias(self):
        return 7

    def to_params(self):
        return (self.tipo, self.titulo, self.edicao)

    @classmethod
    def from_row(cls, linha):
        id, tipo, titulo, edicao = linha
        return cls(titulo, edicao, id)

TIPOS = {"livro": Livro, "revista": Revista}

def criar_item(linha):
    id, tipo, titulo, edicao = linha
    classe = TIPOS.get(tipo)
    if not classe:
        raise ValueError(f"Tipo de item desconhecido: {tipo}")
    return classe.from_row(linha)

class RepositorioItens:
    def __init__(self, caminho):
        self.caminho = caminho
        create_table = """
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                titulo TEXT NOT NULL,
                edicao INTEGER
            )
        """
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute(create_table)

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, tipo, titulo, edicao FROM itens ORDER BY id"
            ).fetchall()
        return [criar_item(linha) for linha in linhas]

    def salvar(self, item):
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(
                "INSERT INTO itens (tipo, titulo, edicao) VALUES (?, ?, ?)",
                item.to_params()
            )
            item.id = cursor.lastrowid

    def buscar_por_id(self, id):
        with sqlite3.connect(self.caminho) as conexao:
            linha = conexao.execute(
                "SELECT id, tipo, titulo, edicao FROM itens WHERE id = ?",
                (id,)
            ).fetchone()
        if linha is None:
            return None
        return criar_item(linha)


# ===== TESTE (não altere estas linhas) =====
BANCO = Path(__file__).parent / "ex03.db"
with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS itens")    # começa do zero a cada execução

repo = RepositorioItens(BANCO)
repo.salvar(Livro("Dom Casmurro"))
repo.salvar(Revista("Superinteressante", 452))
repo.salvar(Livro("Vidas Secas"))
galileu = Revista("Galileu", 380)
repo.salvar(galileu)
print(galileu, galileu.edicao)    # #4 Galileu (revista) 380

outro = RepositorioItens(BANCO)    # como se o programa fechasse e abrisse de novo
itens = outro.listar()
print(itens)
# [#1 Dom Casmurro (livro), #2 Superinteressante (revista), #3 Vidas Secas (livro), #4 Galileu (revista)]
print(itens[1].edicao, itens[1].prazo_dias(), itens[0].prazo_dias())    # 452 7 14

achado = outro.buscar_por_id(2)
print(achado, achado.edicao)      # #2 Superinteressante (revista) 452
livro = outro.buscar_por_id(1)
print(livro, livro.prazo_dias())    # #1 Dom Casmurro (livro) 14
print(outro.buscar_por_id(99))    # None

mensagem = "nenhum erro"
try:
    criar_item((9, "jornal", "Jornal da Tarde", None))
except ValueError as erro:
    mensagem = str(erro)
print("Erro:", mensagem)    # Erro: tipo desconhecido: jornal

with sqlite3.connect(BANCO) as conexao:
    linhas = conexao.execute("SELECT id, tipo, titulo, edicao FROM itens ORDER BY id").fetchall()
print(linhas[0])    # (1, 'livro', 'Dom Casmurro', None)

prazos = sum([i.prazo_dias() for i in itens])
print(itens[3].edicao, prazos)    # 380 42

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-15. O nome tem que ser ex03.py.
#    (O arquivo ex03.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
