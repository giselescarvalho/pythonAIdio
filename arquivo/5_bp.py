## Boas práticas
from pathlib import Path

ROOTH_PATH = Path(__file__).parent


# with garante fechamento do arquivo mesmo em caso de erro
#with open(ROOTH_PATH / "dois.txt", "r") as arquivo:
#        1/0


# verificar se foi aberto com sucesso ou nao
#try: 
#    with open(ROOTH_PATH / "dois.txt", "r") as arquivo:
#        print(arquivo.read)
#except IOError as exc:
#    print(f"Erro ao abrir arquivo:::::::::::::: {exc}")


# certificar de usar a codificacao correta
try: 
    with open(ROOTH_PATH / "um.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir arquivo >>>>>>>\n                       >>>>>> {exc}")
except UnicodeDecodeError as exc:
    print(exc)
