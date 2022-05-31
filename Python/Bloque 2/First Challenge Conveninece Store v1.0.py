#tienda mct
cajero=input('escribe tu nombre: ')
art1=input(' articulo 1: ')
precio1=int(input(' cuanto cuesta: '))
art2=input('articulo 2: ')
precio2=int(input(' cuanto cuesta: '))
art3=input(' articulo 3: ')
precio3=int(input(' cuanto cuesta: '))
art4=input(' articulo 4: ')
precio4=int(input('cuanto cuesta: '))
art5=input(' articulo 5: ')
precio5=int(input(' cuanto cuesta: '))

subtotal=precio1+precio2+precio3+precio4+precio5
iva=.16
impuesto=subtotal+iva

total=subtotal+impuesto

#ticket
print(' tiendita mct')
print(' cajero:', cajero)
print(art1, '$', precio1)
print(art2, '$', precio2)
print(art3, '$', precio3)
print(art4, '$', precio4)
print(art5, '$', precio5)
print(' tu subtotal es: ', subtotal)
print(' tu total es: ', total)
print(' gracias por tu compra')