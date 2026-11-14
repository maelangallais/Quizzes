#Créé le 5 Mai 2023
from math import *
from random import *

while True:
  s=randint(0,15)
  print("Carre de ",s," ? ")
  r=int(input())
  if r==s**2:
    print("Bravo !")
  else:
    print("Rate sale merde !")
    print(s," au carre = ",s**2)
