def pedir_nombre_usuario()->str:  
    """la función pide input al usuario    
    Retorna  nombre(el input) como str """
    nombre=input("nombre del jugador: ")
    return nombre

def elige_estado_de_juego()->str:
    """Pide un input (valor), lo valida si es "s/S" o "n/N".    
     Retorna el valor como str."""
    valor=input("desea jugar? (s/n): \n")
    while valor!="S" and valor!="s" and valor!="N" and valor!="n":
     print("error solo se acepta S/s o N/n")
     valor=input("desea jugar? (s/n): \n")
    
    return valor

def numero_aleatoria_que_no_se_repite(valor:int,lista:list)->bool :
   """Función que comprueba si un número está en una lista.     
      Parámetros:     
      valor: un número (int)  
      lista: lista que se compara.  
      Retorna es_unico (bool)."""
   if valor in lista:
      es_unico=False
   else:
      es_unico=True
      
   return es_unico


def  pregunta(pregun:list,valor:int):
   """Función que muestra los valores de una lista según el índice dado.  
      Parámetros:  
      pregun: lista que contiene las preguntas con campos: "pregunta", "respuesta_a", "respuesta_b", "respuesta_c".  
      valor: número (int) que se usa como índice."""
   print ("pregunta: ",pregun[valor]["pregunta"],"\n","Respuesta a: ",
          pregun[valor]["respuesta_a"],"\n","Respuesta b: ",
          pregun[valor]["respuesta_b"],"\n","Respuesta c: ",
          pregun[valor]["respuesta_c"]
          )

def input_usuario()->str:
   """La función pide input al usuario.    
     Retorna usuario_respuesta (el input) como str."""
   usuario_respuesta=input("elegi tu respuesta (a/b/c): ")
   while usuario_respuesta!="a" and usuario_respuesta!="b" and usuario_respuesta!="c" :
     print("error solo se acepta a/b/c")
     usuario_respuesta=input("elegi tu respuesta (a/b/c): ")
   
   return usuario_respuesta

def comprueba_la_respuesta(pregun:list,valor:int,respuesta:str)->bool:
   """Valida si la respuesta dada por el usuario es igual a "respuesta_correcta" en la lista.    
     Parámetros:
     pregun: lista con preguntas que incluye "respuesta_correcta".       
     valor: número (int) que se usa como índice.   
     respuesta: str que se compara con "respuesta_correcta".  
     Retorna resultado (bool): True o False."""
   if respuesta == pregun[valor]["respuesta_correcta"]:
     resultado=True
   else:
     resultado=False
   
   return resultado



def movimiento(puntero:int,lista:list,dirección:bool)->int:
   """Maneja el movimiento según los parámetros: mueve el puntero positiva o negativamente cierta cantidad.    
      Parámetros:    
      puntero: número (int) que representa la posición del jugador en el tablero.    
      lista: representa el tablero de juego.    
      dirección: bool que indica si el puntero se mueve positivamente o negativamente.  
      Retorna puntero (int) con la posición actualizada."""
   if dirección==True:
      puntero+= 1 + lista[puntero+1]
   else:
      puntero+= (-1 - lista[puntero-1])
   return puntero

def ganaste_o_perdiste(puntero:int)-> str:
   """Función que comprueba el estado del juego según la posición del jugador.  
      Parámetros:  
      puntero: número (int) que representa la posición del jugador en el tablero.  
      Retorna resultado (str): "N" si el juego termina, "s" si continúa."""
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
   """Crea un archivo CSV con el nombre y puntuación del jugador.     
      Parámetros:  
      nombre: str con el nombre elegido por el jugador.   
      posición: int que representa su posición en el tablero (se usa como puntuación)."""
   posision_str=str(posision)
   puntuasion= open("Score.csv","a")
   puntuasion.write("\nNombre del jugador: ")
   puntuasion.write(nombre)
   puntuasion.write("\npuntuasion del jugador: ")
   puntuasion.write(posision_str)

