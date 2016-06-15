from maximo import maximo

lista= []
pre= "si"

while pre == "si":
	num= int(input("Ingrese un numero: "))
	lista.append(num)
	pre= input("Si desea ingresar otro numero escriba si: ")

print(lista)
print ("El maximo de su lista es: " , maximo(lista))	