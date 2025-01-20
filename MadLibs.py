#El codigo crea un programa de Madlibs, dónde el usuario debe ingresar diferentes partes faltantes en un parrafo para personalizar el estilo de una historia predefinida

import time
import random

#Solicitamos el nombre al jugador

jugador = input("Ingresa tu nombre: ")

#Le damos un mensaje de bienvenida

bienvenida = f"¡Hola {jugador}! ¡Vamos a jugar juntos!"
print(bienvenida)

time.sleep(1.5)

#Le damos las instrucciones dónde debe elegir la tematica del texto a completar

while True:
  
  instrucciones = input("""Ahora deberas elegir alguna de las temáticas siguientes para jugar a completar una minihistoria:
    1. Aventura en el espacio
    2. Misterio en la montaña
    3. Desafio medieval
    4. Agente secreto
    5. Salir del juego

    Ingresa el numero correspondiente a la opcion que deseas: """)
  
  #Validamos que la opcion ingresada sea un numero correcto

  try:  
    instrucciones = int(instrucciones)
    if instrucciones == 1 or instrucciones == 2 or instrucciones == 3 or instrucciones == 4:
      break

    elif instrucciones == 5:
      time.sleep(2)
      mensaje = f"¡Te esperamos en otro momento {jugador}!"
      print(mensaje)
      time.sleep(2)
      exit()
    else:
      print("El numero ingresado debe ser 1, 2, 3 o 4")
  except ValueError:
    print("El valor ingresado debe ser un numero")

#Imprimimos un mensaje para indicarle al jugador que debera prepararse para completar la historia

time.sleep(2)
mensaje = f"\nExcelente elección {jugador}. Voy a pedirte algunos detalles para poder completar la historia.\n"
print(mensaje)
time.sleep(2)


#Definimos una funcion para convertir los verbos ingresados para ser reutilizados en diferente tiempo luego

def verboGerundio(verbo):
  if verbo.endswith("ar"):
    return verbo[:-2] + "ando"  # Eliminar "ar" y añadir "ando"
  elif verbo.endswith("er") or verbo.endswith("ir"):
    return verbo[:-2] + "iendo"  # Eliminar "er/ir" y añadir "iendo"
  else:
    return verbo  # Si no es un verbo regular, lo devuelve tal cual

#Desarrollamos las diferentes historias de acuerdo a la opcion elegida por el usuario

