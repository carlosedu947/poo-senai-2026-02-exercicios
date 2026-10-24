# Aula 06 · Exercício 01 (sala): Pessoa e Aluno
#
# Pessoa: o __init__ recebe nome e idade e guarda os dois.
#   idade          @property e @idade.setter. O setter RECUSA idade negativa:
#                      raise ValueError("idade não pode ser negativa")
#                  O __init__ faz self.idade = idade: o setter roda na criação.
#   apresentar()   RETORNA, por exemplo:  Oi, eu sou Bia e tenho 8 anos
#
# Aluno é uma Pessoa (herda de Pessoa):
#   o __init__ recebe nome, idade e curso. Chame super().__init__(nome, idade)
#   para o pai guardar nome e idade, e guarde só o curso no Aluno.
#   carteirinha()  RETORNA, por exemplo:  Elis | Redes
#
# O Aluno NÃO escreve de novo o apresentar() nem a idade: ele herda do pai,
# e a proteção da idade vem junto.
#
# SE TRAVAR, REVEJA:
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   herança ................ aula 06, slide 5  https://poo.leoad.com.br/aulas/aula-06/#s5
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade         

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("idade não pode ser negativa")
        self._idade = valor

    def apresentar(self):
        return f"Oi, eu sou {self.nome} e tenho {self.idade} anos"


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)   
        self.curso = curso

    def carteirinha(self):
        return f"{self.nome} | {self.curso}"
# ===== TESTE (não altere estas linhas) =====
p = Pessoa("Bia", 8)
a1 = Aluno("Diego", 19, "ADS")
a2 = Aluno("Elis", 23, "Redes")

print(p.apresentar())        
print(a1.apresentar())       
print(a1.carteirinha())      
print(a2.carteirinha())      
a2.idade = 24
print(a1.idade + a2.idade)   
print(isinstance(a1, Pessoa), isinstance(p, Aluno))    

recusadas = 0
try:
    Aluno("Gui", -1, "ADS")
except ValueError as erro:
    print("recusado:", erro)     
    recusadas = recusadas + 1
try:
    a1.idade = -5
except ValueError:
    recusadas = recusadas + 1
print(a1.idade, recusadas)   

print(f"chave: {a1.idade + a2.idade}-{len(p.apresentar())}-{len(a2.apresentar())}-{len(a1.carteirinha())}-{len(a2.carteirinha())}-{recusadas}-{isinstance(a2, Pessoa)}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA:Oi, eu sou Bia e tenho 8 anos
#Oi, eu sou Diego e tenho 19 anos
#Diego | ADS
#Elis | Redes
#43
#True False
#recusado: idade não pode ser negativa
#19 2
#chave: 43-29-31-11-12-2-True
