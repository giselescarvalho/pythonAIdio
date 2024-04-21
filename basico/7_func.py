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

####################
print("-------------")

def retorna_ant_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(retorna_ant_sucessor(100))

####################
print("-------------")

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}|{modelo}/{ano}/{placa}")

salvar_carro("fiat", "palio", "1999", "ABC-1900")
salvar_carro(marca="Audi", modelo="A3", ano="2013", placa="DEF-1800")
salvar_carro(**{"marca": "Chevrolet", "modelo": "xpto", "ano": 2009, "placa": "GHI-17000"})
