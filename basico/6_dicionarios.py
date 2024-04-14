pessoa = {"nome": "Guilherme", "idade": 28}
#chave e valor

pessoa = dict(nome="Guilherme", idade = 28)
pessoa["telefone"] = "333-1234"
print(pessoa)


print("------------------")
dados = {"nome": "Guilherme", 'idade': 28, 'telefone': '333-1234'}
dados["nome"]="Maria"
print(dados)


print("------------------")
contatos = {
    "guilherm@gmail.com": {"nome": "Guilherme", "idade": 28},
    "giovanna@gmail.com": {"nome": "Giovanna", "idade": 27},
    "vitor@gmail.com": {"nome": "Vitor", "idade": 26, "telefone": "333+124"}
}

print(contatos["vitor@gmail.com"]) #{'nome': 'Vitor', 'idade': 26, 'telefone': '333+124'}
print(contatos["vitor@gmail.com"]["idade"]) #26

print("---")
for chave, valor in contatos.items():
    print(chave,valor)


#-----copy
print("---")
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gyui"}

print(copia)

#-----fromkeys
print("---")
contatos = {
    "giovanna@gmail.com": {"nome": "Giovanna", "idade": 27}
}
dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "telefone"], "vazio")
print(contatos)

#-----get
print("---")
contatos = {
    "guilherm@gmail.com": {"nome": "Guilherme", "idade": 28}
}

print(contatos.get("chave")) #none
print(contatos.get("guilherm@gmail.com"))
print(contatos.get("chave", {})) #default: {}

#-----keys
print("---")
clientes = {"id": 1, "nome": "Joao", "idade": 20}
print(clientes.keys()) #chaves do dicionario

#-----pop
clientes = {1: {"nome": "Joao", "idade": 20},
            2: {"nome": "Jose", "idade": 27}
            }
print(clientes)
clientes.pop(1, {})
print(" -- -- -- ", clientes)

#-----popitem
clientes = {1: {"nome": "Joao", "idade": 20},
            3: {"nome": "Jose", "idade": 22}
            }

print(clientes.popitem())
print(clientes.popitem())
# print(clientes.popitem()) #error


#-----setdefault
client = {"nome": "Giovanne", "idade": 27}
client.setdefault("nome", "Giovanni")
print(client)

#-----values
print("------------------")
contatos = {
    "guilherm@gmail.com": {"nome": "Guilherme", "idade": 28},
    "giovanna@gmail.com": {"nome": "Giovanna", "idade": 27},
    "vitor@gmail.com": {"nome": "Vitor", "idade": 26, "telefone": "333+124"}
}


#-----del
del contatos["giovanna@gmail.com"]
print(contatos)

del contatos
print(contatos)