if instrucciones == 1: #AVENTURA EN EL ESPACIO
  nombre = input("Nombre del astronauta: ")
  planeta = input("Nombre de un planeta: ")
  objeto = input("Un objeto extraño: ")
  adjetivo = input("Un adjetivo: ")
  criatura = input("Una criatura alienígena: ")
  actividad = input("Una actividad: ")
  exclamacion = input("Una exclamación: ")
  

  # Ajustar el verbo para estar en gerundio
  
  verbo_gerundio = verboGerundio(actividad)
  
  historia = f"""El astronauta {nombre} fue enviado en una misión de exploración al remoto planeta {planeta}. Todo parecía ir bien hasta que tropezó con un {objeto.lower()} que era muy {adjetivo.lower()}.Intrigado, {nombre} decidió investigar más, pero justo entonces apareció un {criatura.lower()} gigante que estaba {verbo_gerundio.lower()} en medio del camino. ¡El universo nunca es tan fácil deexplorar!"""
  
  #Mostrar historia inicial

  print("\nTu historia espacial empieza así:\n")
  time.sleep(1)
  for linea in historia.split("\n"):
    print(linea)
    time.sleep(0.5)
  time.sleep(1.5)

  # Primer punto de decisión: La criatura aparece

  print("\n¡Ups! Aparece una criatura alienígena gigante. ¿Qué debería hacer el astronauta?")
  time.sleep(1.5)
  print("1. Hablar con la criatura.")
  time.sleep(1)
  print("2. Intentar escapar.")
  time.sleep(1)
  print("3. Usar el objeto extraño para defenderse.")
  time.sleep(1)
  
  # Obtener la elección del jugador 
  
  eleccion = input("Ingresa el número de tu elección: ")

  # Decisiones y ramificaciones de la historia
  if eleccion == "1":
    historia += f"\n\n{nombre} decidió hablar con la criatura. Para su sorpresa, la criatura no era hostil, sino que tenía una gran habilidad para contar chistes malos. "
    historia += f"Cada vez que {nombre} le preguntaba algo, la criatura respondía con: '¿Por qué cruzó el astronauta la galaxia? ¡Para llegar al otro planeta!'"
    historia += f" {nombre} no sabía si reír o llorar, pero decidió seguir adelante con la misión, buscando una respuesta más seria."
  elif eleccion == "2":
    historia += f"\n\n{nombre} decidió escapar rápidamente. Corrió hacia su nave espacial, pero un campo gravitacional extraño lo hizo caer y rodar por el suelo como si fuera una bola de tenis. "
    historia += f"Al final, se dio cuenta de que la criatura solo quería ayudarlo a salir del planeta. ¡Y él se había escapado de un amigo potencial!"
  elif eleccion == "3":
    historia += f"\n\n{nombre} usó el objeto extraño para defenderse. Para su sorpresa, el objeto comenzó a brillar como una lámpara de fiesta y la criatura se calmó al instante. "
    historia += f"El objeto resultó ser una especie de comunicador intergaláctico, ¡y la criatura empezó a recitar poesía de la antigua civilización alienígena!"
  else:
    historia += f"\n\n{nombre} no sabía qué hacer y quedó paralizado. La criatura se acercó lentamente, pero, por suerte, no era peligrosa. "
    historia += f"Al final, la criatura le dio un abrazo y le ofreció una taza de té. ¡Parecía más un ser manso que un monstruo galáctico!"

  # Mostrar la historia después del primer punto de 
  time.sleep(1.5)
  print("\nHistoria después de tu elección:")
  time.sleep(1.5)
  print(historia)

  # Segundo punto de decisión: Explorar el planeta
  time.sleep(1.5)
  print(f"\nAhora, {nombre} debe decidir cómo proceder.")
  print("1. Explorar el planeta con la criatura.")
  print("2. Regresar a la nave y seguir su misión original.")
    
  eleccion2 = input("Ingresa el número de tu elección: ")
  time.sleep(1.5)
  
  if eleccion2 == "1":
    historia += f"\n\n{nombre} decidió explorar el planeta con la criatura. Juntos descubrieron un antiguo templo oculto en las montañas, donde, para sorpresa de {nombre},"
    historia += f" la criatura comenzó a bailar en círculos como si estuviera en una fiesta intergaláctica. Después de una serie de pruebas, {nombre} logró desbloquear un secreto que cambiaría el futuro de la humanidad."
    historia += f" ¡Y todo gracias a los movimientos de baile de la criatura!"
  elif eleccion2 == "2":
    historia += f"\n\n{nombre} decidió regresar a su nave para seguir con la misión original. A pesar de la extraña experiencia, {nombre} completó con éxito la misión, "
    historia += f"pero nunca olvidó lo que ocurrió en el planeta {planeta}. ¡Y, para su sorpresa, encontró una pizza en su nave que apareció de la nada! ¡El universo tiene sus misterios!"
  else:
    historia += f"\n\n{nombre} no pudo decidir y pasó mucho tiempo pensando. Mientras tanto, el planeta continuaba ofreciendo misterios y secretos por descubrir, como una enorme estatua de {criatura.lower()} que tenía un sombrero gigante. "
    historia += f"¡Nada aburrido en este planeta, eso es seguro!"

  # Mostrar la historia después de la segunda decisión

  print("\nHistoria después de tu segunda elección:")
  print(historia)

  # Tercer punto de decisión: El descubrimiento
  print(f"\nMientras explora, {nombre} descubre algo impresionante. ¿Qué hará con este nuevo hallazgo?")
  print("1. Estudiarlo y tratar de entender su función.")
  print("2. Llevarlo de vuelta a la nave para investigarlo más tarde.")
  print("3. Destruirlo por miedo a que sea peligroso.")
    
  eleccion3 = input("Ingresa el número de tu elección: ")
  
  if eleccion3 == "1":
    historia += f"\n\n{nombre} decidió estudiar el objeto. Resultó ser una tecnología avanzada que permitió crear una nueva fuente de energía renovable."
    historia += f" Pero, para sorpresa de {nombre}, también tenía una función extra: ¡podía hacer que cualquier ser humano bailara sin parar! Esto cambió la historia de la humanidad, pero no sin antes causar una serie de incidentes incómodos en la NASA."
  elif eleccion3 == "2":
    historia += f"\n\n{nombre} decidió llevar el objeto de vuelta a la nave. Los científicos a bordo lo estudiaron y descubrieron que podría ser una clave para la colonización de nuevos planetas. "
    historia += f"Lo primero que hicieron con el objeto fue programarlo para tocar música de jazz todo el tiempo. ¡El espacio nunca fue tan rítmico!"
  elif eleccion3 == "3":
    historia += f"\n\n{nombre} destruyó el objeto por miedo. Más tarde, se dio cuenta de que había cometido un gran error. Sin el objeto, la humanidad perdió una oportunidad de cambiar su futuro. "
    historia += f"Y, peor aún, se dio cuenta de que el objeto había sido un regalo de cumpleaños del presidente de los alienígenas. ¡La vergüenza fue universal!"
  else:
    historia += f"\n\n{nombre} se quedó indeciso frente al objeto. Finalmente, decidió dejarlo donde lo encontró, pero nunca dejó de preguntarse qué podría haber sido. "
    historia += f"Eventualmente, el objeto se volvió muy famoso entre los coleccionistas de arte alienígena, pero {nombre} aún se pregunta si debería haberlo tocado."

  # Mostrar la historia después de la tercera decisión
  time.sleep(1.5)
  print("\nHistoria después de tu tercera elección:")
  print(historia)

  # Cuarto punto de decisión: El regreso
  time.sleep(1.5)
  print(f"\nEs hora de regresar a la nave. ¿Qué hará {nombre} ahora?")
  print("1. Regresar inmediatamente para contar su descubrimiento.")
  print("2. Continuar explorando en busca de más secretos.")
  print("3. Quedarse en el planeta y comenzar una nueva vida.")
    
  eleccion4 = input("Ingresa el número de tu elección: ")
  
  if eleccion4 == "1":
    historia += f"\n\n{nombre} regresó a la nave y contó su descubrimiento. La humanidad comenzó una nueva era de exploración espacial, "
    historia += f"y {nombre} fue recordado como uno de los pioneros más importantes de la historia. Pero aún así, la gente no podía dejar de preguntarse por qué la criatura alienígena había sido tan buena bailarina."
  elif eleccion4 == "2":
    historia += f"\n\n{nombre} decidió seguir explorando. Durante semanas, descubrió nuevos misterios, pero nunca regresó a la nave. "
    historia += f"Su nombre se convirtió en leyenda entre los viajeros del espacio, y su historia sobre el baile de las criaturas alienígenas pasó a ser un tema de culto."
  elif eleccion4 == "3":
    historia += f"\n\n{nombre} decidió quedarse en el planeta. Con el tiempo, estableció una nueva colonia y se convirtió en el líder de una nueva civilización intergaláctica. "
    historia += f"Pero lo más importante de todo es que {nombre} fue recordado como el primer humano en enseñar a los alienígenas a hacer una coreografía sincronizada."
  else:
    historia += f"\n\n{nombre} dudó sobre qué hacer y se quedó atrapado en el planeta, buscando respuestas en su propio corazón. Sin embargo, durante su reflexión, "
    historia += f"descubrió que el verdadero viaje era entender el sentido de la vida... y también encontrar más criaturas bailando."

  # Mostrar la historia final
  time.sleep(1.5)
  print("\nHistoria final:")
  print(historia)

