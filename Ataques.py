#hecho por rodrigo

import random
import time
print("//////////////////////")
nome = input("cual es tu nombre?\n/////////////////////\n>>>")
pacote = ["Eusebio el putas","Eustaquio el metralletas","El violador de la pradera","Erminijildo el mata pollos"]
print()
print()
print("============================")
print("==bienbenido joven gerrero==")
print("============================")

print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
print("☆☆     {}         ".format(nome))
print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
monstroescolhido = random.choice(pacote)
time.sleep(3)
print()
print()
print()
print()
print()
print()
print(" ==================================")
print(" {} aparecio!".format(monstroescolhido))
print(" ==================================")
jogador = 100
monstro = 100

#ataque

while jogador > 1:
  time.sleep(1)
  print()
  print()
  print("{} vida: {}\n{} vida: {}".format(nome, jogador, monstroescolhido, monstro))
  print(" ")
  time.sleep(1)
  print("================================")
  print("Escoje ataque {}".format(nome))
  print("================================")
  ataque = int(input("[1] Ataque normal\n[2] Ataque especial\n[3] supersalto mortal\n[4] El degollamiento\n[5] Recargar ataque\n>>>"))
  print(" ")
  
  if ataque == 1:
    time.sleep(1)
    print()
    print()
    print()
    print("=============================================")
    print("{} ha hecho 15 de daño!".format(nome))
    print("=============================================")
    monstro = monstro - 15
    time.sleep(1)
    print("{} tiene {} de vida ahora!".format(monstroescolhido, monstro))
    print(" ")
    
  elif ataque == 2:
    time.sleep(1)
    chance = random.randint(1,2)
    
    if chance == 1:
      print("{} ha hecho  35 de daño!".format(nome))
      monstro = monstro - 35
      time.sleep(1)
      print("{} tiene {} de vida ahora!".format(monstroescolhido, monstro))
      print(" ")
      
    else:
      print("{} fallo!".format(nome))
  elif ataque == 3:
    time.sleep(1)
    chance = random.randint(1,3)
    
    if chance == 1:
      print("{} esta callendo del cielo".format(nome))
      time.sleep(2)
      print("{} acaba de caer del cielo y...".format(nome))
      time.sleep(2)
      print("{} ha hecho  45 de daño!".format(nome))
      monstro = monstro - 45
      time.sleep(2)
      print("{} tiene {} de vida ahora!".format(monstroescolhido, monstro))
      print(" ")
    if chance ==2:
      print("{} esta callendo del cielo".format(nome))
      time.sleep(2)
      print("{} acaba de caer del cielo y...".format(nome))
      time.sleep(1)
      print("{} ha fallado el supersalto".format(nome))
    if chance == 3:
      print("{} esta callendo del cielo".format(nome))
      time.sleep(2)
      print("{} acaba de caer del cielo y...".format(nome))
      time.sleep(1)
      print("{} ha fallado el supersalto".format(nome))
      
  elif ataque == 4:
    time.sleep(1)
    chance = random.randint(1,10)
    if chance == 1:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} le ha cortado el cuello a {}!".format(nome,mostroescolhido))
      monstro = monstro - 100
      time.sleep(2)
      print("{} tiene {} de vida ahora!".format(monstroescolhido, monstro))
      print(" ")
    if chance ==2:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))
      print(" ")  
    if chance ==3:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))
    if chance ==4:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))
      print(" ")  
    if chance ==5:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))  
    if chance ==6:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))
      print(" ")  
    if chance ==7:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))
    if chance ==8:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))  
    if chance ==9:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))
      print(" ")  
    if chance ==10:
      time.sleep(2)
      print("{} se ha sacado el cuchillo!".format(nome))
      time.sleep(2)
      print("{} se ha escapadoy {} no la ha podido degollar".format(mostroescolhido, nome))
      
  elif ataque == 5:
    time.sleep(1)
    print("{} Recargo 30 de vida!".format(nome))
    time.sleep(1)
    jogador = jogador + 30
    print("{} tiene {} de vida ahora!".format(nome, jogador))
    
    #Win or lose
    
  if jogador < 1:
    time.sleep(1)
    print("{} perdedor".format(nome))
    time.sleep(2)
    break
    
  elif monstro < 1:
    time.sleep(1)
    print("{} ganador!!".format(nome))
    time.sleep(2)
    break
    
    #ataques
  
  print()
  print(" ")
  print("{} tiempo!".format(monstroescolhido))
  time.sleep(2)
  print(" ")
  
  ataqueinimigo = random.randint(1,5)
  
  if ataqueinimigo == 1:
    print("=======================================================")
    print("{} ha hecho 10 de daño!".format(monstroescolhido))
    print("=======================================================")
    jogador = jogador - 10
    time.sleep(1)
    print("{} tiene {} de vida ahora!".format(nome, jogador))
    print(" ")
  
  elif ataqueinimigo == 2:
    print("=======================================================")
    print("{} ha hecho 15 de daño!".format(monstroescolhido))
    print("=======================================================")
    jogador = jogador - 15
    time.sleep(1)
    print("{} tiene {} de vida ahora!".format(nome, jogador))
    print(" ")
    
  elif ataqueinimigo == 3:
    print("=======================================================")
    print("{} ha hecho 20 de daño!".format(monstroescolhido))
    print("=======================================================")
    jogador = jogador - 20
    time.sleep(1)
    print("{} tiene {} de vida ahora!".format(nome, jogador))
  elif ataqueinimigo == 4:
    print("=======================================================")
    print("{} ha hecho 35 de daño!".format(monstroescolhido))
    print("=======================================================")
    jogador = jogador - 35
    time.sleep(1)
    print("{} tiene {} de vida ahora!".format(nome, jogador))
    print(" ")
    print(" ")
  elif ataqueinimigo == 5:
    print("=======================================================")
    print("{} ha hecho 45 de daño!".format(monstroescolhido))
    print("=======================================================")
    jogador = jogador - 45
    time.sleep(1)
    print("{} tiene {} de vida ahora!".format(nome, jogador))
    print(" ")
    print(" ")
    
  print(" ")
  
  #win or lose 2
  
  if jogador < 1:
    time.sleep(1)
    print("{} perdedor".format(nome))
    time.sleep(2)
    break
    
  elif monstro < 1:
    time.sleep(1)
    print("{} ganador!!".format(nome))
    time.sleep(2)
    break
    
