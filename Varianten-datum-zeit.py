import datetime
now = datetime.datetime.now()
datum = [now.year,now.month,now.day,now.hour,now.minute]
print('''Variante 1 = 
import datetime
now = datetime.datetime.now()
datum = [now.year,now.month,now.day,now.hour,now.minute] als Tring Format = ''', datum)


from time import localtime, strftime
now = strftime("%Y-%m-%d %H:%M:%S", localtime())
print('''\nVariante 2 = 
from time import localtime, strftime
now = strftime("%Y-%m-%d %H:%M:%S", localtime())
Datum plus Uhrzeit = ''',now)


import datetime
datetime.date.today()

print('''\nVariante 3 = 
import datetime
datetime.date.today(), nur der genaue Tag = ''',datetime.date.today())