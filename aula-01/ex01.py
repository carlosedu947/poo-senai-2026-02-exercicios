# Aula 01 · Exercício 01 (sala): boas-vindas do mercadinho
#
# Crie a função boas_vindas(nome, loja="Mercadinho"), que DEVOLVE (return) o texto:
#   Olá, <nome>! Bem-vindo(a) ao <loja>.
# Se quem chama não mandar a loja, ela vale "Mercadinho".

def boas_vindas(nome, loja="Mercadinho"):
    return f"Olá, {nome}! Bem-vindo(a) ao {loja} ."


# ===== TESTE (não altere estas linhas) =====
print(boas_vindas("Ana"))               # Olá, Ana! Bem-vindo(a) ao Mercadinho.
print(boas_vindas("Bruno", "Sacolão"))  # Olá, Bruno! Bem-vindo(a) ao Sacolão.

print("chave:", f"{len(boas_vindas('Ana'))}-{len(boas_vindas('Bruno', 'Sacolão'))}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-01. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA:
#Olá, Ana! Bem-vindo(a) ao Mercadinho .
#Olá, Bruno! Bem-vindo(a) ao Sacolão .
#chave: 38-37
