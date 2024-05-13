import csv
from pathlib import Path

ROOTH_PATH = Path(__file__).parent

# try:
#     with open(ROOTH_PATH / "usuarios.csv", "w", encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["1", "Ana"])
#         escritor.writerow(["2", "Nan"])
# except IOError as exc:
#     print(f"Erro ao abrir {exc}")

# arquivo.close()

try:
    with open(ROOTH_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar arquivo \n     >>>>>>> {exc}")



# https://docs.python.org/3/library/csv.html
# 