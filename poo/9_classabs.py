from abc import ABC, abstractmethod, abstractproperty

#extensao de ABC
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):   
        pass 

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    #pass -> erro pois tem dois metodos abstratos
    def ligar(self):
        print("Ligando TV...")
    
    def desligar(self):
        print("Desligando TV...")
        print("TV Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar...")
        print("Ar ligado!")

    def desligar(self):
        print("Desligando Ar...")
        print("Ar Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
print("-------")
controle.desligar()


print("-------")
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

# @abstractmethod