# Aula 12 · Exercício 04 (casa, OBRIGATÓRIO): o boletim em texto
#
# Comece o arquivo com:  from pathlib import Path
#
# Aluno: o __init__ recebe nome, nota1 e nota2 e guarda os três.
#   media()          RETORNA a média das duas notas.
#   para_linha()     RETORNA, por exemplo:  Ana;7.0;9.0\n
#   de_linha(linha)  construtor alternativo (@classmethod): as notas voltam como float.
#   __repr__         retorna, por exemplo:  Aluno('Ana', 7.0, 9.0)
#
# salvar(alunos, caminho): grava a lista inteira, um aluno por linha
#   (modo "w", abrindo o arquivo uma vez só).
# carregar(caminho): RETORNA a lista de Aluno. Pule as linhas em branco.
#   Se o arquivo não existir (FileNotFoundError), RETORNA uma lista vazia.
# Nenhum print dentro da classe nem das funções.
#
# Exemplo: salve Aluno('Ana', 7.0, 9.0), Aluno('Bruno', 4.5, 6.0) e
# Aluno('Carla', 8.0, 5.5) em boletim.txt, na mesma pasta deste arquivo
# (Path(__file__).parent / "boletim.txt"). Carregue de volta e, para cada
# aluno, imprima o nome, a média e a situação (Aprovado com média 6 ou mais,
# senão Reprovado):
#   Ana 8.0 Aprovado
#   Bruno 5.25 Reprovado
#   Carla 6.75 Aprovado
# Abra o boletim.txt no VS Code e confira: uma linha por aluno.
#
# Teste você mesmo: no fim do arquivo, salve, carregue e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   de_linha e para_linha .. aula 12, slide 6  https://poo.leoad.com.br/aulas/aula-12/#s6
#   tudo é texto ........... aula 12, slide 5  https://poo.leoad.com.br/aulas/aula-12/#s5
#   gravar a lista ......... aula 12, slide 7  https://poo.leoad.com.br/aulas/aula-12/#s7
#   ler a lista ............ aula 12, slide 8  https://poo.leoad.com.br/aulas/aula-12/#s8
#   linha em branco ........ aula 12, slide 12  https://poo.leoad.com.br/aulas/aula-12/#s12
#   FileNotFoundError ...... aula 11, slide 17  https://poo.leoad.com.br/aulas/aula-11/#s17
#   Path(__file__).parent .. aula 11, slide 19  https://poo.leoad.com.br/aulas/aula-11/#s19
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

from pathlib import Path

class Aluno: 
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
 
 
    def media(self):
        return (self.nota1 + self.nota2) / 2
 
    def para_linha(self):
        return f"{self.nome};{self.nota1};{self.nota2}\n"
 
    @classmethod
    def de_linha(cls, linha):
        nome, nota1, nota2 = linha.strip().split(";")
        return cls(nome, float(nota1), float(nota2))
 
    def __repr__(self):
        return f"Aluno({self.nome!r}, {self.nota1}, {self.nota2})"
 
 
def salvar(alunos, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(aluno.para_linha())
 
 
def carregar(caminho):
    alunos = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if linha.strip() == "":
                    continue
                alunos.append(Aluno.de_linha(linha))
    except FileNotFoundError:
        return []
    return alunos
 
 
# ----- Teste -----
caminho = Path(__file__).parent / "boletim.txt"
 
salvar([Aluno("Ana", 7.0, 9.0), Aluno("Bruno", 4.5, 6.0), Aluno("Carla", 8.0, 5.5)], caminho)
 
for aluno in carregar(caminho):
    situacao = "Aprovado" if aluno.media() >= 6 else "Reprovado"
    print(aluno.nome, aluno.media(), situacao)
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-12. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA: Ana 8.0 Aprovado
# Bruno 5.25 Reprovado
# Carla 6.75 Aprovado
