# idade1 = 39
# idade2 = 30
# idade3 = 27
# idade4 = 18
#
# print(idade1)
# print(idade2)
# print(idade3)
# print(idade4)

idades = [39, 30, 27, 18]
for idade in idades:
    print(idade)
idades_ano_que_vem = [(idade+ 1) for idade in idades]
maior_idades = [idade for idade in idades if idade > 21]
print(maior_idades)
print(idades_ano_que_vem)
idades.append(15)
print(idades)
print(len(idades))
idades.remove(30)
print(idades)
idades.clear()
print(idades)
print(28 in idades)
idades.insert(3, 20)
print(idades)
idades.extend([19, 27, 42])
print(idades)
