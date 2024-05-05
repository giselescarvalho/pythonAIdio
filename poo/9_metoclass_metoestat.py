class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def criar_apartir_datanasc(self, ano, mes, dia, nome):
        idade = 2022 - ano
        return Pessoa(nome, idade)

p = Pessoa("Gisele", 20)
print(p.nome, p.idade)



#metodo de classe: de fabrica