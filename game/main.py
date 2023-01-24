import random

def elegir_opcion():
  opcions = ("piedra", "papel", "tijeras")
  user_opcion = input("piedra, papel o tijeras => ")
  user_opcion = user_opcion.lower()
  
  if not user_opcion in opcions:
    print("la opcion que eligiste nada que ver por que es", user_opcion)
    return None, None
    #exit() tambien puede servir
    #continue
      
  PC_opcion = random.choice(opcions)
  
  print("user opcion => ", user_opcion)
  print("PC opcion => ",PC_opcion)
  return PC_opcion, user_opcion
  


def check_rules(user_opcion, PC_opcion, user_wins, PC_wins):
  if(user_opcion == PC_opcion):
    print("este es un empate")
  elif user_opcion == "piedra":
    if PC_opcion == "tijeras":
      print("piedra gana a tijeras")
      print("user gano")
      user_wins += 1
    else:
      print("papel gana a piedra")
      print("PC gano")
      PC_wins += 1
  elif user_opcion == "papel":
    if PC_opcion == "piedra":
      print("papel gana a piedra")
      print("user gano")
      user_wins += 1
    else:
      print("tijeras gana a papel ")
      print("PC gano")
      PC_wins += 1
  elif user_opcion == "tijeras":
    if PC_opcion == "papel":
      print("tijeras gana a papel")
      print("user gano")
      user_wins += 1
    else:
      print("piedra gana a tijeras")
      print("PC gano")
      PC_wins += 1
  return user_wins, PC_wins

def final_result(user_wins, PC_wins):
  #aqui estoy sacando las victorias pero al mismo tiempo reinicio el bucle si el jugador lo desea
    if PC_wins == 3:
      print(f"PC gano con {PC_wins} ganados")
      exi = input("¿deseas jugar de nuevo? (s/n) => ")
      if exi == "s":
        rounds = 0
        PC_wins = 0
        user_wins = 0
        print("Ronda",rounds)
      else:
        exit()
  #aqui estoy sacando las victorias pero al mismo tiempo reinicio el bucle si el jugador lo desea
    if user_wins == 3:
      print(f"user gano con {user_wins} wins")
      exi = input("¿deseas jugar de nuevo? (s/n) => ")
      if exi == "s":
        rounds = 0
        PC_wins = 0
        user_wins = 0
        print("            NUEVA PARTIDA")
      else:
        exit()
        
    return user_wins, PC_wins
        
def run_game():
  PC_wins = 0
  user_wins = 0
  rounds = 1

  while True:
  
    print("*" * 10)
    print("Ronda",rounds)
    print("*" * 10)
  
    print("PC_Wins:", PC_wins)
    print("User_Wins:", user_wins)
    #el contador de rounds 
    rounds += 1
    user_opcion, PC_opcion = elegir_opcion()
    user_wins, PC_wins = check_rules(user_opcion, PC_opcion, user_wins, PC_wins)
    user_wins, PC_wins = final_result(user_wins, PC_wins)
        
  
run_game()