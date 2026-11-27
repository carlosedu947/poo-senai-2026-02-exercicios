# Aula 15 · Exercício 02 (sala): o cadastro que recusa e-mail repetido
#
# A classe Usuario e parte do repositório já estão prontos. Na tabela, o e-mail é UNIQUE e o nome é NOT NULL. Escreva:
#
# cadastrar(usuario)   tenta o INSERT (e-mail e nome). Se der certo, guarda o
#                      id gerado em usuario.id e RETORNA True. Se o banco
#                      recusar o dado (sqlite3.IntegrityError), RETORNA False.
#                      Só esse erro: um erro de SQL tem que continuar aparecendo.
# buscar_por_email(email)   RETORNA o Usuario com aquele e-mail, ou None se
#                      não existir. Use WHERE email = ?, fetchone e from_row.
#
# SE TRAVAR, REVEJA:
#   tratar o IntegrityError . aula 15, slide 22  https://poo.leoad.com.br/aulas/aula-15/#s22
#   o except largo ......... aula 15, slide 25  https://poo.leoad.com.br/aulas/aula-15/#s25
#   listar e buscar ........ aula 14, slide 25  https://poo.leoad.com.br/aulas/aula-14/#s25
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

import sqlite3
from pathlib import Path


class Usuario:
    def __init__(self, email, nome, id=None):
        self.id = id
        self.email = email
        self.nome = nome

    def to_params(self):
        return (self.email, self.nome)

    @classmethod
    def from_row(cls, linha):
        id, email, nome = linha
        return cls(email, nome, id)

    def __str__(self):
        return f"#{self.id} {self.nome} <{self.email}>"


class RepositorioUsuarios:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE,
                    nome TEXT NOT NULL
                )
            """)

    def listar(self):
        with sqlite3.connect(self.caminho) as conexao:
            linhas = conexao.execute(
                "SELECT id, email, nome FROM usuarios ORDER BY id"
            ).fetchall()
        return [Usuario.from_row(linha) for linha in linhas]

    def cadastrar(self, usuario):
        try:
            with sqlite3.connect(self.caminho) as conexao:
                cursor = conexao.execute(
                    "INSERT INTO usuarios (email, nome) VALUES (?, ?)",
                    usuario.to_params(),
                )
                usuario.id = cursor.lastrowid
            return True
        except sqlite3.IntegrityError:
            return False

    def buscar_por_email(self, email):
        with sqlite3.connect(self.caminho) as conexao:
            linha = conexao.execute(
                "SELECT id, email, nome FROM usuarios WHERE email = ?",
                (email,),
            ).fetchone()
        if linha is None:
            return None
        return Usuario.from_row(linha)


# ===== TESTE (não altere estas linhas) =====
BANCO = Path(__file__).parent / "ex02.db"
with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS usuarios")    # começa do zero a cada execução

repo = RepositorioUsuarios(BANCO)
r1 = repo.cadastrar(Usuario("ana@email.com", "Ana"))
r2 = repo.cadastrar(Usuario("bia@email.com", "Bia"))
r3 = repo.cadastrar(Usuario("ana@email.com", "Ana Paula"))    # e-mail repetido
r4 = repo.cadastrar(Usuario("caio@email.com", None))          # sem nome
r5 = repo.cadastrar(Usuario("duda@email.com", ""))            # texto vazio
print(r1, r2, r3, r4, r5)    # True True False False True

bia = repo.buscar_por_email("bia@email.com")
print(bia)                                     # #2 Bia <bia@email.com>
print(repo.buscar_por_email("zeca@email.com"))    # None

edu = Usuario("edu@email.com", "Edu")
repo.cadastrar(edu)
print(edu.id, len(repo.listar()))    # 4 4
caio = repo.buscar_por_email("caio@email.com")
print(caio)                          # None

with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE usuarios")    # de propósito: agora o INSERT é um erro de SQL
try:
    repo.cadastrar(Usuario("eva@email.com", "Eva"))
    sql = "escondido"
except sqlite3.OperationalError as erro:
    sql = "apareceu"
    print("Erro de SQL:", erro)    # Erro de SQL: no such table: usuarios

print("O erro de SQL", sql)    # O erro de SQL apareceu

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-15. O nome tem que ser ex02.py.
#    (O arquivo ex02.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA: True True False False True
#2 Bia <bia@email.com>
#None
#4 4
#None
#Erro de SQL: no such table: usuarios
#O erro de SQL apareceu
