from collections import defaultdict, Counter
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
aparicoes = defaultdict(int)
print(meu_texto)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)

aparicoes2 = Counter(meu_texto.split())
print(aparicoes2)
