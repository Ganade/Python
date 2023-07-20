url = "https//:bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
# url = " "

# Verifica se a url não é vazia
if url.strip() == "":
    raise ValueError("A URL está vazia")
else:
    print(f'A URL completa é:   {url}')


# Separa base e os parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(f'A URL base é:       {url_base}')
print(f'Os parametros do URL são:  {url_parametros}')

# Busca o valor de um parametro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor: indice_e_comercial]
print(f'E o valor do parametro de busca é: {valor}')
