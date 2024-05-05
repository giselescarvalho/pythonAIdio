class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
#classe - cls
    @classmethod
    def criar_apartir_datanasc(cls, ano, mes, dia, nome):
       #print(cls)
       idade = 2024 - ano
       return cls(nome, idade)

#estatico
    @staticmethod
    def e_maioridade(idade):
        return idade >= 18

p = Pessoa().criar_apartir_datanasc(1996, 3, 21, "João")
print(p.nome, p.idade)

#metodo de classe: de fabrica - apontam para a classe

#metodo estatico:  utilitarias - nao pode acessar nem modificar o estado
print(Pessoa.e_maioridade(16))
print(Pessoa.e_maioridade(21))