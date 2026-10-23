# Aula 05 · Exercício 01 (sala): a classe Time
#
# Crie a classe Time.
# O __init__ recebe nome, jogadores e cidade, nessa ordem, e guarda os três.
#   nome      @property só de leitura (sem setter): o __init__ grava self._nome.
#   jogadores é opcional: quem não mandar uma lista, o time nasce com uma
#             lista vazia NOVA, só dele. Use None como padrão, nunca [].
#   cidade    é opcional e vale "Goiânia" quando ninguém mandar.
# escalar(jogador)  se o jogador for um texto vazio (""), LEVANTE
#                       ValueError("jogador precisa de nome")
#                   senão, coloca o jogador no fim da lista self.jogadores.
# tamanho()         RETORNA quantos jogadores o time tem.
# __repr__          RETORNA, por exemplo:  Time('Verde', 2 jogadores)
#                   (use self.tamanho() no texto)
#
# SE TRAVAR, REVEJA:
#   valor padrão ........... aula 05, slide 6  https://poo.leoad.com.br/aulas/aula-05/#s6
#   lista como padrão ...... aula 05, slide 15  https://poo.leoad.com.br/aulas/aula-05/#s15
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27


class Time:
    def __init__(self, nome, jogadores=None, cidade="Goiânia"):
        self._nome = nome
        if jogadores is None:
            jogadores = []
        self.jogadores = jogadores
        self.cidade = cidade

    @property
    def nome(self):
        return self._nome

    def escalar(self, jogador):
        if jogador == "":
            raise ValueError("jogador precisa de nome")
        self.jogadores.append(jogador)

    def tamanho(self):
        return len(self.jogadores)

    def __repr__(self):
        return f"Time('{self.nome}', {self.tamanho()} jogadores)"

    
# ===== TESTE (não altere estas linhas) =====
azul = Time("Azul")
verde = Time("Verde", cidade="Anápolis")
amarelo = Time("Amarelo", ["Ana", "Bia"], "Trindade")

azul.escalar("Caio")
verde.escalar("Duda")
verde.escalar("Enzo")
amarelo.escalar("Fábio")

print(azul.jogadores)                    # ['Caio']
print(verde.tamanho(), verde.cidade)     # 2 Anápolis
print(amarelo.tamanho(), azul.cidade)    # 3 Goiânia
print(Time("Roxo").tamanho())            # 0
print(repr(verde))                       # Time('Verde', 2 jogadores)

recusas = 0
try:
    azul.escalar("")
except ValueError as erro:
    print("recusado:", erro)             # recusado: jogador precisa de nome
    recusas = recusas + 1
try:
    azul.nome = "Celeste"
except AttributeError:
    print("nome só de leitura")          # nome só de leitura
    recusas = recusas + 1
print(azul.tamanho(), azul.nome)         # 1 Azul

print(f"chave: {azul.tamanho()}-{verde.tamanho()}-{amarelo.tamanho()}-{Time('Roxo').tamanho()}-{len(verde.cidade)}-{amarelo.nome}-{recusas}-{len(repr(verde))}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA: ['Caio']
#2 Anápolis
#0
#nome só de leitura
#1 Azul
#chave: 1-2-3-0-8-Amarelo-2-26
