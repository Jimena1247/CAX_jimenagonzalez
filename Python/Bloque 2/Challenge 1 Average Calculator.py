mate1=int(input("calificacion1: "))
mate2=int(input("calificacion2: "))
mate3=int(input("calificacion3: "))

promedio=((mate1+mate2+mate3)/3)


if promedio >= 9:
  print("GANASTE UN PREMIO")

if promedio >= 6:
  print("pasaste")

if promedio < 6:
  print("reprobaste")
