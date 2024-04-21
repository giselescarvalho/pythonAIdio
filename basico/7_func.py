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

#### Args e Kwargs #####
print("-------------")

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sabado, 20 de abril de 2024",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",

    autor="Tim Peters",
    ano=1999,
)

#### Positional #####
print("-------------")

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, "|", ano, "|", placa, "|", marca, "|", motor, "|", combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  


#### Keyword only #####
print("-------------")
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  

#### Hibrido = keyword + pos #####
print("-------------")

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  