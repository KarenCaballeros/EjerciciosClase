def fibonacci(num):
	if num == 0 or num == 1:
		return num 	
	else:
		num2= num -1
		num3= num -2
		return fibonacci(num2) + fibonacci(num3) 
