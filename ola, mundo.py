print("Hello world!")

nome = input("informe seu nome: ")
idade = 50

print("olá %s tudo bem? sua idade é %d" % (nome,idade))
print("olá {} tudo bem? sua idade é mais ou menos {}".format(nome,idade))

print(f"Olá, {nome}, sua idade pode ser {idade}")

nome = "joao"

print("olá, {nome}, sua idade é {idade}".format(nome=nome, idade=idade))

print("olá, seu nome é {nome}, e sua idade é {idade}".format(**pessoa))

print("olá {1} tudo bem? sua idade é {2}".format(nome,idade))
print("sua idade é {2}, adorável {1}".format(nome,idade))

