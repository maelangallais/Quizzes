#Créé le 10 Janvier 2024
from random import *

mois=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
jour=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
def date(d,m,y):
  if m<3:y,m=y-1,m+12
  day=(d+(13*(m+1))//5+y+y//4-y//100+y//400)%7
  return day
dact,mact,yact=10,1,2024
while True:
  m,y=randint(1,12),randint(0,2100)
  md=30 if m in[4,6,9,11]else 31
  if m==2:md=29 if not y%4 else 28
  d=randint(1,md)
  if d==1:j="1er"
  else:j=d
  if y<yact:v="etait"
  elif y>yact:v="sera"
  else:
    if m<mact:v="etait"
    elif m>mact:v="sera"
    else:
      if d<dact:v="etait"
      elif d>dact:v="sera"
      else:v="est"
  print(" "),print("Quel jour",v,"le",j,mois[m-1],y,"?")
  r,b=int(input("Entrez votre reponse entre 1 et 7 : ")),date(d,m,y)
  if b==0:b=6
  elif b==1:b=7
  else:b-=1
  if r==b:print("Bonne reponse !"),print("Effectivement, le",j,mois[m-1],y,v),print("un",jour[b-1],"!")
  else:print("Mauvaise reponse !"),print("Maheureusement, le",j,mois[m-1],y,v),print("un",jour[b-1],"!")
