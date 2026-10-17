# Aula 04 · Exercício 02 (sala): o ar-condicionado que recusa
#
# Parte 1. Na classe ArCondicionado, escreva a property temperatura e o setter:
# - o getter retorna self._temperatura;
# - o setter só aceita de 16 a 30 (16 e 30 valem): compare com < e >,
#   como no ex01. Fora disso, LEVANTE:
#       ValueError("temperatura precisa estar entre 16 e 30")
#   e só guarda em self._temperatura depois de validar.
# O __init__ já faz self.temperatura = temperatura: assim o setter roda
# também na criação. Não troque por self._temperatura.
#
# Parte 2. Escreva a função regular(aparelho, valores). Para cada valor da
# lista, ela tenta fazer aparelho.temperatura = valor, dentro de um try.
# Se o setter recusar (except ValueError), conta uma recusa e segue para o
# próximo valor. No fim, RETORNA quantas recusas houve.
# Só o ValueError conta como recusa. Qualquer outro erro tem que sair do
# regular: o teste confere isso.
#
# Parte 3. Escreva o __repr__ do ArCondicionado, que RETORNA, por exemplo:
#     ArCondicionado('sala', 22)
# (aspas simples em volta do cômodo; a temperatura sem aspas)
#
# SE TRAVAR, REVEJA:
#   setter ................. aula 03, slide 18  https://poo.leoad.com.br/aulas/aula-03/#s18
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27


class ArCondicionado:
    def __init__(self, comodo, temperatura):
        self.comodo = comodo
        self.temperatura = temperatura    # passa pelo setter

    # escreva aqui a property temperatura e o setter
    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < 16 or valor > 30:
            raise ValueError("temperatura precisa estar entre 16 e 30")
        self._temperatura = valor

    # escreva aqui o __repr__
    def __repr__(self):
        return f"ArCondicionado('{self.comodo}', {self.temperatura})"


def regular(aparelho, valores):
    recusas = 0
    for valor in valores:
        try:
            aparelho.temperatura = valor
        except ValueError:
            recusas += 1
    return recusas


# ===== TESTE (não altere estas linhas) =====
sala = ArCondicionado("sala", 22)
print(sala.temperatura)                   # 22
print(regular(sala, [18, 35, 10, 24]))    # 2
print(sala.temperatura)                   # 24
print(repr(sala))                         # ArCondicionado('sala', 24)

criados = 0
mensagem = "nenhuma"
for inicial in [16, 40, 30]:
    try:
        quarto = ArCondicionado("quarto", inicial)
        criados = criados + 1
    except ValueError as erro:
        mensagem = str(erro)

print(criados)      # 2
print(mensagem)     # temperatura precisa estar entre 16 e 30

print(regular(quarto, [25, 50]))    # 1
print(quarto.temperatura)           # 25

outro_erro = "não"
try:
    regular(sala, [20, "vinte"])    # "vinte" < 16 dá TypeError, não ValueError
except TypeError:
    outro_erro = "sim"
print(outro_erro)                   # sim

print(f"chave: {regular(sala, [16, 31, 30, 15])}-{sala.temperatura}-{criados}-{len(mensagem)}-{quarto.temperatura}-{outro_erro}-{len(repr(quarto))}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-04. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:
#22
#2
#24
#ArCondicionado('sala', 24)
#2
#temperatura precisa estar entre 16 e 30
#1
#25
#sim
#chave: 2-30-2-39-25-sim-28