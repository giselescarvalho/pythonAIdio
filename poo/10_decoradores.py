# passagem de parametro:
def mensagem(nome):
    print("\n")
    print("executando mensagem...")
    return f"OI {nome}"

def mensagem_longa(nome):
    print("\n")
    print("executando mensagem longa...")
    return f"Ola, td bem com vc, {nome}?"

def executar(funcao, nome):
    print("\n")
    print("executando executar...")
    return funcao(nome)

print("\n")
print(executar(mensagem, "JOAO"))
print(executar(mensagem_longa, "JOSEPH"))    
print("\nFim do primeiro Exemplo\n#############\n")

#######################################
# Nesse caso a funcao está dentro do contexto 
#   e nao existe externamente
def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando funcao interna")
    
    def funcao_2():
        print("executando funcao 2")

    funcao_interna()
    funcao_2

principal()
print("\nFim do segundo Exemplo\n#############\n")

#######################################
# retorna funcao

def calcular (operacao):
    def somar(a,b):
        return a+b
    
    def subtrair(a,b):
        return a-b
    
    def mult(a,b):
        return a*b
    
    def dividir(a,b):
        return a/b
    
    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        case "*":
            return mult
        case "/":
            return dividir
        
    

resultado = calcular("+")(1,3)
print("resultado def calcular: ", resultado)
op = calcular("-")
print("resultado subt: ", op(2,2))

print("\nFim do segundo Exemplo\n#############\n")

#######################################
# decorador

def meu_decorador(funcao):
    def envelope():
        print('->  faz algo antes de executar')
        funcao()
        print("->  faz algo depois de executar\n                                #")

    return envelope

def ola_mundo():
    print("Olá, mundo!")

#     propria funcao como argumento
   #####################################
##                                      ## 
## ola_mundo = meu_decorador(ola_mundo) ##
## ola_mundo()                          ##
##                                      ##
   #####################################

# ~ Açúcar Sintático ~ para tirar o bloco de cima
@meu_decorador
def ola_mundo():
    print("olá, mundo!")

ola_mundo() 
    