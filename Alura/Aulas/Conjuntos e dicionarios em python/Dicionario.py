aparicoes = {
    "guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}
print(aparicoes["cachorro"])
print(aparicoes)
aparicoes["Calos"] = 1
print(aparicoes)
del aparicoes["Calos"]
print(aparicoes)
print("Carlos" in aparicoes)
for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)
