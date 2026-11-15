# Aula 13 · Exercício 05 (casa, OBRIGATÓRIO): o frete da loja
#
# Três classes de frete. Cada uma tem só o método calcular(peso), que RETORNA
# o frete em reais para um pacote com aquele peso (em kg):
#   Sedex      20 + 5 * peso
#   Pac        12 + 2 * peso
#   Retirada   0, qualquer que seja o peso
#
# FRETES: um dicionário que liga o texto à CLASSE (sem parênteses):
#   "sedex" -> Sedex,  "pac" -> Pac,  "retirada" -> Retirada
#
# criar_frete(tipo): a fábrica.
#   Se o tipo não estiver em FRETES: raise ValueError(f"Frete desconhecido: {tipo}")
#   Senão: pega a classe em FRETES e RETORNA um objeto novo dela.
#
# Pedido: o __init__ recebe valor, peso e frete (um OBJETO de frete) e guarda os três.
#   total()   RETORNA o valor mais o frete, delegando a conta: self.frete.calcular(self.peso)
# Nenhum print dentro das classes nem da função.
#
# Exemplos:
#   Pedido(100, 2, criar_frete("sedex")).total()       retorna 130
#   o mesmo pedido, depois de trocar o frete por criar_frete("pac"):  116
#   Pedido(100, 2, criar_frete("retirada")).total()    retorna 100
#   criar_frete("drone") dentro de try/except ValueError mostra:
#   Frete desconhecido: drone
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   Simple Factory ......... aula 13, slide 24  https://poo.leoad.com.br/aulas/aula-13/#s24
#   erros da fábrica ....... aula 13, slide 26  https://poo.leoad.com.br/aulas/aula-13/#s26
#   Strategy com classe .... aula 13, slide 18  https://poo.leoad.com.br/aulas/aula-13/#s18
#   delegar ................ aula 13, slide 19  https://poo.leoad.com.br/aulas/aula-13/#s19
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10

class Sedex:
    def calcular(self, peso):
        return 20 + 5 * peso
 
 
class Pac:
    def calcular(self, peso):
        return 12 + 2 * peso
 
 
class Retirada:
    def calcular(self, peso):
        return 0
 
 
FRETES = {"sedex": Sedex, "pac": Pac, "retirada": Retirada}
 
 
def criar_frete(tipo):
    if tipo not in FRETES:
        raise ValueError(f"Frete desconhecido: {tipo}")
    classe = FRETES[tipo]
    return classe()
 
 
class Pedido:
    def __init__(self, valor, peso, frete):
        self.valor = valor
        self.peso = peso
        self.frete = frete
 
    def total(self):
        return self.valor + self.frete.calcular(self.peso)
 
 
# ----- Teste -----
pedido = Pedido(100, 2, criar_frete("sedex"))
print(pedido.total())
 
pedido.frete = criar_frete("pac")
print(pedido.total())
 
print(Pedido(100, 2, criar_frete("retirada")).total())
 
try:
    criar_frete("drone")
except ValueError as erro:
    print(erro)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA: 130
# 116
# 100
# Frete desconhecido: drone
