from datetime import date, datetime, time, timedelta
tipo_carro = 'P' #P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
#imports
data_atual = datetime.now()  
#data_atual = datetime.utcnow #pode escolher

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    data_days = data_atual - timedelta(days=tempo_pequeno)
    print(f"\nO carro chegou: {data_atual} e ficará pronto às {data_estimada}\n #\n data days: {data_days}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"\nO carro chegou: {data_atual} e ficará pronto às {data_estimada}\n #")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"\nO carro chegou: {data_atual} e ficará pronto às {data_estimada}\n #")

#
# TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.timedelta'
# print(date.today() - timedelta(days=1))
# print(time(10,19,20) - timedelta(hours=1))   
#
print("\n¨¨¨", date.today() - timedelta(days=1))
resultado = datetime(2024, 7, 25, 10, 19, 20) - timedelta(hours=1)
print("\n@@@ ", resultado.time)

print("\n---", datetime.now().date())