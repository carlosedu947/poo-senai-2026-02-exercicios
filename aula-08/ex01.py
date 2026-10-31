# Aula 08 · Exercício 01 (sala): o Animal vira classe abstrata
#
# Do jeito que está, dá para criar um Animal genérico e um Peixe sem som(),
# e o Python aceita os dois em silêncio. Rode e veja: sai "aceito aceito".
# E o nome do animal ainda pode ser trocado: sai "mudou Bob".
#
# Transforme Animal em classe abstrata:
# 1. Logo acima da classe Animal, escreva: from abc import ABC, abstractmethod
# 2. Animal herda de ABC.
# 3. som() vira método abstrato: @abstractmethod em cima do def,
#    e o corpo vira só pass.
# 4. O nome vira property SÓ DE LEITURA: o __init__ grava self._nome, e a
#    @property nome retorna self._nome. Animal criado não troca de nome.
# Não mexa no apresentar(), nem em Cachorro, Gato e Peixe.
#
# SE TRAVAR, REVEJA:
#   classe abstrata ........ aula 08, slide 8  https://poo.leoad.com.br/aulas/aula-08/#s8
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @abstractmethod
    def som(self):
        pass

    def apresentar(self):
        return f"{self.nome} diz {self.som()}"


class Cachorro(Animal):
    def som(self):
        return "Au"


class Gato(Animal):
    def som(self):
        return "Miau"


class Peixe(Animal):
    pass  # peixe não tem som(): não pode virar objeto


# ===== TESTE (não altere estas linhas) =====
rex = Cachorro("Rex")
mimi = Gato("Mimi")
print(rex.apresentar())     # Rex diz Au
print(mimi.apresentar())    # Mimi diz Miau

try:
    Animal("Bicho")
    animal = "aceito"
except TypeError:
    animal = "recusado"

try:
    Peixe("Nemo")
    peixe = "aceito"
except TypeError:
    peixe = "recusado"

print(animal, peixe)        # recusado recusado
print(isinstance(mimi, Animal))    # True

try:
    rex.nome = "Bob"
    nome = "mudou"
except AttributeError:
    nome = "protegido"
print(nome, rex.nome)       # protegido Rex

print(f"chave: {mimi.som()}-{animal}-{peixe}-{len(rex.apresentar())}-{nome}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-08. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA:
# Rex diz Au
# Mimi diz Miau
# recusado recusado
# True
# protegido Rex
# chave: Miau-recusado-recusado-10-protegido

