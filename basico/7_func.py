def exibir_mensagem():
    print("olá, mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo, {nome}!")

def exibir_mensagem3(nome="Anonomimo"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem2(nome = "Joao")
exibir_mensagem3()
exibir_mensagem3(nome="Jose")