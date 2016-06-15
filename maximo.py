def maximo(lista):
	if lista[0] > lista[1:]:
		return lista[0]
	else:
		lista[0] <= lista[1]
		return maximo(lista[1:])