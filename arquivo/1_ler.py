# 'r' é opcional, mas para ficar explicito é uma boa prática
arquivo = open("/Users/Gisele/Documents/pythonAIdio/datahora/arquivo/um.txt", "r")

#1: o arquivo todo
#print(arquivo.read())

#2: line
#print("\n\n1a linha: " , arquivo.readline())
#print("\n2a linha: " , arquivo.readline())
#print("\n3a linha: " , arquivo.readline())
#print("\n4a linha: " , arquivo.readline())
#print("\nall linhas: " , arquivo.readlines())


#3: melhor forma de readline - retorna lista de string com todas as linhas do arquivo
#for linha in arquivo.readlines():
#    print(linha, "@@")

#4:
while len(linha := arquivo.readline()):
    print(linha, "##")   

arquivo.close()