# Aula 14 · Exercício 01 (sala): a receita vira linha e volta
#
# Receita: o __init__ recebe nome, porcoes, minutos e id, com id=None como
# valor padrão (a receita ainda não está no banco), e guarda os quatro com self.
#   from_row(linha)   construtor alternativo (@classmethod). Recebe a tupla que
#                     vem do banco, na ordem (id, nome, porcoes, minutos), e
#                     RETORNA cls(...) com os quatro valores no lugar certo.
#   to_params()       RETORNA a tupla (nome, porcoes, minutos), nessa ordem: os
#                     valores para os ? do INSERT. Sem o id: quem gera é o banco.
# O __repr__ já está pronto. Nenhum print dentro da classe.
#
# SE TRAVAR, REVEJA:
#   from_row e to_params ... aula 14, slide 18  https://poo.leoad.com.br/aulas/aula-14/#s18
#   o return do from_row ... aula 14, slide 19  https://poo.leoad.com.br/aulas/aula-14/#s19
#   a ordem do to_params ... aula 14, slide 20  https://poo.leoad.com.br/aulas/aula-14/#s20
#   para_dict e de_dict .... aula 12, slide 23  https://poo.leoad.com.br/aulas/aula-12/#s23
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

import sqlite3
from pathlib import Path


class Receita:
    def __init__(self, nome, porcoes, minutos, id=None):
        self.nome = nome
        self.porcoes = porcoes
        self.minutos = minutos 
        self.id = id 

    @classmethod
    def from_row(cls, linha):
            id, nome, porcoes, minutos = linha
            return cls(nome, porcoes, minutos, id)  

    def to_params(self):
            return (self.nome, self.porcoes, self.minutos)
    
    def __repr__(self):
            return (
                f"Receita({self.nome!r}, {self.porcoes}, "
                f"{self.minutos}, {self.id})"
        )



# ===== TESTE (não altere estas linhas) =====
BANCO = Path(__file__).parent / "ex01.db"

with sqlite3.connect(BANCO) as conexao:
    conexao.execute("DROP TABLE IF EXISTS receitas")    # começa do zero a cada execução
    conexao.execute("""
        CREATE TABLE receitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            porcoes INTEGER NOT NULL,
            minutos INTEGER NOT NULL
        )
    """)
    sql = "INSERT INTO receitas (nome, porcoes, minutos) VALUES (?, ?, ?)"
    conexao.execute(sql, Receita("Bolo de fubá", 12, 50).to_params())
    conexao.execute(sql, Receita("Pão de queijo", 30, 40).to_params())
    linhas = conexao.execute("SELECT id, nome, porcoes, minutos FROM receitas ORDER BY id").fetchall()

nova = Receita("Cuscuz", 4, 15)
print(nova.id, nova.to_params())    # None ('Cuscuz', 4, 15)
print(linhas[1])                    # (2, 'Pão de queijo', 30, 40)

bolo = Receita.from_row(linhas[0])
pao = Receita.from_row(linhas[1])
print(bolo)                         # Receita('Bolo de fubá', 12, 50, 1)
print(pao.nome, pao.id)             # Pão de queijo 2

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-14. O nome tem que ser ex01.py.
#    (O arquivo ex01.db que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA: None ('Cuscuz', 4, 15)
#(2, 'Pão de queijo', 30, 40)
# Receita('Bolo de fubá', 12, 50, 1)
# Pão de queijo 2
