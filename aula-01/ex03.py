# Aula 01 · Exercício 03 (sala): preços com desconto
#
# Crie a função com_desconto(precos, desconto=2), que DEVOLVE uma LISTA NOVA
# com cada preço menos o desconto. Se o resultado ficar negativo, coloque 0.
# A lista original não pode mudar. Dica: comece com nova = [] e use append.
def com_desconto(precos, desconto=2):
    nova = []
    for preco in precos:
        novo_preco = preco - desconto
        if novo_preco < 0:
            novo_preco = 0
        nova.append(novo_preco)
    return nova
# ===== TESTE (não altere estas linhas) =====
precos = [12, 5, 30, 8]

a = com_desconto(precos)
b = com_desconto(precos, 10)
print(a)                          # [10, 3, 28, 6]
print(b)                          # [2, 0, 20, 0]
print("Lista original:", precos)  # Lista original: [12, 5, 30, 8]

print("chave:", f"{a[0]}-{a[-1]}-{b[1]}-{b[3]}-{len(b)}-{precos[0]}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-01. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
# [10, 3, 28, 6]
# [2, 0, 20, 0]
# Lista original: [12, 5, 30, 8]
# chave: 10-6-0-0-4-12