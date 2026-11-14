#Créé le 5 Mai 2023
from math import *
from random import *

while True:
  s=randint(15,100)
  print("Racine carree de ",s**2," ? ")
  r=int(input())
  if r==s:
    print("Bravo !")
  else:
    print("Rate sale merde !")
    print("Racine carree de ",s**2," = ",s)
