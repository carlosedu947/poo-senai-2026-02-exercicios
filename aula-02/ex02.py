# Aula 02 · Exercício 02 (sala): a classe Aluno
#
# O _init_ recebe nome e notas (uma lista de números) e guarda os dois.
# media()     RETORNA a média das notas: some com um for e divida pela
#             quantidade (len). Se a lista estiver vazia, retorna 0.
# situacao()  RETORNA "Aprovado" se a média for 7 ou mais, senão "Reprovado".
#             Use self.media() aqui dentro, não repita a conta.
# Nenhum print dentro dos métodos.


class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


# ===== TESTE (não altere estas linhas) =====
a1 = Aluno("Ana", [8, 7, 9])
a2 = Aluno("Bruno", [6, 7])
a3 = Aluno("Caio", [7])
a4 = Aluno("Duda", [])

print(a1.nome, a1.media(), a1.situacao())    # Ana 8.0 Aprovado
print(a2.nome, a2.media(), a2.situacao())    # Bruno 6.5 Reprovado
print(a3.nome, a3.media(), a3.situacao())    # Caio 7.0 Aprovado
print(a4.nome, a4.media(), a4.situacao())    # Duda 0 Reprovado

print(f"chave: {a3.nome}-{a3.situacao()}-{a2.media()}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:
#Ana 8.0 Aprovado
#Bruno 6.5 Reprovado
#Caio 7.0 Aprovado
#Duda 0 Reprovado
#chave: Caio-Aprovado-6.5