# exemplo anterior com args e kwargs
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('->  faz algo antes de executar')
        funcao(*args, **kwargs)
        print("->  faz algo depois de executar\n                                #")

    return envelope

def ola_mundo():
    print("Olá, mundo!")

@meu_decorador
def ola_mundo(nome): #pode incluir int
    print(f"olá, mundo {nome}!")

ola_mundo("Lia") #, 1000
print("\nFim do primeiro Exemplo\n#############\n")

#######################################
#decorador com argumentos =

import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print('->  faz algo antes de executar')
        resultado = funcao(*args, **kwargs)
        print("->  faz algo depois de executar\n                                #")
        return resultado
    
    return envelope

def ola_mundo():
    print("Olá, mundo!")

@meu_decorador
def ola_mundo(nome, valor_random): 
    print(f"olá, mundo {nome}!")
    return nome.upper()

resultado = ola_mundo("Lia", 100) 
print(resultado)
print(ola_mundo.__name__)
