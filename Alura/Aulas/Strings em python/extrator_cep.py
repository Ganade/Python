import re  # Regular Expression -- ReqEx

endereco = "Rua das flores 72, Apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

# 5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}-?[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