elif instrucciones == 2: #MISTERIO EN LA MONTAÑA

  nombre = input("Nombre del protagonista: ")
  adjetivo = input("Un adjetivo: ")
  animal = input("Un animal misterioso: ")
  ruido = input("Un ruido extraño: ")
  objeto = input("Un objeto perdido: ")
  actividad = input("Una actividad: ")

  # Ajustar el verbo para estar en gerundio
  verbo_gerundio = verboGerundio(actividad)


  historia = f"""Era una noche {adjetivo.lower()} en las montañas, y {nombre} estaba buscando su preciado {objeto.lower()}. 
  Mientras lo buscaba, escuchó un {ruido.lower()} que hizo que se le erizara la piel. 
  Al girarse, {nombre} vio un {animal.lower()} que, para su sorpresa, ¡estaba {verbo_gerundio.lower()} con el {objeto.lower()}!

  "{ruido.capitalize()}!", exclamó {nombre}, que no sabía si estar asustado o reírse. 
  Decidió seguir al {animal.lower()} mientras intentaba convencerlo de devolverle su {objeto.lower()}. 
  Finalmente, tras varias horas de negociación (y un poco de {actividad.lower()} por su parte para ganar confianza), 
  {nombre} recuperó su {objeto.lower()}. Aunque, claro, nadie en el pueblo le creyó la historia del {animal.lower()}.
  """

  # Imprimimos un mensaje para presentar la historia
  time.sleep(2)
  print("\nTu historia de misterio:")
  time.sleep(2)
  print(historia)

