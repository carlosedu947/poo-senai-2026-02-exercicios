# Aula 03 · Exercício 01 (sala): a classe Funcionario
#
# Crie a classe Funcionario.
# O __init__ recebe nome e salario e guarda os dois POR DENTRO, com _ na
# frente: self._nome e self._salario.
# nome           @property só de leitura: RETORNA o nome.
# salario        @property só de leitura: RETORNA o salário.
# salario_anual  @property calculada: RETORNA o salário vezes 13.
# dar_aumento(valor)   soma o valor ao salário (mexa no self._salario).
# Nenhum setter neste exercício: de fora, ninguém grava nome nem salário.


class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @property
    def salario_anual(self):
        return self._salario * 13

    def dar_aumento(self, valor):
        self._salario += valor

# ===== TESTE (não altere estas linhas) =====
f1 = Funcionario("Ana", 3000)
f2 = Funcionario("Bruno", 2500)

print(f1.nome, f1.salario)             # Ana 3000
print(f2.nome, f2.salario_anual)       # Bruno 32500

f2.dar_aumento(500)
print(f2.salario, f2.salario_anual)    # 3000 39000
print(f1.salario == f2.salario)        # True

# Só o teste olha por dentro, para conferir que você guardou com _:
print(f1._nome, f1._salario)           # Ana 3000

print(f"chave: {f1.nome}-{f2.nome}-{f1.salario_anual}-{f2.salario}-{f2.salario_anual}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA -> chave: Ana-Bruno-39000-3000-3900
