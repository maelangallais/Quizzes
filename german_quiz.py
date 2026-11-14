#Créé le 4 Juin 2023
from random import*
from kandinsky import*
from ion import*
from time import *

francais=["maison","marché","coin","jardin","école","banque","hôtel","restaurant","bibliothèque","gare"]
allemand=["Haus","Market","Ecke","Garten","Schule","Bank","Hotel","Restaurant","Bibliothek","Banhof"]
verbes=[0,0,0,0,0,0,0,0,0,0]
axe_x=[10,170]
axe_y=[64,96,128,160,192]
intro=True
rouge,vert,bleu,blanc=(220,0,0),(0,180,0),(0,0,255),(255,255,255)
pause,fin=0.1,0.7
while True:
  while intro:
    intro=False
    fill_rect(0,0,320,222,blanc)
    x_fleche,y_fleche=0,0
    verbe=randint(0,len(francais)-1)
    fr_ou_all=randint(1,2)
    if fr_ou_all==1:
      draw_string("Quel est l'allemand de",10,10)
      draw_string(francais[verbe]+" ?",10,30)
      for i in range(10):
        verbes[i]=randint(0,len(francais)-1)
      bon=randint(0,9)
      verbes[bon]=verbe
      for i in range(5):
        draw_string(allemand[verbes[i]],axe_x[0]+20,axe_y[i])
      for i in range(5):
        draw_string(allemand[verbes[i+5]],axe_x[1]+20,axe_y[i])
    elif fr_ou_all==2:
      draw_string("Quel est le francais de",10,10)
      draw_string(allemand[verbe]+" ?",10,30)
      for i in range(10):
        verbes[i]=randint(0,len(francais)-1)
      bon=randint(0,9)
      verbes[bon]=verbe
      for i in range(5):
        draw_string(francais[verbes[i]],axe_x[0]+20,axe_y[i])
      for i in range(5):
        draw_string(francais[verbes[i+5]],axe_x[1]+20,axe_y[i])
    draw_string("→",axe_x[x_fleche],axe_y[y_fleche],bleu)
  if keydown(KEY_RIGHT):
    if x_fleche==0:x_fleche+=1
    elif x_fleche==1:x_fleche-=1
    fill_rect(10,64,20,148,blanc)
    fill_rect(170,64,20,148,blanc)
    draw_string("→",axe_x[x_fleche],axe_y[y_fleche],bleu)
    sleep(pause)
  elif keydown(KEY_LEFT):
    if x_fleche==1:x_fleche-=1
    elif x_fleche==0:x_fleche+=1
    fill_rect(10,64,20,148,blanc)
    fill_rect(170,64,20,148,blanc)
    draw_string("→",axe_x[x_fleche],axe_y[y_fleche],bleu)
    sleep(pause)
  elif keydown(KEY_DOWN):
    if y_fleche<=3:y_fleche+=1
    elif y_fleche==4:y_fleche=0
    fill_rect(10,64,20,148,blanc)
    fill_rect(170,64,20,148,blanc)
    draw_string("→",axe_x[x_fleche],axe_y[y_fleche],bleu)
    sleep(pause)
  elif keydown(KEY_UP):
    if y_fleche>=1:y_fleche-=1
    elif y_fleche==0:y_fleche=4
    fill_rect(10,64,20,148,blanc)
    fill_rect(170,64,20,148,blanc)
    draw_string("→",axe_x[x_fleche],axe_y[y_fleche],bleu)
    sleep(pause)
  elif keydown(KEY_OK) or keydown(KEY_EXE):
    intro=True
    fill_rect(0,0,320,222,blanc)
    if verbe==verbes[y_fleche+x_fleche*5]:
      draw_string("Bravo !",125,101,vert)
    else:
      draw_string("Dommage !",115,101,rouge)
    sleep(fin)
    sleep(pause)
