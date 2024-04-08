print("Hello world!")

nome = input("informe seu nome: ")
idade = 50

print("olá %s tudo bem? sua idade é %d" % (nome,idade))
print("olá {} tudo bem? sua idade é {}".format(nome,idade))

print("olá {1} tudo bem? sua idade é {2}".format(nome,idade))
print("sua idade é {2}, adorável {1}".format(nome,idade))
