from collections import deque

def es_palindromo(palabra):
	pila = list(palabra)
	cola = deque(pila)
	while len(pila) > 0:
		if pila.pop() != cola.popleft():
			return False
	return True