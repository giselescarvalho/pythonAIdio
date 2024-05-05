class Passaro:
    def voar(self):
        print("voando...")

class Pardal(Passaro):
    def voar(self):
        #return super().voar()
        print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao pode voar")

# FIXME: exemplo ruim de herança
class Aviao(Passaro):
    def voar(self):
        print("Aviao decolando")

#funcao
def plano_voo(obj):
    obj.voar()

#p1 = Pardal()
p2 = Avestruz

plano_voo(Pardal())
plano_voo(p2)
#plano_voo(Aviao())