elif instrucciones == 3: #DESAFIO MEDIEVAL
  caballero = input("Nombre del caballero o caballera: ")
  arma = input("Un arma medieval: ")
  criatura = input("Una criatura mágica: ")
  verbo = input("Un verbo en infinitivo: ")
  adjetivo = input("Un adjetivo: ")
  manjar = input("Un manjar medieval: ")


  # Pluralizar el manjar si es necesario (agrega una 'es' o una 's' según la palabra)
  if manjar.endswith("z"):
    manjar_plural = manjar[:-1] + "ces"  # Ejemplo: "luz" -> "luces"
  elif manjar.endswith(("a", "e", "i", "o", "u")):
    manjar_plural = manjar + "s"  # Ejemplo: "jamón" -> "jamones"
  else:
    manjar_plural = manjar + "es"  # Ejemplo: "flor" -> "flores"

  # Ajustar el verbo para estar en gerundio
  verbo_gerundio = verboGerundio(verbo)

  historia = f"""En el reino de Aguardiente, el valiente {caballero} fue convocado para una misión: {verbo.lower()} al terrible {criatura.lower()} 
  que aterrorizaba a los campesinos. Con su fiel {arma.lower()} en mano, {caballero} se aventuró al bosque {adjetivo.lower()}.

  Al llegar, {caballero} encontró al {criatura.lower()} junto a una mesa llena de {manjar.lower()}. En lugar de pelear, 
  el {criatura.lower()} le ofreció un banquete y le dijo: "No quiero {verbo.lower()} a nadie, solo quiero disfrutar de mis {manjar.lower()}. 
  ¿Puedes dejarme en paz?"

  Después de un largo debate y de mucho {manjar.lower()} comido, {caballero} decidió regresar al castillo y reportar que 
  el {criatura.lower()} ya no era una amenaza, solo un amante de la buena comida. Aunque, claro, el Rey nunca supo por qué 
  {caballero} regresó con un estómago tan lleno.
  """

  # Imprimimos un mensaje para presentar la historia
  time.sleep(2)
  print("\nTu aventura medieval:")
  time.sleep(2)
  print(historia)

elif instrucciones == 4: #AGENTE SECRETO

  nombre_agente = input("Nombre del agente secreto: ")
  código = input("Un código secreto: ")
  país = input("Un país exótico: ")
  objeto = input("Un objeto espía: ")
  desastre = input("Un desastre improbable: ")
  exclamacion = input("Una exclamación: ")

  historia = f"""El agente secreto {nombre_agente}, conocido como {código}, fue enviado a {país} en su misión más peligrosa hasta ahora. 
  Su objetivo: recuperar un {objeto.lower()} que contenía información ultrasecreta.

  Todo iba según lo planeado hasta que ocurrió un {desastre.lower()}. "{exclamacion}!", gritó {nombre_agente}, mientras buscaba desesperadamente su {objeto.lower()} de emergencia. 
  Por suerte, el {objeto.lower()} no solo salvó la misión, sino que también le permitió escapar de una forma tan absurda que ni las películas lo creerían.

  Al regresar a casa, el jefe de {nombre_agente} lo felicitó, aunque todavía tenía dudas sobre cómo un {desastre.lower()} pudo involucrar un {objeto.lower()}. 
  {nombre_agente} simplemente sonrió y dijo: "Un buen agente nunca revela todos sus secretos."
  """

  # Imprimimos un mensaje para presentar la historia
  time.sleep(2)
  print("\nTu misión secreta:")
  time.sleep(2)
  print(historia)

else:
  print("Opcion no valida")


  
  


      

