frutas = ["maça", "laranja", "manga", "pera"]
print(frutas[-1])

print("-------------------")

matriz = [
    [1, "a", 3],
    [2, "z", 4]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])

print("-------------------")

lista = ["p", "y", "t", "h", "o", "n"]

print("2:   ", lista[2:])
print(":2   ", lista[:2])
print("1:3  ", lista[1:3])
print("0:3:2", lista[0:3:2])
print("::   ", lista[::])
print("::-1 ", lista[::-1])

print("-------------------")

for fruta in frutas:
    print(fruta)

for matris in matriz:
    print(matris)

print("-------------------")

numeros = [1,30, 31, 29, 65, 64]
pares = []

for numero in numeros:
    if numero %2 ==0:
        pares.append(numero)
        print(pares)

print("-")

numeros.clear

numeros = [1,30, 31, 29, 65, 64]
pares = [numero for numero in numeros if numero %2 == 0]
print(pares)

print("----")
print("-------------------")

print("-")
lis2 = lista.copy
print(lista)
#lis2[0] = "2"
#print(lis2)

print("-")
lista.extend("2")
#int nao é iteravel
print(lista)
print("-")

print(lista.index("p"))
print(lista.index("h"))
print(lista.index("o"))
print("-")

lista.pop(0)
print(lista)
print("-")

lista.remove("n")
print("remove: ", lista)

lista.reverse()
print(lista)
print("--")

lista.sort()
print(lista)

lista = ["p", "y", "t", "h", "o", "n"]
lista.sort(reverse=True)
print("reverse:", lista)

lista = ["p", "y", "t", "h", "o", "n"]
lista.sort(key=lambda x: len(x))
print("key    :", lista)

lista = ["p", "y", "t", "h", "o", "n"]
lista.sort(key=lambda x: len(x), reverse=True)
print("lambda :", lista)
print("---")

#built in: len e sorted
print(len(lista))

print(sorted(lista, key=lambda x:len(x)))
print(sorted(lista, key=lambda x:len(x), reverse=True))
