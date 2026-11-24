# Aula 14 · Exercício 02 (sala): o repositório de pets
#
# A classe Pet já está pronta. Crie a classe RepositorioPets:
#   __init__(caminho)   guarda o caminho do banco em self.caminho e cria a tabela,
#                       com este SQL (o IF NOT EXISTS deixa criar o repositório
#                       quantas vezes quiser):
#                           CREATE TABLE IF NOT EXISTS pets (
#                               id INTEGER PRIMARY KEY AUTOINCREMENT,
#                               nome TEXT NOT NULL,
#                               especie TEXT NOT NULL,
#                               idade INTEGER NOT NULL
#                           )
#   salvar(pet)         INSERT do pet, com ? e pet.to_params(). Depois, guarda
#                       em pet.id o id que o banco gerou (cursor.lastrowid).
#   listar()            SELECT id, nome, especie, idade ... ORDER BY id, e RETORNA
#                       uma lista de objetos Pet (Pet.from_row em cada linha).
# Cada método abre o banco com:  with sqlite3.connect(self.caminho) as conexao:
# Nenhum print dentro da classe.
#
# SE TRAVAR, REVEJA:
#   repositório ............ aula 14, slide 23  https://poo.leoad.com.br/aulas/aula-14/#s23
#   __init__ e salvar ...... aula 14, slide 24  https://poo.leoad.com.br/aulas/aula-14/#s24
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   with sqlite3.connect ... aula 14, slide 15  https://poo.leoad.com.br/aulas/aula-14/#s15
#   ? e não f-string ....... aula 14, slide 16  https://poo.leoad.com.br/aulas/aula-14/#s16

import sqlite3
from pathlib import Path


class Pet:
    def __init__(self, nome, especie, idade, id=None):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade

    @classmethod
    def from_row(cls, linha):
        id, nome, especie, idade = linha
        return cls(nome, especie, idade, id)

    def to_params(self):
        return (self.nome, self.especie, self.idade)

    def __repr__(self):
        return f"Pet('{self.nome}', '{self.especie}', {self.idade}, {self.id})"


class RepositorioPets:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS pets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    especie TEXT NOT NULL,
                    idade INTEGER NOT NULL
                
            )
        """)

    def salvar(self, pet):
        sql = "INSERT INTO pets (nome, especie, idade) VALUES (?, ?, ?)"
        with sqlite3.connect(self.caminho) as conexao:
            cursor = conexao.execute(sql, pet.to_params())
        pet.id = cursor.lastrowid

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
            "SELECT id, nome, especie, idade FROM pets ORDER BY id"
            ).fetchall()
        return [Pet.from_row(linha) for linha in linhas]

# ===== TESTE (não altere estas linhas) =====
BANCO = Path(__file__).parent / "ex02.db"

with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS pets")    # começa do zero a cada execução

repo = RepositorioPets(BANCO)
# aspas duplas no nome do Rex e um apóstrofo no do gato: com ? os dois passam
rex = Pet('Rex "Fumaça"', "cachorro", 3)
print(rex.id)                     # None
repo.salvar(rex)
print(rex.id)                     # 1
repo.salvar(Pet("D'Artagnan", "gato", 2))
bolt = Pet("Bolt", "cachorro", 1)
repo.salvar(bolt)
print(bolt.id)                    # 3

pets = repo.listar()
print(pets[0])                    # Pet('Rex "Fumaça"', 'cachorro', 3, 1)
print(pets[1].nome, pets[1].id)   # D'Artagnan 2

outro = RepositorioPets(BANCO)    # outro repositório, o mesmo arquivo .db
print(len(outro.listar()))        # 3

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex02.py.
#    (O arquivo ex02.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA: None
# 1
# 3
# Pet('Rex "Fumaça"', 'cachorro', 3, 1)
# D'Artagnan 2
# 3
