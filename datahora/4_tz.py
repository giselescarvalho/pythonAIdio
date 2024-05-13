#digitar o comando pip :::> install pytz
import pytz
from datetime import datetime

data_am = datetime.now(pytz.timezone('America/Sao_Paulo'))
#Europe/Oslo

print(data_am)