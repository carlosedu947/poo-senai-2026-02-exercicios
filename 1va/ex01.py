# 1ª VA · Parte prática · ex01.py: as entregas da lanchonete
#
# Escreva as três classes abaixo, ACIMA do bloco de teste.
#
# 1. Entrega, uma classe abstrata (herda de ABC):
#    - o __init__ recebe cliente e km e guarda os dois;
#    - km é uma property com setter. O setter RECUSA km menor ou igual a 0
#      com raise ValueError("km precisa ser maior que zero") e guarda o
#      valor em self._km. O __init__ passa pelo setter: self.km = km;
#    - frete() é um método abstrato (@abstractmethod);
#    - o __str__ RETORNA um texto como "Ana: 3 km, frete R$ 8.00",
#      usando self.frete(): cada tipo de entrega calcula o seu.
#
# 2. EntregaMoto, filha de Entrega:
#    - frete() RETORNA 5 mais 1 real por km.
#
# 3. EntregaCarro, filha de Entrega:
#    - o __init__ recebe cliente, km e volumes. Ele chama o
#      super().__init__ com cliente e km, e guarda volumes;
#    - frete() RETORNA 10 mais 2 reais por km mais 3 reais por volume.
#
# Não altere o teste. Rode a cada passo e compare a saída com o
# comentário ao lado de cada print.

from abc import ABC, abstractmethod

class Entrega(ABC):
    @abstractmethod
    def frete(self):
        pass

    def __init__(self, cliente, km):
        self._cliente = cliente
        self.km = km
    
    @property
    def cliente (self):
        return self._cliente

    @cliente.setter
    def cliente (self, km):
        if km <= 0:
            raise ValueError("Km precisa ser maior que zero")
        self.km = km
        
    def __str__(self):
        return f"{self.cliente}: {self.km} km, frete R${self.frete()}"
    
class EntregaMoto(Entrega):
    def  frete(self):
        return  5 +1
    
class EntregaCarro(Entrega):
    def __init__(self, cliente, km, volumes):
        super().__init__(cliente, km)
        self.volumes = volumes

    def frete(self):
        return 10 + 2 + 3


# ===== TESTE (não altere estas linhas) =====
e1 = EntregaMoto("Ana", 3)
e2 = EntregaCarro("Bruno", 4, 2)
entregas = [e1, e2]

for e in entregas:
    print(e)
# Ana: 3 km, frete R$ 8.00
# Bruno: 4 km, frete R$ 24.00

total = 0
for e in entregas:
    total = total + e.frete()
print(f"Total: R$ {total:.2f}")        # Total: R$ 32.00

try:
    EntregaMoto("Caio", 0)
except ValueError as erro:
    print(erro)                         # km precisa ser maior que zero

e1.km = 5
print(e1)                               # Ana: 5 km, frete R$ 10.00


class EntregaBicicleta(Entrega):        # esqueceu o frete()
    pass


try:
    EntregaBicicleta("Duda", 2)
except TypeError:
    print("recusada: falta o frete")    # recusada: falta o frete

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta 1va. O nome tem que ser ex01.py.
# ============================================================
# SAÍDA:
