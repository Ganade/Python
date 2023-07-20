class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


conta_do_gui = ContaCorrente(15)
print(conta_do_gui)
conta_do_gui.deposita(500)
print(conta_do_gui)
conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_da_dani, conta_do_gui]
deposita_para_todas(contas)
for conta in contas:
    print(conta)

guilherme = ('Guilherme', 37, 1981)  # tupla
daniela = ('Daniela', 31, 1987)
usuarios = [guilherme, daniela]
print(usuarios)
usuarios.append(('Paulo', 38, 1980))
print(usuarios)
