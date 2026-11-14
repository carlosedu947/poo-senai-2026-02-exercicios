# Aula 13 · Exercício 03 (sala): o ingresso de cinema
#
# Três funções de preço. Cada uma recebe o preço base e RETORNA o preço do ingresso:
#   inteira(base)          RETORNA o próprio base
#   meia(base)             RETORNA metade do base (base / 2)
#   promocao_terca(base)   RETORNA 12, qualquer que seja o base
#
# Ingresso: o __init__ recebe filme, base e calcular_preco (uma FUNÇÃO de preço,
# que chega sem parênteses) e guarda os três com self.
#   preco()   RETORNA o resultado da função guardada, chamada com o base.
# Nenhum print dentro das funções nem da classe.
#
# O teste cria uma regra nova (idoso) depois da classe pronta.
# O seu Ingresso tem que usar essa regra sem nenhuma mudança.
#
# SE TRAVAR, REVEJA:
#   f × f() ................ aula 10, slide 8  https://poo.leoad.com.br/aulas/aula-10/#s8
#   função em dicionário ... aula 13, slide 7  https://poo.leoad.com.br/aulas/aula-13/#s7
#   Strategy com função .... aula 13, slide 11  https://poo.leoad.com.br/aulas/aula-13/#s11
#   trocar a regra ......... aula 13, slide 12  https://poo.leoad.com.br/aulas/aula-13/#s12
#   a função guardada ...... aula 13, slide 14  https://poo.leoad.com.br/aulas/aula-13/#s14


def inteira(base):
    return base

def meia(base):
    return base / 2

def promocao_terca(base):
    return 12

class Ingresso:
    def __init__(self, filme, base, calcular_preco):
        self.filme = filme
        self.base = base
        self.calcular_preco = calcular_preco

    def preco(self):
        return self.calcular_preco(self.base)

        

# ===== TESTE (não altere estas linhas) =====
ana = Ingresso("Duna", 30, inteira)
bia = Ingresso("Duna", 30, meia)
caio = Ingresso("Moana", 26, promocao_terca)

print(ana.filme, ana.preco())        # Duna 30
print(bia.preco())                   # 15.0
print(caio.filme, caio.preco())      # Moana 12
print(ana.preco() + bia.preco())     # 45.0

bia.calcular_preco = inteira         # a regra muda; a classe, não
print(bia.preco())                   # 30

def idoso(base):                     # regra nova: nenhuma linha muda no Ingresso
    return base * 40 / 100

dudu = Ingresso("Moana", 26, idoso)
print(dudu.preco())                  # 10.4

PRECOS = {"inteira": inteira, "meia": meia, "terça": promocao_terca}
caixa = 0
for tipo in ["meia", "inteira", "terça", "meia"]:
    caixa = caixa + Ingresso("Duna", 30, PRECOS[tipo]).preco()
print(caixa)                         # 72.0

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
