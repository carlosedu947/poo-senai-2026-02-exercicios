# Aula 13 · Exercício 01 (sala): o canal que avisa os inscritos
#
# Canal: o __init__ recebe nome, guarda com self e cria duas listas vazias:
#   self.videos = []      (os títulos publicados)
#   self.inscritos = []   (as FUNÇÕES que querem ser avisadas)
#   inscrever(funcao)   guarda a função na lista de inscritos, sem chamar.
#   publicar(titulo)    acrescenta o título em self.videos e depois chama
#                       CADA função inscrita, passando o título.
# As funções celular e email já estão prontas no teste: não mexa nelas.
# Nenhum print dentro da classe.
#
# SE TRAVAR, REVEJA:
#   f × f() ................ aula 10, slide 8  https://poo.leoad.com.br/aulas/aula-10/#s8
#   função em lista ........ aula 13, slide 7  https://poo.leoad.com.br/aulas/aula-13/#s7
#   callback ............... aula 13, slide 29  https://poo.leoad.com.br/aulas/aula-13/#s29
#   Observer ............... aula 13, slide 31  https://poo.leoad.com.br/aulas/aula-13/#s31


class Canal:
    def __init__(self,nome):
        self.nome = nome
        self.videos = []
        self.inscritos = []

    def inscrever(self, funcao):
        self.inscritos.append(funcao)

    def publicar(self,titulo):
        self.videos.append(titulo)

        for i in self.inscritos:
            i(titulo)


# ===== TESTE (não altere estas linhas) =====
avisos = []

def celular(titulo):
    avisos.append("celular: " + titulo)

def email(titulo):
    avisos.append("email: " + titulo)

receitas = Canal("Receitas")
games = Canal("Games")
receitas.inscrever(celular)
receitas.inscrever(email)
games.inscrever(celular)

receitas.publicar("Bolo de cenoura")
games.publicar("Speedrun")
receitas.publicar("Pão de queijo")

print(avisos[0])                                    # celular: Bolo de cenoura
print(avisos[2])                                    # celular: Speedrun
print(len(avisos))                                  # 5
print(receitas.videos)                              # ['Bolo de cenoura', 'Pão de queijo']
print(len(receitas.inscritos), len(games.inscritos), len(games.videos))    # 2 1 1
print(receitas.nome, games.nome)                    # Receitas Games

print(avisos[4])                                    # email: Pão de queijo

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-13. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA:
