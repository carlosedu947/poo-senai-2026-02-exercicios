# Aula 05 · Exercício 03 (casa, OBRIGATÓRIO): a casa, os cômodos e os moradores
#
# Crie a classe Comodo:
#   o __init__ recebe nome e area, e guarda os dois.
#   area  @property e @area.setter. O setter RECUSA área 0 ou menos:
#             raise ValueError("área precisa ser maior que zero")
#         O __init__ faz self.area = area: o setter roda na criação.
# Crie a classe Morador: o __init__ recebe nome e guarda.
# Crie a classe Casa:
#   o __init__ recebe endereco, guarda, e cria self.comodos e self.moradores
#   como listas vazias.
#   adicionar_comodo(nome, area)  CRIA um Comodo ali dentro (composição)
#                                 e coloca na lista self.comodos.
#   receber(morador)              GUARDA o morador que chegou pronto
#                                 (associação) na lista self.moradores.
#   area_total()    RETORNA a soma das áreas dos cômodos, usando um for.
#   tem_morador(nome)  RETORNA True se algum morador da casa tem esse nome,
#                      e False se nenhum tem (um for com if; o False vem
#                      depois do for).
#
# SE TRAVAR, REVEJA:
#   composição ............. aula 05, slide 38  https://poo.leoad.com.br/aulas/aula-05/#s38
#   associação ............. aula 05, slide 39  https://poo.leoad.com.br/aulas/aula-05/#s39
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19


class Comodo:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area 
 
    @property
    def area(self):
        return self._area
 
    @area.setter
    def area(self, valor):
        if valor <= 0:
            raise ValueError("área precisa ser maior que zero")
        self._area = valor
 
 
class Morador:
    def __init__(self, nome):
        self.nome = nome
 
 
class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []
        self.moradores = []
 
    def adicionar_comodo(self, nome, area):
        comodo = Comodo(nome, area)  
        self.comodos.append(comodo)
 
    def receber(self, morador):
        self.moradores.append(morador)  
 
    def area_total(self):
        total = 0
        for comodo in self.comodos:
            total += comodo.area
        return total
 
    def tem_morador(self, nome):
        for morador in self.moradores:
            if morador.nome == nome:
                return True
        return False

ana = Morador("Ana")
bia = Morador("Bia")

casa = Casa("Rua 10, 25")
casa.adicionar_comodo("sala", 20)
casa.adicionar_comodo("quarto", 9)
casa.adicionar_comodo("cozinha", 12)
casa.receber(ana)
casa.receber(bia)

praia = Casa("Rua da Praia, 3")
praia.receber(ana)                       

print(len(casa.comodos), len(casa.moradores))    
print(casa.area_total())                         
print(casa.tem_morador("Bia"), praia.tem_morador("Bia"))    
print(praia.moradores[0] == casa.moradores[0])   
print(praia.area_total(), len(praia.comodos))    

try:
    casa.adicionar_comodo("banheiro", 0)
except ValueError as erro:
    print("recusado:", erro)                     
print(len(casa.comodos))                         

print(f"chave: {len(casa.comodos)}-{len(casa.moradores)}-{casa.area_total()}-{casa.tem_morador("Bia")}-{praia.tem_morador("Bia")}-{praia.moradores[0] == casa.moradores[0]}-{praia.area_total()}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA: c:/Users/Carlos Eduardo/Desktop/AULA05/ex03.py"
#3 2
#41
#True False
#True
#0 0
#recusado: área precisa ser maior que zero
#3
#chave: 3-2-41-True-False-True-0
