frutas = ("p", "y", "t", "h", "o", "n",)

letras = tuple("python")

numeros = tuple(("pyt", "hon"))

pais = ("Brasil")

print(frutas, pais, letras, numeros)
print("-------------------")

cores = ("vermelho", "azul", "verde", "azul")
cores.count("vermelho")
cores.count("azul")

#tupla nao suporta atribuição de itens
print("-------------------")

carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print("-------------------")

linguagens = ("python", "js", "java", ".net",)

print(linguagens.index("java"))
print(linguagens.index(".net"))
print("---")
print(len(linguagens))