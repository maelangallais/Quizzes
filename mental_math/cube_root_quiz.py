#Créé le 12 Septembre 2023
from random import *

while True:
  p=randint(10,100)
  rc=p**3
  print(" ")
  print("Trouve la racine cubique de");print(rc)
  r=int(input())
  if r==p:
    print("Bravo !")
  else:
    print("Rate sale merde !")
    print("C'était : "+str(p))
