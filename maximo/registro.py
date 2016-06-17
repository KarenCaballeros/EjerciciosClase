
print("BIENVENIDO A REGISTRO.PY")

menu= "si"

estudiantes= {
	
}

while menu =="si":

	print("1. Crear estudiante.")
	print("2. Ingresar notas.")
	print("3. Reporte de notas.")
	print("4. Salir.")

	pre= int(input("Ingrese opcion escogida: "))


	if pre == 1:
		opc= "si" 
		while opc == "si":
			estu= input("Ingrese nombre del estudiante: ")
			estudiantes[estu] = []
			opc= input("Si desea crear otro estudiante escriba si: ")

	elif pre == 2:
		opc= "si"
		nom= input("Ingrese nombre del estudiante: ")
		while opc == "si":
			nota= int(input("Ingrese nota: "))
			if nota <= 100 and nota >= 0:
				estudiantes[nom] += [nota]
			else:
				print("Ingreso nota invalida.")	
			opc= input("Si desea seguir ingresando notas a este estudiante escriba si: ")

	elif pre == 3:
		opc = "si"
		while opc == "si":
			nom= input("Ingrese el nombre del alumno: ")
			print(estudiantes[nom])
			suma = 0
			for i in estudiantes[nom]:
   				suma += i
   				prome= suma/len(estudiantes[nom])
			print("Y su promedio es: ", prome)
			opc= input("Si desea ver el reporte de otro alumno escriba si: ")

	elif pre == 4:
		print("Vuelva pronto.")
		menu= "no"

	else:	
		print("Error, opcion inexistente.")

