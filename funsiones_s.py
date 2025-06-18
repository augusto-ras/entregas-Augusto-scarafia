
def pedir_nombre_usuario()->str:
    nombre=input("nombre del jugador: ")
    return nombre

def elige_estado_de_juego()->str:
    valor=input("desea jugar? (s/n): \n")
    while valor!="S" and valor!="s" and valor!="N" and valor!="n":
     print("error solo se acepta S/s o N/n")
     valor=input("desea jugar? (s/n): \n")
    
    return valor

def numero_aleatoria_que_no_se_repite(valor:int,lista:list)->int :
   if valor in lista:
      es_unico=False
   else:
      es_unico=True
      
   return es_unico


def  pregunta(pregun:list,valor:int):
   print ("pregunta: ",pregun[valor]["pregunta"],"\n","Respuesta a: ",
          pregun[valor]["respuesta_a"],"\n","Respuesta b: ",
          pregun[valor]["respuesta_b"],"\n","Respuesta c: ",
          pregun[valor]["respuesta_c"]
          )

def tomar_respuesta()->str:
   usuario_respueta=input("elegi tu respuesta: (a/b/c): ")
   return usuario_respueta

def comprueba_la_respuesta(pregun:list,valor:int,respuesta:str)->float:
   if respuesta == pregun[valor]["respuesta_correcta"]:
     resultado=True
   else:
     resultado=False
   
   return resultado



def movimiento(puntero:int,lista:list,direcsion:bool)->int:
   if direcsion==True:
      puntero+= 1 + lista[puntero+1]
   else:
      puntero+= (-1 - lista[puntero-1])
   return puntero

def ganaste_o_perdiste(puntero:int)-> str:
   if puntero==30:
      print("ganador")
      resultado="N"
   elif puntero == 0:
      print("perdedor")
      resultado="N"
   else:
      resultado="s"
   return resultado

def  archivos_csv(nombre:str,posision:int):
   posision_str=str(posision)
   puntuasion= open("Score.csv","w")
   puntuasion.write("Nombre del jugador: ")
   puntuasion.write(nombre)
   puntuasion.write("\npuntuasion del jugador: ")
   puntuasion.write(posision_str)
