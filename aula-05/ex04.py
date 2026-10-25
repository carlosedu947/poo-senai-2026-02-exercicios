# Aula 05 · Exercício 04 (casa, OBRIGATÓRIO): a classe Van
#
# Atributo de CLASSE: capacidade = 4 (quantos passageiros cabem em toda van).
# O __init__ recebe rota e passageiros, nessa ordem, e guarda os dois.
#   rota        @property só de leitura (sem setter): o __init__ grava self._rota.
#   passageiros é opcional: quem não mandar uma lista, a van nasce com uma
#   lista vazia NOVA, só dela. Use None como padrão, nunca [].
# embarcar(nome)    se o nome for um texto vazio (""), LEVANTE
#                       ValueError("passageiro precisa de nome")
#                   se ainda cabe gente, coloca o nome na lista e RETORNA True;
#                   se está cheia, não coloca e RETORNA False.
# lugares_livres()  RETORNA quantos lugares ainda sobram (use Van.capacidade).
#
# Exemplos:
#   Van("Centro") embarca Ana, Bia, Caio e Duda: os 4 embarques retornam True;
#   o 5º embarque retorna False, e lugares_livres() retorna 0.
#   Uma Van("Campus") criada depois começa com lugares_livres() igual a 4.
#   Uma Van("Setor Sul", ["Enzo"]) começa com lugares_livres() igual a 3.
#   Depois de Van.capacidade = 6, a van "Centro" passa a ter 2 lugares livres.
#   embarcar("") é recusado com ValueError: mostre a mensagem com try/except.
#
# Teste você mesmo: no fim do arquivo, crie as vans dos exemplos e mostre
# os resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   lista como padrão ...... aula 05, slide 15  https://poo.leoad.com.br/aulas/aula-05/#s15
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13

class Van:
    capacidade = 4
 
    def __init__(self, rota, passageiros=None):
        self._rota = rota
        if passageiros is None:
            passageiros = []
        self.passageiros = passageiros
 
    @property
    def rota(self):
        return self._rota
 
    def embarcar(self, nome):
        if nome == "":
            raise ValueError("passageiro precisa de nome")
        if len(self.passageiros) < Van.capacidade:
            self.passageiros.append(nome)
            return True
        return False
 
    def lugares_livres(self):
        return Van.capacidade - len(self.passageiros)

centro = Van("Centro")
print(centro.embarcar("Ana"), centro.embarcar("Bia"), centro.embarcar("Caio"), centro.embarcar("Duda"))
print(centro.embarcar("Eva"))
print(centro.lugares_livres())
 
campus = Van("Campus")
print(campus.lugares_livres())
 
sul = Van("Setor Sul", ["Enzo"])
print(sul.lugares_livres())
 
Van.capacidade = 6
print(centro.lugares_livres())
 
try:
    centro.embarcar("")
except ValueError as erro:
    print("recusado:", erro)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:True True True True
#False
#0
#4
#3
#2
#recusado: passageiro precisa de nome
