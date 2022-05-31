print('Bienvenidos a la tienda de Jimena!')
print('Ingrese su nombre: ')
nom=input()
print('Hola', nom)
print('Articulos a comprar: ')
print('audifonos')
print('papas')
print('refresco')
print('mochila')
print('ipad')
print('lapiz')
print('lapicera')
print('goma')
print('chicle')
print('agua')


while True:
  a=input('ingrese el articulo:')
  if(a=='audifonos'):
    print('los audifonos cuestan $110')
    costo=110
  if(a=='papas'):
    print('las papa cuestan $17')
    costo=17
  if(a=='refresco'):
    print('los refrescos cuestan $39')
    costo=39
  if(a=='mochila'):
    print('las mochilas cuestan $129')
    costo=129
  if(a=='ipad'):
    print('los ipads cuestan $5499')
    costo=5499
  if(a=='lapiz'):
    print('los lapices cuestan $9')
    costo=9
  if(a=='lapicera'):
    print('las lapiceras cuestan $30')
    costo=30
  if(a=='goma'):
    print('las gomas cuestan $5')
    costo=5
  if(a=='chicle'):
    print('los chicles cuestan $2')
    costo=2
  if(a=='agua'):
    print('las aguas cuestan $10')
    costo=10
   
  b=input('ingrese el articulo:')
  if(b=='audifonos'):
    print('los audifonos cuestan $110')
    costo2=110
  if(b=='papas'):
    print('las papa cuestan $17')
    costo2=17
  if(b=='refresco'):
    print('los refrescos cuestan $39')
    costo2=39
  if(b=='mochila'):
    print('las mochilas cuestan $129')
    costo2=129
  if(b=='ipad'):
    print('los ipads cuestan $5499')
    costo2=5499
  if(b=='lapiz'):
    print('los lapices cuestan $9')
    costo2=9
  if(b=='lapicera'):
    print('las lapiceras cuestan $30')
    costo2=30
  if(b=='goma'):
    print('las gomas cuestan $5')
    costo2=5
  if(b=='chicle'):
    print('los chicles cuestan $2')
    costo2=2
  if(b=='agua'):
    print('las aguas cuestan $10')
    costo2=10
  print('el total es:',(costo+costo2))