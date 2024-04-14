set([1,2,3,1,3,4])

set("abacaxi")
print(set("abacaxi"))

carros = set(("palio", "gol", "celta", "palio"))
print(carros)


print("----------")
numeros = {1,2,3,4}
#nao funciona, nao é possível acessar
##print(numeros[0])
##numeros = list (numeros)
numeros = list (numeros)
print(numeros[0])


print("------For-------")
carros = set(("palio", "gol", "celta", "palio"))
for carro in carros:
    print(carro)


print("------Enumerate-------")
carros = {"palio", "gol", "audi", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


print("--------Union---------")
conj_a =  {1,2}
conj_b = {3,4}

print(conj_a.union(conj_b))
#1,2,3,4


print("----Interesection----")
conja =  {1,2,3}
conjb = {3,4,5}

print(conja.intersection(conjb))
#3


print("------Difference------")
conjua =  {1,2,3}
conjub = {3,4,5}
conjuc = {3,4,6} 

print(conjua.difference(conjub)) #1,2
print(conjub.difference(conjua)) #4,5
print(conjub.difference(conjuc)) #5


print("----Symmetric_Diff----")
conjuna =  {1,2,3}
conjunb = {3,4,5}
print(conjuna.symmetric_difference(conjunb)) #excluiu 3


print("------Issubset------")
conjunta =  {1,2,3}
conjuntb = {3,4,5,1,2,6}

print(conjunta.issubset(conjuntb))
print(conjuntb.issubset(conjunta))
print("-----Issuperset-----") #contrário
print(conjunta.issuperset(conjuntb))
print(conjuntb.issuperset(conjunta))


print("--------Isdisjoint---------")
conjuntoa =  {1,2,3,4,5}
conjuntob = {0,6,7}
conjuntoc = {3,4,6,0}

print(conjuntoa.isdisjoint(conjuntob))
print(conjuntob.isdisjoint(conjuntoc))


print("--------Add---------")
sorteio = {1, 23}

sorteio.add(25)
print(sorteio)
sorteio.add(50)
print(sorteio)
sorteio.add(25)
print(sorteio)

print("----")
#----copy
sorteio
sorteio.copy
print(sorteio)

#----clear
sorteio.clear()
print(sorteio)

#----discard
numeros = {1,2,3,1,3,4,9,0,10,11}
print(numeros)
numeros.discard(1)
print(numeros)
#print(numeros.discard(9)) #Resultado: none
print(numeros)

#----remove
print(numeros.remove(3))
print(numeros)

#----len
print(len(numeros))

#---in
print(0 in numeros)
print(20 in numeros)