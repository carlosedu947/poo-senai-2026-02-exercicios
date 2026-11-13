# Aula 12 · Exercício 03 (sala): a agenda de contatos em JSON
#
# Contato: o __init__ recebe nome, telefone e favorito (com valor padrão False)
# e guarda os três.
#   para_dict()      RETORNA {"nome": ..., "telefone": ..., "favorito": ...}
#   de_dict(dados)   construtor alternativo (@classmethod): recebe um dicionário
#                    como o do para_dict() e RETORNA cls(...) com os três valores.
#   __repr__         retorna, por exemplo:  Contato('Ana', '62 99999-0001')
#
# salvar(contatos, caminho): transforma cada contato num dicionário com para_dict(),
#   junta tudo numa lista e grava a lista no arquivo com
#   json.dump(lista, arquivo, ensure_ascii=False, indent=2)  (modo "w", encoding="utf-8").
# carregar(caminho): lê o arquivo com json.load e RETORNA uma lista de objetos
#   Contato (use Contato.de_dict em cada dicionário).
#   Se o arquivo não existir (FileNotFoundError), RETORNA uma lista vazia.
# Nenhum print dentro da classe nem das funções.
#
# SE TRAVAR, REVEJA:
#   valor padrão ........... aula 05, slide 6  https://poo.leoad.com.br/aulas/aula-05/#s6
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   para_dict e de_dict .... aula 12, slide 23  https://poo.leoad.com.br/aulas/aula-12/#s23
#   salvar a lista ......... aula 12, slide 26  https://poo.leoad.com.br/aulas/aula-12/#s26
#   carregar a lista ....... aula 12, slide 28  https://poo.leoad.com.br/aulas/aula-12/#s28
#   FileNotFoundError ...... aula 11, slide 17  https://poo.leoad.com.br/aulas/aula-11/#s17

import json
from pathlib import Path


class Contato:
    def __init__(self, nome, telefone, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.favorito = favorito
 
    def para_dict(self):
        return {"nome": self.nome, "telefone": self.telefone, "favorito": self.favorito}
 
    @classmethod
    def de_dict(cls, dados):
        return cls(dados["nome"], dados["telefone"], dados["favorito"])
 
    def __repr__(self):
        return f"Contato({self.nome!r}, {self.telefone!r})"
 
 
def salvar(contatos, caminho):
    lista = []
    for contato in contatos:
        lista.append(contato.para_dict())
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)
 
 
def carregar(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return []
    contatos = []
    for item in dados:
        contatos.append(Contato.de_dict(item))
    return contatos


# ===== TESTE (não altere estas linhas) =====
PASTA = Path(__file__).parent

agenda = [
    Contato("Ana", "62 99999-0001", True),
    Contato("Bruno", "62 98888-0002"),
    Contato("Júlia", "62 97777-0003", True),
]
salvar([Contato("Teste", "0")], PASTA / "contatos.json")    # salva uma vez...
salvar(agenda, PASTA / "contatos.json")                     # ...e de novo: substitui
de_volta = carregar(PASTA / "contatos.json")

print(de_volta[0])                              # Contato('Ana', '62 99999-0001')
print(de_volta[2].nome, de_volta[1].favorito)   # Júlia False
print(carregar(PASTA / "nao_existe.json"))      # []

with open(PASTA / "contatos.json", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
print(len(texto))                               # 253

favoritos = 0
for contato in de_volta:
    if contato.favorito:
        favoritos = favoritos + 1

print(favoritos)                                # 2

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-12. O nome tem que ser ex03.py.
#    (O arquivo contatos.json que o programa cria não precisa ser enviado.)
# ============================================================
# SAÍDA:
