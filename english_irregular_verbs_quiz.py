#Créé le 18 Mai 2023
from random import randint
from kandinsky import fill_rect,draw_string
from ion import keydown,KEY_OK,KEY_EXE,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT
from time import sleep

francais=["programmer","mouiller","composer","enfoncer","cracher","répandre","parier","enchérir","diffuser","crever","projeter","coûter","frapper","quitter","débarasser","déchirer","fendre","étendre","couper","blesser","laisser","mettre","lire","fixer","fermer","prévoir","compenser","respecter","(se) courber","saigner","apporter","construire","brûler","acheter","pouvoir","attraper","s'accrocher","ramper","distribuer","creuser","rêver","habiter","nourrir","(se) sentir","se battre","trouver","s'enfuir","lancer","obtenir","moudre","pendre","avoir","entendre","tenir","garder","s'agenouiller","poser","mener","apprendre","laisser","prêter","allumer","perdre","faire","signifier","(se) rencontrer","payer","relayer","déchirer","dire","chercher","vendre","envoyer","briller","chausser","tirer","s'asseoir","dormir","glisser","sentir","aller vite","épeler","dépenser","se tenir debout","tourner","gâcher","coller","piquer","frapper","balayer","se balancer","enseigner","dire","penser","comprendre","pleurer","gagner","enrouler","tordre","battre","devenir","venir","courir","surmonter","survenir","se réveiller","porter","engendrer","commencer","mordre","souffler","casser","choisir","faire","dessiner","boire","conduire","manger","tomber","voler","interdire","prévoir","oublier","pardonner","abandonner","geler","obtenir","donner","aller","grandir","cacher","savoir","mentir","prendre part","sonner","lever(soleil)","voir","secouer","chanter","couler","tuer","parler","surgir","voler","puer","s'efforcer","jurer","gonfler","nager","prendre","déchirer","prospérer","jeter","subir","réveiller","se retirer","écrire"]
infinitif=["preset","wet","typeset","thrust","spit","shed","bet","bid","broadcast","burst","cast","cost","hit","quit","rid","slit","split","spread","cut","hurt","let","put","read","set","shut","forecast","offset","abide","bend","bleed","bring","build","burn","buy","can","catch","cling","creep","deal","dig","dream","dwell","feed","feel","fight","find","flee","fling","get","grind","hang","have","hear","hold","keep","kneel","lay","lead","learn","leave","lend","light","lose","make","mean","meet","pay","relay","rend","say","seek","sell","send","shine","shoe","shoot","sit","sleep","slide","smell","speed","spell","spend","stand","spin","spoil","stick","sting","strike","sweep","swing","teach","tell","think","understand","weep","win","wind","wring","beat","become","come","run","overcome","arise","awake","bear","beget","begin","bite","blow","break","choose","do","draw","drink","drive","eat","fall","fly","forbid","foresee","forget","forgive","forsake","freeze","get","give","go","grow","hide","know","lie","partake","ring","rise","see","shake","sing","sink","slay","speak","spring","steal","stink","strive","swear","swelled","swim","take","tear","thrive","throw","undergo","wake","withdraw","write"]
preterit=["preset","wet","typeset","thrust","spit","shed","bet","bid","broadcast","burst","cast","cost","hit","quit","rid","slit","split","spread","cut","hurt","let","put","read","set","shut","forecast","offset","abode","bent","bled","brought","built","burnt","bought","could","caught","clung","crept","dealt","dug","dreamt","dwelt","fed","felt","fought","found","fled","flung","got","ground","hung","had","heard","held","kept","knelt","laid","led","learnt","left","lent","lit","lost","made","meant","met","paid","relaid","rent","said","sought","sold","sent","shone","shod","shot","sat","slept","slid","smelt","sped","spelt","spent","stood","spun","spoilt","stuck","stung","struck","swept","swung","taught","told","thought","understood","wept","won","wound","wrung","beat","became","came","ran","overcame","arose","awoke","bore","begot","began","bit","blew","broke","chose","did","drew","drank","drove","ate","fell","flew","forbade","foresaw","forgot","forgave","forsook","froze","got","gave","went","grew","hid","knew","lay","partook","rang","rose","saw","shook","sang","sank","slew","spoke","sprang","stole","stank","strove","swore","swelled","swam","took","tore","throve","threw","underwent","woke","withdrew","wrote"]
passe_simple=["preset","wet","typeset","thrust","spit","shed","bet","bid","broadcast","burst","cast","cost","hit","quit","rid","slit","split","spread","cut","hurt","let","put","read","set","shut","forecast","offset","abode","bent","bled","brought","built","burnt","bought","could","caught","clung","crept","dealt","dug","dreamt","dwelt","fed","felt","fought","found","fled","flung","got","ground","hung","had","heard","held","kept","knelt","laid","led","learnt","left","lent","lit","lost","made","meant","met","paid","relaid","rent","said","sought","sold","sent","shone","shod","shot","sat","slept","slid","smelt","sped","spelt","spent","stood","spun","spoilt","stuck","stung","struck","swept","swung","taught","told","thought","understood","wept","won","wound","wrung","beaten","become","come","run","overcome","arisen","awoken","born","begotten","begun","bitten","blown","broken","chosen","done","drawn","drunk","driven","eaten","fallen","flown","forbidden","foreseen","forgotten","forgiven","forsaken","frozen","gotten","given","gone","grown","hidden","known","lain","partaken","rung","risen","seen","shaken","sung","sunk","slain","spoken","sprung","stolen","stunk","striven","sworn","swollen","swum","taken","torn","thriven","thrown","undergone","woken","withdrawn","written"]
h_intro=[32,96,160]
h_jeu=[62,126,190]
difficulte=[26,102,157]
jeu,intro,move,mouv=True,True,True,True
quizz,stop_quizz,stop_jeu=False,False,False
h_p_intro,h_p_jeu=1,0
pause=0.15
blanc,bleu,rouge,vert=(255,255,255),(0,0,255),(220,0,0),(0,180,0)
victoire,defaite=0,0
while jeu:
  new=True
  while intro:
    while new:
      fill_rect(0,0,320,222,blanc)
      draw_string("Facile",130,h_intro[0])
      draw_string("Moyen",135,h_intro[1])
      draw_string("Difficile",115,h_intro[2])
      draw_string("[",90,h_intro[h_p_intro],bleu)
      draw_string("]",220,h_intro[h_p_intro],bleu)
      draw_string("Stop",260,h_jeu[2])
      new=False
    while mouv:
      if keydown(KEY_UP):
        if h_p_intro>0:h_p_intro-=1
        elif h_p_intro==0:h_p_intro=2
        fill_rect(90,h_intro[0],10,h_intro[2]-h_intro[0]+20,blanc)
        fill_rect(220,h_intro[0],10,h_intro[2]-h_intro[0]+20,blanc)
        draw_string("[",90,h_intro[h_p_intro],bleu)
        draw_string("]",220,h_intro[h_p_intro],bleu)
        sleep(pause)
      elif keydown(KEY_DOWN):
        if h_p_intro<2:h_p_intro+=1
        elif h_p_intro==2:h_p_intro=0
        fill_rect(90,h_intro[0],10,h_intro[2]-h_intro[0]+20,blanc)
        fill_rect(220,h_intro[0],10,h_intro[2]-h_intro[0]+20,blanc)
        draw_string("[",90,h_intro[h_p_intro],bleu)
        draw_string("]",220,h_intro[h_p_intro],bleu)
        sleep(pause)
      elif keydown(KEY_OK) or keydown(KEY_EXE):
        intro=False
        quizz=True
        nouveau=True
        sleep(0.3)
        break
      elif keydown(KEY_RIGHT):
        mouv=False
        stop_jeu=True
        nouvo=True
        break
    while stop_jeu:
      while nouvo:
        fill_rect(90,h_intro[0],10,h_intro[2]-h_intro[0]+20,blanc)
        fill_rect(220,h_intro[0],10,h_intro[2]-h_intro[0]+20,blanc)
        draw_string("[",245,h_jeu[2],bleu)
        draw_string("]",305,h_jeu[2],bleu)
        nouvo=False
      if keydown(KEY_OK) or keydown(KEY_EXE):
        stop_jeu=False
        jeu=False
        fill_rect(0,0,320,222,(255,181,59))
        draw_string("Finito !",120,112,rouge)
        sleep(0.3)
        break
      elif keydown(KEY_LEFT):
        stop_jeu=False
        mouv=True
        draw_string("[",90,h_intro[h_p_intro],bleu)
        draw_string("]",220,h_intro[h_p_intro],bleu)
        fill_rect(305,h_jeu[2],10,20,blanc)
        fill_rect(245,h_jeu[2],10,20,blanc)
        break
  while quizz:
    while nouveau:
      nouveau=False
      move=True
      fill_rect(0,0,320,222,blanc)
      verbe=randint(0,difficulte[h_p_intro]-1)
      question=randint(1,4)
      if question==1:
        draw_string("Trouver l'infinitif du verbe",10,10)
        pops=randint(1,3)
        if pops==1:
          draw_string(francais[verbe],10,30)
        elif pops==2:
          draw_string(preterit[verbe],10,30)
        elif pops==3:
          draw_string(passe_simple[verbe],10,30)
        verbes=[randint(0,len(infinitif)-1),randint(0,len(infinitif)-1),randint(0,len(infinitif)-1)]
        bon=randint(0,2)
        for i in range(3):
          if bon==i:
            verbes[i]=verbe
        draw_string(infinitif[verbes[0]],30,h_jeu[0])
        draw_string(infinitif[verbes[1]],30,h_jeu[1])
        draw_string(infinitif[verbes[2]],30,h_jeu[2])
      elif question==2:
        draw_string("Traduire le verbe en francais",10,10)
        draw_string(infinitif[verbe],10,30)
        verbes=[randint(0,len(infinitif)-1),randint(0,len(infinitif)-1),randint(0,len(infinitif)-1)]
        bon=randint(0,2)
        for i in range(3):
          if bon==i:
            verbes[i]=verbe
        draw_string(francais[verbes[0]],30,h_jeu[0])
        draw_string(francais[verbes[1]],30,h_jeu[1])
        draw_string(francais[verbes[2]],30,h_jeu[2])
      elif question==3:
        draw_string("Conjuguer le verbe en anglais",10,10)
        draw_string(infinitif[verbe],10,30)
        verbes=[randint(0,len(infinitif)-1),randint(0,len(infinitif)-1),randint(0,len(infinitif)-1)]
        bon=randint(0,2)
        for i in range(3):
          if bon==i:
            verbes[i]=verbe
        draw_string(preterit[verbes[0]]+", "+passe_simple[verbes[0]],30,h_jeu[0])
        draw_string(preterit[verbes[1]]+", "+passe_simple[verbes[1]],30,h_jeu[1])
        draw_string(preterit[verbes[2]]+", "+passe_simple[verbes[2]],30,h_jeu[2])
      elif question==4:
        draw_string("Retrouver le passé simple de",10,10)
        draw_string(infinitif[verbe],10,30)
        verbes=[randint(0,len(infinitif)-1),randint(0,len(infinitif)-1),randint(0,len(infinitif)-1)]
        bon=randint(0,2)
        for i in range(3):
          if bon==i:
            verbes[i]=verbe
        draw_string(passe_simple[verbes[0]],30,h_jeu[0])
        draw_string(passe_simple[verbes[1]],30,h_jeu[1])
        draw_string(passe_simple[verbes[2]],30,h_jeu[2])
      draw_string("→",10,h_jeu[h_p_jeu],bleu)
      draw_string("Stop",260,h_jeu[2])
      draw_string("Reussi:",250,50,vert)
      fill_rect(250,70,70,20,blanc)
      draw_string(str(victoire),250,70,vert)
      draw_string("Rate:",250,110,rouge)
      fill_rect(250,130,70,20,blanc)
      draw_string(str(defaite),250,130,rouge)
    while move:
      if keydown(KEY_DOWN):
        if h_p_jeu<2:h_p_jeu+=1
        elif h_p_jeu==2:h_p_jeu=0
        fill_rect(10,h_jeu[0],10,h_jeu[2]-h_jeu[0]+20,blanc)
        draw_string("→",10,h_jeu[h_p_jeu],bleu)
        sleep(pause)
      elif keydown(KEY_UP):
        if h_p_jeu>0:h_p_jeu-=1
        elif h_p_jeu==0:h_p_jeu=2
        fill_rect(10,h_jeu[0],10,h_jeu[2]-h_jeu[0]+20,blanc)
        draw_string("→",10,h_jeu[h_p_jeu],bleu)
        sleep(pause)
      elif keydown(KEY_OK) or keydown(KEY_EXE):
        nouveau=True
        fill_rect(0,0,320,222,blanc)
        for i in range(3):
          if h_p_jeu==i:
            if verbe==verbes[i]:
              for i in range(800):
                draw_string("Bravo !",randint(0,285),randint(0,300),(randint(0,255),randint(0,255),randint(0,255)))
              sleep(0.5)
              victoire+=1
              fill_rect(0,0,320,222,(255,)*3)
            else:
              draw_string("Dommage !",115,101,rouge)
              defaite+=1
              sleep(1)
              fill_rect(0,0,320,222,(0,)*3)
            for ht,sl in[[48,francais],[88,infinitif],[116,preterit],[146,passe_simple]]:
              draw_string(str(sl[verbe]),160-5*len(str(sl[verbe])),ht)
            sleep(3)
            move=False
            break
      elif keydown(KEY_RIGHT):
        move=False
        stop_quizz=True
        nouv=True
        break
    while stop_quizz:
      while nouv:
        fill_rect(10,h_jeu[0],10,h_jeu[2]-h_jeu[0]+20,blanc)
        draw_string("[",245,h_jeu[2],bleu)
        draw_string("]",305,h_jeu[2],bleu)
        nouv=False
      if keydown(KEY_OK) or keydown(KEY_EXE):
        stop_quizz=False
        quizz=False
        intro=True
        sleep(0.3)
      elif keydown(KEY_LEFT):
        stop_quizz=False
        move=True
        draw_string("→",10,h_jeu[h_p_jeu],bleu)
        fill_rect(305,h_jeu[2],10,20,blanc)
        fill_rect(245,h_jeu[2],10,20,blanc)
        break
