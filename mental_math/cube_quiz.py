#Créé le 12 Septembre 2023
from random import *

while True:
  p=randint(10,100)
  rc=p**3
  print(" ")
  print("Trouve le cube de",p)
  r=int(input())
  if r==rc:
    print("Bravo !")
  else:
    print("Rate sale merde !")
