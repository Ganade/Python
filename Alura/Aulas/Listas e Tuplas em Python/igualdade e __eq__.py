class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __str__(self):
        return f"Conta código {self._codigo} e Saldo {self._saldo}"


conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)
print(conta1)
print(conta2)
print(conta1 == conta2)
conta1.deposita(100)
conta2.deposita(110)
print(conta1)
print(conta2)
print(conta1 == conta2)
