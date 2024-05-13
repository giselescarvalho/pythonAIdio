import os
import shutil
# mais pratico para ler o caminho
from pathlib import Path


ROOT_PATH = Path(__file__).parent
print("## caminho " , ROOT_PATH.parent)


# cria na raiz essa pasta os.mkdir("novo-diretorio")
#arquivo = open("/Users/Gisele/Documents/pythonAIdio/datahora/arquivo/tres.txt", "w")


#depois de usar o ROOTH PATH:
#os.mkdir(ROOT_PATH/"nova-pasta")


#criar arquivo
#arquivo = open(ROOT_PATH/"novo.txt", "w")


#renomear arquivo
#os.rename(ROOT_PATH /"novo.txt", ROOT_PATH/"alterado.yml")


#remover arquivo
#os.remove(ROOT_PATH/"alterado.yml")


#mover de diretorio
shutil.move(ROOT_PATH/'novo.txt', ROOT_PATH/'nova-pasta'/'novo1.txt')



#arquivo = open("novo.txt")