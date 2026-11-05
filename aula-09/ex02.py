# Aula 09 · Exercício 02 (sala): a comanda do restaurante
#
# Escreva as 4 classes do diagrama (está no slide e neste endereço):
#   https://poo.leoad.com.br/images/aula-09/ex02-comanda.svg
# Leia cada linha do diagrama antes de escrever o __init__:
#   linha simples   o objeto chega PRONTO, por parâmetro, e é só guardado.
#   losango cheio   o todo CRIA a parte num método dele e guarda na lista.
#
# ItemComanda.subtotal()   RETORNA o preço do prato vezes a quantidade.
# Comanda                  começa com a lista itens vazia.
#   pedir(prato, quantidade)  cria o ItemComanda e guarda na lista.
#   total()                   RETORNA a soma dos subtotais (um for).
#   com_servico()             RETORNA o total mais 10%:
#                             self.total() + self.total() * 10 / 100
#
# SE TRAVAR, REVEJA:
#   linhas do diagrama ..... aula 09, slide 15  https://poo.leoad.com.br/aulas/aula-09/#s15
#   composição ............. aula 05, slide 42  https://poo.leoad.com.br/aulas/aula-05/#s42


class Garcom:
    def __init__(self, nome):
        self.nome = nome


class Prato:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class ItemComanda:
    def __init__(self, prato, quantidade):
        self.prato = prato
        self.quantidade = quantidade

    def subtotal(self):
        return self.prato.preco * self.quantidade


class Comanda:
    def __init__(self, numero, garcom):
        self.numero = numero
        self.garcom = garcom     
        self.itens = []           

    def pedir(self, prato, quantidade):
        item = ItemComanda(prato, quantidade)
        self.itens.append(item)

    def total(self):
        soma = 0
        for item in self.itens:
            soma += item.subtotal()
        return soma

    def com_servico(self):
        return self.total() + self.total() * 10 / 100
    
# ===== TESTE (não altere estas linhas) =====
jorge = Garcom("Jorge")
pamonha = Prato("Pamonha", 12)
galinhada = Prato("Galinhada", 45)

comanda = Comanda(7, jorge)
comanda.pedir(pamonha, 3)
comanda.pedir(galinhada, 1)

print(len(comanda.itens))             # 2
print(comanda.itens[0].subtotal())    # 36
print(comanda.total())                # 81
print(comanda.com_servico())          # 89.1
print(comanda.garcom == jorge)        # True
print(comanda.itens[1].prato == galinhada)    # True

outra = Comanda(8, jorge)
print(len(outra.itens), outra.total())        # 0 0

print(f"chave: {len(comanda.itens)}-{comanda.total()}-{comanda.com_servico()}-{comanda.garcom.nome}-{comanda.itens[1].prato == galinhada}-{len(outra.itens)}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:
