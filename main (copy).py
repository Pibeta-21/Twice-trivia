import time
import random
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
puntaje = random.randint(0, 10)
print(MAGENTA+"\nHola"+RESET)
nombre_1 = BLUE+(input("Ingresa tu nombre: ")+RESET)
print("\nHola", nombre_1, "bienvenidx a mi trivia sobre Twice")
print("Con esta trivia pondré a prueba tus conocimientos acerca de este girl group coreano")
print ("Empezarás con", puntaje, "puntos. Trata de alcanzar el mayor puntaje posible")
time.sleep(8)
print("Esto es solo una pizca de kpop que le brindaré a tu día. ¡Comencemos!")
time.sleep(5)
nombre_2 = input("\nPara comenzar, escriba LISTO! o cualquier letra: ")
iniciar_trivia = True
intentos = 0
while iniciar_trivia == True: 
  intentos += 1

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  print("\nEscribe la letra de la alternativa y presiona Enter para enviar tu respuesta")
  
  #Pregunta 1
  print("\n1) ¿En qué año debutaron?")
  print("a) 2016")
  print("b) 2015")
  print("c) 2013")
  print("d) 2014")
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a","b","c","d","x"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_1 == "x":
    print(GREEN+"Atinaste la alternativa secreta: la respuesta es b "+RESET)
    puntaje = puntaje + 20
  if respuesta_1 == "a":
    puntaje = puntaje + 2
    print(YELLOW+"Incorrecto;"+RESET, nombre_1,YELLOW+",ese año debutó Blackpink. Año de las blinks"+RESET)
  elif respuesta_1 == "b":
      print(GREEN+"Así es;"+RESET, nombre_1,GREEN+", One in a million is forever."+RESET)
      puntaje += 10
  elif respuesta_1 == "c":
      print(YELLOW+"Incorrecto;"+RESET, nombre_1,YELLOW+",en este año inició la boyband más reconocida del kpop, BTS"+RESET)
      puntaje += 5 
  elif respuesta_1 == "d":
      print(YELLOW+"Casi cerca;"+RESET, nombre_1,YELLOW+",este año debutaron las Red Velvet"+RESET)
      puntaje += 8
  
  print("\n", nombre_1,"llevas", puntaje,"puntos")
  
  #Pregunta 2
  time.sleep(2)
  print("\n2) Escoge la alternativa donde se mencione tres nombres de las integrantes")
  print("a) Jihyo, Mina, Dahyun")
  print("b) Tzuyu, Jihyo, Wendy")
  print("c) Mina, Dahyun, Yeri")
  print("d) Nayeon, Winter, Mina")
  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "a":
    print(GREEN+"Correcto;"+RESET, nombre_1, GREEN+", Twice es un grupo de 9 chicas así que ahora conoces 1/3 del grupo."+RESET)
    puntaje = puntaje * 2
  elif respuesta_2 == "b":
    print(YELLOW+"Inconrrecto;"+RESET, nombre_1,YELLOW+", Wendy es parte del grupo Red Velvet"+RESET)
    puntaje = puntaje / 2
  elif respuesta_2 == "c":
    print(YELLOW+"Incorrecto;"+RESET, nombre_1,YELLOW+", Yeri es parte del grupo Red Velvet"+RESET)
    puntaje = puntaje - 5
  elif respuesta_2 == "d":
    print(YELLOW+"No, No;"+RESET, nombre_1,YELLOW+", Winter es parte de AESPA"+RESET)
    puntaje = puntaje + 10
  print("\n", nombre_1,"llevas", puntaje,"puntos")
  
  #Pregunta 3
  time.sleep(2)
  print("\n3)¿Cúal es la reciente canción que lanzaron?")
  print("a) What is love")
  print("b) Talk that talk")
  print("c) Feel Special")
  print("d) Breaktrough")
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
    print(YELLOW+"Incorrecto;"+RESET, nombre_1,YELLOW+",esta canción es del año 2018"+RESET)
    puntaje = puntaje - 13
  elif respuesta_3 == "b":
    print(GREEN+"SÍ;"+RESET, nombre_1, GREEN+", este regreso se da después de la renovación de contrato por parte de todas las integrantes"+RESET)
    puntaje = puntaje * 1.5
  elif respuesta_3 == "c":
    print(YELLOW+"Incorrecto;"+RESET, nombre_1,YELLOW+", esta es del 2019"+RESET)
    puntaje = puntaje + 8
  elif respuesta_3 == "d":
    print(YELLOW+"Nada;"+RESET, nombre_1,YELLOW+", esta canción es del mismo año que Feel Special"+RESET)
    puntaje = puntaje / 5
  
  time.sleep(3)
  print (MAGENTA+"\nGracias"+RESET, nombre_1, MAGENTA+"por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)

  time.sleep(3)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  
   print(MAGENTA+"\nEspero"+RESET, nombre_1, MAGENTA+"que lo hayas pasado bien, hasta pronto!"+RESET)
   iniciar_trivia = False 