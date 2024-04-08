curso = "pYthon"

print(curso.upper())
print(curso.lower())
print(curso.title())

print("-------------------")

curso = "  PythoN "

print(curso.strip() + ".")
print(curso.lstrip() + ".")
print(curso.rstrip() + ".")

print("-------------------")

curso = "Python"

print(curso.center(25) + ".")
print(curso.center(9, '#'))
print(curso.center(10, '-'))
print(".".join(curso))
print("_".join(curso))

print("-------------------")
print("-------------------")

nome = "joao"
idade = 50
print(f"Olá, {nome}, sua idade pode ser {idade}")

PI = 3.14159

print(f"Valor de pi: {PI:.2f}")
print(f"Valor de pi: {PI:10.2f}")
print(f"Valor de pi: {PI:.15f}")

print("-------------------")
print("-------------------")

nome = "Edhelzoieth Yatgan Silva"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[-1])
print(nome[-1])
print(nome[::-1])


print("-------------------")
print("-------------------")

nome = "josé"

mensagem = f"""
Olá, seu nome é {nome},
   Está aprendendo Python
"""
print(mensagem)

mensagem = f'''
Olá, seu nome é {nome},
   Está aprendendo Python
 Recuos diferentes nessa mensagem
'''
print(mensagem)