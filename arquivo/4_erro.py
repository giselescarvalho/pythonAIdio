from pathlib import Path

ROOTH_PATH = Path(__file__).parent

try:
    #    arquivo = open(ROOTH_PATH/ "novo.y")
    arquivo = open(ROOTH_PATH/ "nova-pasta" / "novo.py")
except FileExistsError as exc:
    print("- - - - -  Arquivo nao encontrado ! - - - - -") 
    print(exc)
except IsADirectoryError as exc:
    print(f"\n--------- Nao foi possivel abrir o arquivo : {exc} -------")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: ---> {exc} <--- ")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc} ####")



#try: 
#    arquivo = open(ROOTH_PATH/"nova-pasta")
#except IsADirectoryError as exp:
#    print(f"\n--------- Nao foi possivel abrir o arquivo : {exp} -------")