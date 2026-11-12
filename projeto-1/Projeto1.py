

class ReservaNaoEncontradaError(Exception):
    def __init__(self, codigo):
        super().__init__(f"Reserva {codigo} não encontrada.")

 
from abc import ABC, abstractmethod
class Quarto(ABC):
    def __init__(self, numero, diaria_base):
        self.numero = numero            # passa pelo setter
        self.diaria_base = diaria_base  # passa pelo setter
 
    @property
    def numero(self):
        return self._numero
 
    @numero.setter
    def numero(self, valor):
        if valor <= 0:
            raise ValueError("O número do quarto deve ser maior que zero.")
        self._numero = valor
 
    @property
    def diaria_base(self):
        return self._diaria_base
 
    @diaria_base.setter
    def diaria_base(self, valor):
        if valor <= 0:
            raise ValueError("A diária base deve ser maior que zero.")
        self._diaria_base = valor
 
    @abstractmethod
    def calcular_diaria(self, noites):
 
        def __str__(self):
            return (f"Quarto {self.numero} ({type(self).__name__}) "
                f"- diária base R$ {self.diaria_base:.2f}")
 
    def __repr__(self):
        return f"{type(self).__name__}({self.numero}, {self.diaria_base})"
 
 
class QuartoSimples(Quarto):
    def calcular_diaria(self, noites):
        return round(self.diaria_base * noites, 2)
 
 
class QuartoSuite(Quarto):
    adcional_hidromassagem = 40.0  
 
    def __init__(self, numero, diaria_base, hidromassagem):
        super().__init__(numero, diaria_base)
        self.hidromassagem = hidromassagem
 
    def calcular_diaria(self, noites):
        valor_noite = self.diaria_base
        if self.hidromassagem:
            valor_noite += self.adcional_hidromassagem
        return round(valor_noite * noites, 2)
 
    def __str__(self):
        extra = "sim" if self.hidromassagem else "não"
        return super().__str__() + f" | hidromassagem: {extra}"
 
 
class QuartoLuxo(Quarto):
    def __init__(self, numero, diaria_base, taxa_servico):
        super().__init__(numero, diaria_base)
        self.taxa_servico = taxa_servico  
 
    def calcular_diaria(self, noites):
        return round(self.diaria_base * noites * (1 + self.taxa_servico), 2)
 
    def __str__(self):
        return super().__str__() + f" | taxa de serviço: {self.taxa_servico:.0%}"
 
 
class Hospede:
    def __init__(self, nome, telefone):
        self.nome = nome  
        self.telefone = telefone
 
    @property
    def nome(self):
        return self._nome
 
    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("O nome do hóspede não pode ser vazio.")
        self._nome = valor.strip()
 
    def __str__(self):
        return f"Hóspede: {self.nome} (tel. {self.telefone})"
 
    def __repr__(self):
        return f"Hospede({self.nome!r}, {self.telefone!r})"
 
 
class Reserva:
    def __init__(self, codigo, hospede, quarto, noites):
        self.codigo = codigo
        self.hospede = hospede
        self.quarto = quarto
        self.noites = noites  
 
    @property
    def noites(self):
        return self._noites
 
    @noites.setter
    def noites(self, valor):
        if valor <= 0:
            raise ValueError("O número de noites deve ser maior que zero.")
        self._noites = valor
 
    def valor_total(self):
        return self.quarto.calcular_diaria(self.noites)
 
    def __str__(self):
        return (f"Reserva #{self.codigo} | {self.hospede.nome} | "
                f"Quarto {self.quarto.numero} | {self.noites} noite(s) | "
                f"R$ {self.valor_total():.2f}")
 
    def __repr__(self):
        return f"Reserva({self.codigo}, {self.hospede!r}, {self.quarto!r}, {self.noites})"
 
 
class Pousada:
    def __init__(self, nome):
        self.nome = nome
        self._reservas = []
 
    def adicionar(self, reserva):
        self._reservas.append(reserva)
 
    def buscar(self, codigo):
        for reserva in self._reservas:
            if reserva.codigo == codigo:
                return reserva
        raise ReservaNaoEncontradaError(codigo)
 
    def total_faturamento(self):
        total = 0
        for reserva in self._reservas:
            total += reserva.valor_total()
        return total
 
    def __str__(self):
        return f"{self.nome} - {len(self._reservas)} reserva(s)"
 
    def __repr__(self):
        return f"Pousada({self.nome!r})"
 
 
