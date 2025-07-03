#inport
from preguntas import preguntas
from funsiones_s import *
import random
posicion_del_jugador=15
tablero=[0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]
lista_ya_preguntadas=[]

nombre_usuario=pedir_nombre_usuario()
estado_de_juego=elige_estado_de_juego()
hay_preguntas = True 
while (estado_de_juego=="S" or estado_de_juego=="s")and hay_preguntas==True :
 if len(lista_ya_preguntadas) == len(preguntas):
     print("¡Se han terminado las preguntas!")
     estado_de_juego = "N"
     hay_preguntas= False
 else:
  n_preguta=random.randint(0, 14)
  while numero_aleatoria_que_no_se_repite(n_preguta,lista_ya_preguntadas)== False:
   n_preguta=random.randint(0, 14)
  pregunta(preguntas,n_preguta)
  resultado_pregunta=comprueba_la_respuesta(preguntas,n_preguta,input_usuario())
  print("tu respuesta es",resultado_pregunta)
  lista_ya_preguntadas.append(n_preguta)
  posicion_del_jugador=movimiento(posicion_del_jugador,tablero,resultado_pregunta)
  print("tu posision actual es: ",posicion_del_jugador,"\n")
  estado_de_juego=ganaste_o_perdiste(posicion_del_jugador)
  if estado_de_juego=="S" or estado_de_juego=="s":
    estado_de_juego=elige_estado_de_juego()
 
if estado_de_juego=="N" or estado_de_juego=="n" :
 print("tu posision finla es: ",posicion_del_jugador)
 print("Fin del Juego")
 archivos_csv(nombre_usuario,posicion_del_jugador)







