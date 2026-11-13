# Aula 12 · Exercício 02 (sala): o caixa que anota cada venda
#
# Venda: o __init__ recebe produto e valor e guarda os dois.
#   para_linha()      RETORNA, por exemplo:  café;3\n
#   de_linha(linha)   construtor alternativo (@classmethod): RETORNA cls(...),
#                     com o valor como float.
#
# registrar(venda, caminho): ACRESCENTA a linha da venda no fim do arquivo
#   (modo "a", encoding="utf-8"), sem apagar o que já estava lá.
# carregar(caminho): RETORNA a lista de Venda do arquivo. Pule as linhas em
#   branco. Se o arquivo não existir (FileNotFoundError), RETORNA uma lista vazia.
# total(vendas): RETORNA a soma dos valores das vendas.
# Nenhum print dentro da classe nem das funções.
#
# SE TRAVAR, REVEJA:
#   modo a ................. aula 11, slide 10  https://poo.leoad.com.br/aulas/aula-11/#s10
#   tudo é texto ........... aula 12, slide 5  https://poo.leoad.com.br/aulas/aula-12/#s5
#   de_linha e para_linha .. aula 12, slide 6  https://poo.leoad.com.br/aulas/aula-12/#s6
#   linha em branco ........ aula 12, slide 12  https://poo.leoad.com.br/aulas/aula-12/#s12
#   FileNotFoundError ...... aula 11, slide 17  https://poo.leoad.com.br/aulas/aula-11/#s17

from pathlib import Path


class Venda:
    def __init__(self, produto, valor):
        self.produto = produto
        self.valor = valor
 
    def para_linha(self):
        return f"{self.produto};{self.valor}\n"
 
    @classmethod
    def de_linha(cls, linha):
        produto, valor = linha.strip().split(";")
        return cls(produto, float(valor))
 
 
def registrar(venda, caminho):
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(venda.para_linha())
 
 
def carregar(caminho):
    vendas = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.strip() == "":
                    continue
                vendas.append(Venda.de_linha(linha))
    except FileNotFoundError:
        return []
    return vendas
 
 
def total(vendas):
    soma = 0
    for venda in vendas:
        soma = soma + venda.valor
    return soma
 



# ===== TESTE (não altere estas linhas) =====
PASTA = Path(__file__).parent
caminho = PASTA / "caixa.txt"

with open(caminho, "w", encoding="utf-8") as arquivo:    # o dia começa com uma venda
    arquivo.write("pão de queijo;4.5\n")                 # e uma linha em branco
    arquivo.write("\n")

registrar(Venda("café", 3), caminho)
registrar(Venda("bolo", 7.25), caminho)

vendas = carregar(caminho)
print(len(vendas), total(vendas))                 # 3 14.75
print(vendas[2].produto)                          # bolo
print(carregar(PASTA / "nao_existe.txt"))         # []

with open(caminho, "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
print(repr(texto))                                # 'pão de queijo;4.5\n\ncafé;3\nbolo;7.25\n'

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-12. O nome tem que ser ex02.py.
#    (O arquivo caixa.txt que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
# 3 14.75
# bolo
# []
# 'pão de queijo;4.5\n\ncafé;3\nbolo;7.25\n'
