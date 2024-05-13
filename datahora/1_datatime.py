from datetime import date, datetime, time

data = date(2024, 5, 10)
print("\n1. Random date: " , data)
print("1. Today:       " , date.today())


#2º import datetime
data_hora = datetime(2024, 7, 10, 10, 30, 30)
print("#\n2. Random datetime:   " , data_hora)
print("2. Today actual time: " , datetime.today())

#3º import time
hora = time(10,20,0)
print("#\n3. Random time:      " , hora)
#nao existe? #print("3. Today actual time: " , time.hour, time.minute)