#---------------------------------------------------------------
# Teste
#---------------------------------------------------------------
if __name__ == "__main__":
    q1 = QuartoSimples(101, 120.0)
    q2 = QuartoSuite(201, 200.0, True)
    q3 = QuartoLuxo(301, 350.0, 0.10)
 
    print(q1)  # Quarto 101 (QuartoSimples) - diária base R$ 120.00
    print(q2)  # Quarto 201 (QuartoSuite) - diária base R$ 200.00 | hidromassagem: sim
    print(q3)  # Quarto 301 (QuartoLuxo) - diária base R$ 350.00 | taxa de serviço: 10%
 
    print(q1.calcular_diaria(3))  # 360.0
    print(q2.calcular_diaria(2))  # 480.0
    print(q3.calcular_diaria(2))  # 770.0
 
    try:
        Quarto(1, 100.0)
    except TypeError:
        print("Quarto é abstrato: não pode ser instanciado")  
 
    h1 = Hospede("Ana Souza", "62999990001")
    h2 = Hospede("Bruno Lima", "62999990002")
    h3 = Hospede("Carla Dias", "62999990003")
    print(h1)  # Hóspede: Ana Souza (tel. 62999990001)
 
    r1 = Reserva(1, h1, q1, 3)
    r2 = Reserva(2, h2, q2, 2)
    r3 = Reserva(3, h3, q3, 2)
    print(r1)  # Reserva #1 | Ana Souza | Quarto 101 | 3 noite(s) | R$ 360.00
 
    pousada = Pousada("Pousada Sol Nascente")
    print(pousada)  # Pousada Sol Nascente - 0 reserva(s)
 
    pousada.adicionar(r1)
    pousada.adicionar(r2)
    pousada.adicionar(r3)
    print(pousada)  # Pousada Sol Nascente - 3 reserva(s)
 
    print(pousada.buscar(2))  # Reserva #2 | Bruno Lima | Quarto 201 | 2 noite(s) | R$ 480.00
    print(pousada.total_faturamento())  # 1610.0
 
    try:
        pousada.buscar(99)
    except ReservaNaoEncontradaError as erro:
        print(erro)  # Reserva 99 não encontrada.
 
    try:
        QuartoSimples(0, 100.0)
    except ValueError as erro:
        print(erro)  # O número do quarto deve ser maior que zero.
 
    try:
        QuartoSimples(102, -5)
    except ValueError as erro:
        print(erro)  # A diária base deve ser maior que zero.
 
    try:
        Hospede("   ", "62999990004")
    except ValueError as erro:
        print(erro)  # O nome do hóspede não pode ser vazio.
 
    try:
        Reserva(4, h1, q1, 0)
    except ValueError as erro:
        print(erro)  # O número de noites deve ser maior que zero.
 
    q1.diaria_base = 150.0  
    print(q1.calcular_diaria(3))  # 450.0
# ========================================================================
# SAÍDA:
# Quarto 101 (QuartoSimples) - diária base R$ 120.00
# Quarto 201 (QuartoSuite) - diária base R$ 200.00 | hidromassagem: sim
# Quarto 301 (QuartoLuxo) - diária base R$ 350.00 | taxa de serviço: 10%
# 360.0
# 480.0
# 770.0
# Quarto é abstrato: não pode ser instanciado
# Hóspede: Ana Souza (tel. 62999990001)
# Reserva #1 | Ana Souza | Quarto 101 | 3 noite(s) | R$ 360.00
# Pousada Sol Nascente - 0 reserva(s)
# Pousada Sol Nascente - 3 reserva(s)
# Reserva #2 | Bruno Lima | Quarto 201 | 2 noite(s) | R$ 480.00
# 1610.0
# Reserva 99 não encontrada.
# O número do quarto deve ser maior que zero.
# A diária base deve ser maior que zero.
# O nome do hóspede não pode ser vazio.
# O número de noites deve ser maior que zero.
# 450.0
# =============================================================================
