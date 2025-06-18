#inport
from preguntas import preguntas
from funsiones_s import *
import random
posision_deljugador=15
tablero=[0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]
lista_ya_preguntadas=[]

nombre_usuario=pedir_nombre_usuario()
estado_de_juego=elige_estado_de_juego()
while estado_de_juego=="S" or estado_de_juego=="s":
 n_preguta=random.randint(0, 14)
 while numero_aleatoria_que_no_se_repite(n_preguta,lista_ya_preguntadas)== False:
  n_preguta=random.randint(0, 14)
  numero_aleatoria_que_no_se_repite(n_preguta,lista_ya_preguntadas)
 #resultado_pregunta=pregunta(preguntas,n_preguta)
 pregunta(preguntas,n_preguta)
 resultado_pregunta=comprueba_la_respuesta(preguntas,n_preguta,tomar_respuesta())
 print("tu respuesta es",resultado_pregunta)
 lista_ya_preguntadas.append(n_preguta)
 posision_deljugador=movimiento(posision_deljugador,tablero,resultado_pregunta)
 print("tu posision actual es: ",posision_deljugador,"\n")
 estado_de_juego=ganaste_o_perdiste(posision_deljugador)
 if estado_de_juego=="S" or estado_de_juego=="s":
    estado_de_juego=elige_estado_de_juego()
 
 
  
if estado_de_juego=="N" or estado_de_juego=="n":
 print("tu posision finla es: ",posision_deljugador)
 print("Fin del Juego")
 archivos_csv(nombre_usuario,posision_deljugador)




#for e_dic in preguntas:
    #print(e_dic)
#print(nombre)