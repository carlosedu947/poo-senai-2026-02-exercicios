# Aula 01 · Exercício 05 (casa, OBRIGATÓRIO): par ou ímpar
#
# Crie duas funções:
#   eh_par(n): DEVOLVE True se n é par e False se é ímpar.
#     Dica: n % 2 == 0 já é True ou False.
#   contar_pares(numeros): DEVOLVE quantos números da lista são pares (use for e eh_par).
def eh_par(n):
    return n % 2 == 0


def contar_pares(numeros):
    total = 0
    for numero in numeros:
        if eh_par(numero):
            total += 1
    return total
#
# No fim do seu código, teste a sua função com print. Por exemplo:
#   print(eh_par(8))
#   print(contar_pares([3, 8, 11, 20]))

print(eh_par(8))
print(contar_pares([3, 8, 11, 20]))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-01. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
#True
#2
