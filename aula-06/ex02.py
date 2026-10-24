# Aula 06 · Exercício 02 (sala): personagens de um jogo
#
# Personagem: o __init__ recebe nome e forca. Guarde a força em self._forca.
#   forca          @property SÓ DE LEITURA (sem setter): RETORNA self._forca.
#                  A força de um personagem não muda depois de criado.
#   ataque()       RETORNA a forca.
#   golpe_duplo()  RETORNA o dobro de self.ataque() (chame o método, não use a forca).
#   __str__        retorna, por exemplo:  Lia (força 10)
#
# Guerreiro é um Personagem. Não precisa de __init__.
#   ataque()  ESTENDE o do pai: o ataque do pai (super().ataque()) mais 5.
#
# Mago é um Personagem com mana:
#   o __init__ recebe nome, forca e mana. Use super().__init__ para nome e forca.
#   ataque()  SUBSTITUI o do pai: retorna mana * 2 (a forca não entra na conta).
#   __str__   ESTENDE o do pai:  Zed (força 3) | mana 20
#
# SE TRAVAR, REVEJA:
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13

class Personagem:
    def __init__(self, nome, forca):
        self.nome = nome
        self._forca = forca

    @property
    def forca(self):
        return self._forca          

    def ataque(self):
        return self.forca

    def golpe_duplo(self):
        return self.ataque() * 2   

    def __str__(self):
        return f"{self.nome} (força {self.forca})"


class Guerreiro(Personagem):
    def ataque(self):
        return super().ataque() + 5     


class Mago(Personagem):
    def __init__(self, nome, forca, mana):
        super().__init__(nome, forca)
        self.mana = mana

    def ataque(self):
        return self.mana * 2            

    def __str__(self):
        return f"{super().__str__()} | mana {self.mana}"   

# ===== TESTE (não altere estas linhas) =====
p = Personagem("Lia", 10)
g = Guerreiro("Tor", 12)
g2 = Guerreiro("Ash", 7)
m = Mago("Zed", 3, 20)
m2 = Mago("Ivy", 5, 7)

print(p, p.ataque())       # Lia (força 10) 10
print(g, g.ataque())       # Tor (força 12) 17
print(g2, g2.ataque())     # Ash (força 7) 12
print(m, m.ataque())       # Zed (força 3) | mana 20 40
print(m2, m2.ataque())     # Ivy (força 5) | mana 7 14
print(g.golpe_duplo())     # 34
print(m.golpe_duplo())     # 80

protegidos = 0
for personagem in [p, g, m]:
    try:
        personagem.forca = 99
    except AttributeError:
        protegidos = protegidos + 1
print(protegidos, g.forca)  # 3 12

print(f"chave: {g.ataque()}-{g2.ataque()}-{m.ataque()}-{m2.ataque()}-{m2.forca}-{m.golpe_duplo()}-{len(str(m))}-{len(str(m2))}-{protegidos}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:Lia (força 10) 10
#Tor (força 12) 17
#Ash (força 7) 12
#Zed (força 3) | mana 20 40
#Ivy (força 5) | mana 7 14
#34
#80
#3 12
#chave: 17-12-40-14-5-80-23-22-3
