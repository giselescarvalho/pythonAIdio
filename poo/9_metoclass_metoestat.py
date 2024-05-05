class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_datanasc(cls, ano, mes, dia, nome):
       #print(cls)
       idade = 2024 - ano
       return cls(nome, idade)

p = Pessoa().criar_apartir_datanasc(1996, 3, 21, "João")
print(p.nome, p.idade)


#metodo de classe: de fabrica
