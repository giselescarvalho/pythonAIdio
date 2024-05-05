class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Gisele", 1)
aluno2 = Estudante("Giovana",2)
mostrar_valores(aluno1,aluno2)

print("----------------")
aluno1.matricula = 3
print(aluno1, "#")
print(aluno2)

print("----------------")
Estudante.escola = "Python"
print(aluno1, "##")
print(aluno2, "##")

