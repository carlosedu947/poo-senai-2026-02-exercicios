# Aula 07 · Exercício 04 (casa, OBRIGATÓRIO): a orquestra polimórfica
#
# Instrumento: o __init__ recebe nome.
#   nome      @property SÓ DE LEITURA (guarde em self._nome): o nome não muda.
#   som()     RETORNA "..." (o pai não sabe qual é o som)
#   tocar()   RETORNA, por exemplo:  Violão faz plim plim
#             usando self.nome e self.som()
#   __str__   RETORNA o mesmo texto do tocar() (chame self.tocar()).
# Crie três filhas de Instrumento que SOBRESCREVEM som():
#   Violao()   som "plim plim"     Bateria()  som "tum tum"     Flauta()  som "fiu fiu"
#   Cada filha chama super().__init__ com o próprio nome: "Violão", "Bateria", "Flauta".
#   Nenhuma filha reescreve o tocar(): ele vem do pai e chama o som() certo sozinho.
# Monte uma lista com os três e, num for SEM nenhum if, imprima o tocar() de cada um.
# Depois crie a filha Sanfona() (som "fom fom"), coloque na lista e rode de novo:
# o for não pode mudar nenhuma linha.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir. Mostre também print(violao)
# e, com try/except, que violao.nome = "Guitarra" dá AttributeError.
#
# SE TRAVAR, REVEJA:
#   sobrescrita no for ..... aula 07, slide 8  https://poo.leoad.com.br/aulas/aula-07/#s8
#   classe nova no for ..... aula 07, slide 9  https://poo.leoad.com.br/aulas/aula-07/#s9
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13


class Instrumento:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def som(self):
        return "..."

    def tocar(self):
        return f"{self.nome} faz {self.som()}"

    def __str__(self):
        return self.tocar()


class Violao(Instrumento):
    def __init__(self):
        super().__init__("Violão")

    def som(self):
        return "plim plim"


class Bateria(Instrumento):
    def __init__(self):
        super().__init__("Bateria")

    def som(self):
        return "tum tum"


class Flauta(Instrumento):
    def __init__(self):
        super().__init__("Flauta")

    def som(self):
        return "fiu fiu"


class Sanfona(Instrumento):
    def __init__(self):
        super().__init__("Sanfona")

    def som(self):
        return "fom fom"


violao = Violao()
bateria = Bateria()
flauta = Flauta()

instrumentos = [violao, bateria, flauta]

for instrumento in instrumentos:
    print(instrumento.tocar())


sanfona = Sanfona()
instrumentos.append(sanfona)

print("\nCom a Sanfona:")

for instrumento in instrumentos:
    print(instrumento.tocar())

print(violao)

try:
    violao.nome = "Guitarra"
except AttributeError as erro:
    print("Erro:", erro)
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:
# Violão faz plim plim
# Bateria faz tum tum
# Flauta faz fiu fiu
#
# Com a Sanfona:
# Violão faz plim plim
# Bateria faz tum tum
# Flauta faz fiu fiu
# Sanfona faz fom fom
# Violão faz plim plim
# Erro: property 'nome' of 'Violao' object has no setter
