#Dados ramdomicos


import random

d1=random.Random()
d2=random.Random()

double=0
rolls= []
for i in range (10):
    a=d1.randrange(1,7)
    b=d2.randrange(1,7)
    i+=1
    rolls.append((a,b))
    print(a,b)
    if a+b ==12:
      print ("Duplol Seis!!!")
      double+=1
print (rolls)
print (double)