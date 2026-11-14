# Aula 13 · Exercício 02 (sala): a fábrica de planos da academia
#
# Plano (a classe pai): o __init__ recebe aluno e guarda com self.
#   total(meses)   RETORNA self.mensalidade() vezes os meses.
# Três classes filhas herdam de Plano e só escrevem o método mensalidade(),
# que RETORNA o valor de um mês:
#   Mensal       120
#   Trimestral   100
#   Anual        80
#
# PLANOS: um dicionário que liga o texto à CLASSE (sem parênteses):
#   "mensal" -> Mensal,  "trimestral" -> Trimestral,  "anual" -> Anual
#
# matricular(tipo, aluno): a fábrica.
#   Se o tipo não estiver em PLANOS: raise ValueError(f"Plano desconhecido: {tipo}")
#   Senão: pega a classe em PLANOS e RETORNA um objeto novo dela.
# Nenhum print dentro das classes nem da função.
#
# O teste cria um plano novo (Diaria) e só acrescenta uma linha em PLANOS.
# A sua matricular tem que fabricar esse plano sem nenhuma mudança.
#
# SE TRAVAR, REVEJA:
#   herança ................ aula 06, slide 5  https://poo.leoad.com.br/aulas/aula-06/#s5
#   classe é valor ......... aula 13, slide 22  https://poo.leoad.com.br/aulas/aula-13/#s22
#   Simple Factory ......... aula 13, slide 24  https://poo.leoad.com.br/aulas/aula-13/#s24
#   erros da fábrica ....... aula 13, slide 26  https://poo.leoad.com.br/aulas/aula-13/#s26
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10


class Plano:
    def __init__(self, aluno):
        self.aluno = aluno

    def total(self,meses):
        return self.mensalidade() * meses

class Mensal(Plano):
    def mensalidade(self):
        return 120

class Trimestral(Plano):
    def mensalidade(self):
        return 100

class Anual(Plano):
    def mensalidade(self):
        return 80

PLANOS = {"mensal": Mensal, "trimestral": Trimestral, "anual": Anual}

def matricular(tipo, aluno):
    if tipo not in PLANOS:
        raise ValueError(f"Plano desconhecido: {tipo}")
    classe = PLANOS[tipo]
    return classe(aluno)


# ===== TESTE (não altere estas linhas) =====
p1 = matricular("mensal", "Ana")
p2 = matricular("trimestral", "Bruno")
p3 = matricular("anual", "Caio")

print(p1.aluno, p1.mensalidade())              # Ana 120
print(p2.aluno, p2.mensalidade())              # Bruno 100
print(p3.aluno, p3.total(12))                  # Caio 960
print(len(PLANOS))                             # 3
print(PLANOS["anual"]("Duda").total(2))        # 160

class Diaria(Plano):
    def mensalidade(self):
        return 200

PLANOS["diaria"] = Diaria                      # plano novo: só uma linha no dicionário
diaria = matricular("diaria", "Gil").total(1)
print(diaria)                                  # 200

aviso = "nenhum"
try:
    matricular("semanal", "Eva")
except ValueError as erro:
    aviso = str(erro)
print(aviso)                                   # Plano desconhecido: semanal

caixa = 0
for tipo in ["mensal", "anual", "anual", "trimestral"]:
    caixa = caixa + matricular(tipo, "Visitante").mensalidade()
print(caixa)                                   # 380

print(p2.total(3), isinstance(p3, Plano))      # 300 True

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:
