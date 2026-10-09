# Aula 01 · Exercício 02 (sala): total do carrinho
#
# Crie duas funções:
#   total(precos): DEVOLVE a soma dos preços da lista (use for e acumulador, sem sum()).
#   contar_caros(precos, limite=10): DEVOLVE quantos preços são MAIORES que o limite.
def total(precos):
    soma = 0
    for preco in precos:
        soma = soma + preco
    return soma     
def contar_caros(precos, limite=10):
    contador = 0
    for preco in precos:
        if preco > limite:
            contador = contador + 1
    return contador
# ===== TESTE (não altere estas linhas) =====
precos = [12, 5, 30, 8]

print("Total:", total(precos))                   # Total: 55
print("Caros:", contar_caros(precos))            # Caros: 2
print("Acima de 20:", contar_caros(precos, 20))  # Acima de 20: 1

print("chave:", f"{total(precos)}-{contar_caros(precos)}-{contar_caros([10, 11, 9])}-{contar_caros([1, 50, 60, 70])}-{total([])}-{contar_caros(precos, 20)}")
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-01. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA: