import datetime

datetime.datetime.today()
todayday=datetime.datetime.today().strftime('%Y-%m-%d')
m=datetime.datetime.today().strftime('%Y-%m-')
d=int(datetime.datetime.today().strftime('%d'))-19
d=str(d)
yesterday=m+d

print(yesterday)
print(todayday)
todayday=int(todayday)
yesterday=int(yesterday)
print(todayday-yesterday)