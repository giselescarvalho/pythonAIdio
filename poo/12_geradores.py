def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1,2,3]):
    print(i)



#tipos especiais de iteradores, mas nao armazenam todos os valores na memória
#
# no lugar de return utilizam yield