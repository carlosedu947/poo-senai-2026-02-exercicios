# Aula 10 · Exercício 01 (sala): o ingresso e a regra de preço
#
# Crie três funções. Cada uma recebe o preço cheio e RETORNA o preço a pagar:
#   inteira(preco)    retorna o preço sem mudar nada.
#   meia(preco)       retorna a metade do preço.
#   cortesia(preco)   retorna 0.
#
# Crie a classe Ingresso:
#   O __init__ recebe evento, preco e regra (uma das três funções) e guarda os três.
#   valor()  RETORNA o preço a pagar: chama a função guardada em self.regra,
#            passando o preço do ingresso.
#
# A função entra no Ingresso SEM parênteses: Ingresso("Show", 80, inteira).
# Nenhum print dentro das funções nem do método.
#
# SE TRAVAR, REVEJA:
#   f × f() ................ aula 10, slide 8  https://poo.leoad.com.br/aulas/aula-10/#s8
#   função em atributo ..... aula 10, slide 12  https://poo.leoad.com.br/aulas/aula-10/#s12
#   os dois tropeços ....... aula 10, slide 13  https://poo.leoad.com.br/aulas/aula-10/#s13

def inteira(preco):
    return preco


def meia(preco):
    return preco / 2


def cortesia(preco):
    return 0


class Ingresso:
    def __init__(self, evento, preco, regra):
        self.evento = evento
        self.preco = preco
        self.regra = regra

    def valor(self):
        return self.regra(self.preco)

# ===== TESTE (não altere estas linhas) =====
i1 = Ingresso("Show", 80, inteira)
i2 = Ingresso("Teatro", 50, meia)
i3 = Ingresso("Cinema", 30, cortesia)

print(i1.evento, i1.valor())    # Show 80
print(i2.evento, i2.valor())    # Teatro 25.0
print(i3.evento, i3.valor())    # Cinema 0

i1.regra = meia                 # trocou a regra do ingresso 1
print(i1.valor())               # 40.0

print(f"chave: {i1.valor() + i2.valor()}-{i3.valor()}-{inteira(9) + meia(9)}-{i2.regra == meia}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA: Show 80
# Teatro 25.0
# Cinema 0
# 40.0
# chave: 65.0-0-13.5-True
