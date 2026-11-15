# Aula 12 · Exercício 05 (casa, OBRIGATÓRIO): o estoque em JSON
#
# Comece o arquivo com:  import json  e  from pathlib import Path
#
# Produto: o __init__ recebe nome, preco e quantidade e guarda os três.
#   valor_em_estoque()   RETORNA preco * quantidade.
#   para_dict()          RETORNA {"nome": ..., "preco": ..., "quantidade": ...}
#   de_dict(dados)       construtor alternativo (@classmethod): RETORNA cls(...).
#   __repr__             retorna, por exemplo:  Produto('Caneta', 2.5, 100)
#
# salvar_produtos(produtos, caminho): cada produto vira dicionário com para_dict(),
#   e a lista inteira vai para o arquivo com json.dump (modo "w", encoding="utf-8",
#   ensure_ascii=False, indent=2).
# carregar_produtos(caminho): lê com json.load e RETORNA uma lista de Produto
#   (use Produto.de_dict). Se o arquivo não existir, RETORNA uma lista vazia.
#
# Exemplo: salve Produto('Caneta', 2.5, 100), Produto('Caderno', 25, 10) e
# Produto('Borracha', 1.5, 40) em produtos.json, na mesma pasta deste arquivo
# (Path(__file__).parent / "produtos.json"). Carregue de volta, imprima a lista
# e a soma do valor_em_estoque() de todos: 560.0
#
# Teste você mesmo: no fim do arquivo, salve, carregue e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   para_dict e de_dict .... aula 12, slide 23  https://poo.leoad.com.br/aulas/aula-12/#s23
#   salvar a lista ......... aula 12, slide 26  https://poo.leoad.com.br/aulas/aula-12/#s26
#   carregar a lista ....... aula 12, slide 28  https://poo.leoad.com.br/aulas/aula-12/#s28
#   FileNotFoundError ...... aula 11, slide 17  https://poo.leoad.com.br/aulas/aula-11/#s17
#   Path(__file__).parent .. aula 11, slide 19  https://poo.leoad.com.br/aulas/aula-11/#s19
#   sum .................... aula 10, slide 28  https://poo.leoad.com.br/aulas/aula-10/#s28

import json
from pathlib import Path
 
 
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
 
    def valor_em_estoque(self):
        return self.preco * self.quantidade
 
    def para_dict(self):
        return {"nome": self.nome, "preco": self.preco, "quantidade": self.quantidade}
 
    @classmethod
    def de_dict(cls, dados):
        return cls(dados["nome"], dados["preco"], dados["quantidade"])
 
    def __repr__(self):
        return f"Produto({self.nome!r}, {self.preco}, {self.quantidade})"
 
 
def salvar_produtos(produtos, caminho):
    dados = [produto.para_dict() for produto in produtos]
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)
 
 
def carregar_produtos(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return []
    return [Produto.de_dict(item) for item in dados]
 
 
# ----- Teste -----
caminho = Path(__file__).parent / "produtos.json"
 
salvar_produtos(
    [Produto("Caneta", 2.5, 100), Produto("Caderno", 25, 10), Produto("Borracha", 1.5, 40)],
    caminho,
)
 
produtos = carregar_produtos(caminho)
print(produtos)
print(sum(p.valor_em_estoque() for p in produtos))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-12. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA: [Produto('Caneta', 2.5, 100), Produto('Caderno', 25, 10), Produto('Borracha', 1.5, 40)]
# 560.0
