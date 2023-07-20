from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"Conta código {self._codigo} e Saldo {self._saldo}"


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other.saldo

    def __str__(self):
        return f"Conta código {self._codigo} e Saldo {self._saldo}"

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._codigo < other._codigo


# conta1 = ContaSalario(37)
# conta2 = ContaSalario(37)
# print(conta1)
# print(conta2)
# print(conta1 == conta2)
# conta1.deposita(100)
# conta2.deposita(110)
# print(conta1)
# print(conta2)
# print(conta1 == conta2)
# ######################################
# conta16 = ContaCorrente(16)
# conta16.deposita(1000)
# conta17 = ContaPoupanca(17)
# conta17.deposita(1000)
# conta18 = ContaInvestimento(18)
# conta18.deposita(1000)
# contas = [conta16, conta17, conta18]
#
# for conta in contas:
#     conta.passa_o_mes()  # Duck typing
#     print(conta)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)
conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(550)
conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)
contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
print(conta_do_guilherme <= conta_da_daniela)

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

for conta in sorted(contas):
    print(f"--{conta}--")
