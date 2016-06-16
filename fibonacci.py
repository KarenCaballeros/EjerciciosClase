def fibonacci(num):
	lista= []
	if num == 0 or num == 1:
		return num 
	lista= [1]
	else:
		lista.append(lista[0] + lista[0])
		lista.append(num + 1)
		print(lista)
		return fibonacci(num)
