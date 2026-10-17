# Aula 04 · Exercício 01 (sala): o desconto que se recusa
#
# O __init__ do Ingresso já está pronto. Faltam dois métodos.
#
# __str__  RETORNA, por exemplo:  Show · R$ 80.00   (o preço com :.2f)
#
# com_desconto(porcentagem):
# - se a porcentagem for menor que 0 OU maior que 100, LEVANTE (raise):
#       ValueError("desconto precisa estar entre 0 e 100")
# - senão, RETORNE o preço com o desconto: preco - preco * porcentagem / 100
#
# 0 e 100 são válidos (0 = preço cheio, 100 = de graça).
# Nada de print nem de return None no lugar do raise.
#
# SE TRAVAR, REVEJA:
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10


class Ingresso:
    def __init__(self, evento, preco):
        self.evento = evento
        self.preco = preco

    
    def __str__(self): 
            return f"{self.evento} · R$ {self.preco:.2f}"  
    
    def com_desconto(self, porcentagem):
        if porcentagem < 0 or porcentagem > 100:
            raise ValueError("Desconto precisa estar entre 0 e 100")
        return self.preco - self.preco * porcentagem / 100


# ===== TESTE (não altere estas linhas) =====
show = Ingresso("Show", 80)
print(show)                      # Show · R$ 80.00
print(show.com_desconto(25))     # 60.0
print(show.com_desconto(100))    # 0.0

resultados = []
recusados = 0
mensagem = "nenhuma"
for porcentagem in [50, -10, 0, 120]:
    try:
        resultados.append(show.com_desconto(porcentagem))
    except ValueError as erro:
        resultados.append("recusado")
        recusados = recusados + 1
        mensagem = str(erro)

print(resultados)    # [40.0, 'recusado', 80.0, 'recusado']
print(mensagem)      # desconto precisa estar entre 0 e 100

print(f"chave: {recusados}-{show.com_desconto(10)}-{len(mensagem)}-{len(str(show))}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-04. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA: