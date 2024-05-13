# 'w' : write
arquivo = open("/Users/Gisele/Documents/pythonAIdio/datahora/arquivo/dois.txt", "w")


arquivo.write("Escrevendo dados")

#iteravel tipo string
arquivo.writelines(["\nPython", " --", "version"])

arquivo.close

