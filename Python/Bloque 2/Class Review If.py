
while True:
  a=int(input('adivina el numero: '))
  if(a==9):
    print('-adivinaste-')
  if(a<9):
    print('te falta')
  if(a>9):
    print('te sobra')