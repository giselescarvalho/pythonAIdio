from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print("\nOslo Time:::>  ",data_oslo, "\nSP Time  :::>  ", data_sp)