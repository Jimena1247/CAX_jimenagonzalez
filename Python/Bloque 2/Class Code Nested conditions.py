#nested conditions


mensaje=input("escribe hola:   ")

if(mensaje!="hola"):

  if(mensaje=="HOLA"):
    print("que no sabe leer, era hola....")
    mensaje=input("intentalo nuevamente")
    if(mensaje=="HOLA"): 
      print("y con todo y eso no aorende a leer")

  elif(mensaje=="hoLA"):
    print("la L y la A es minuscula")
    mensaje=input("inetentelo nuevamente:  ")
    if(mensaje=="hoLa"):
      print("te dije que la L y la A no solo la A")

  elif(mensaje=="Hola"):
    print("se agradece una persona muy aletrada, pero aprenda a leer, dije hola")

  elif(mensaje=="hOLA"):
    print("desactive el bloq mayus")

  else:
    print("en serio.....")

elif(mensaje=="hola"):
  print("que agradable sujeto")