n= []
opc= "si" 

while opc== "si":
	n.append( int(input("Ingrese una nota: ")))
	opc= input("Si desea seguir ingresando notas escriba si: ")

notas= open("notasguardadas.txt" , 'w')

for nota in n:
	notas.write(str(nota) + "\n")

notas.close()