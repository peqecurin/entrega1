from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators1 = ["+", "-", "*", "/"]
operators2 = ["+", "-", "*"]

# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

#Contador de respuestas correctas:
cont_correctas = 0

for i in range(0, times):
	# Se eligen números y operador al azar
	number_1 = randrange(10)
	number_2 = randrange(10)
	
	if (number_2 == 0) : 
		operator = choice(operators2)
	else:
		operator = choice(operators1)

	# Se imprime la cuenta.
	print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
	# Le pedimos al usuario el resultado
	result = input("resultado:")

	if (operator == "+"):
		cuenta = number_1 + number_2
		if (cuenta == int(result)): 
			print("el resultado es correcto")
			cont_correctas = cont_correctas + 1
		else : 
			print("el resultado es incorrecto")

	elif (operator == "-"):
		cuenta = number_1 - number_2
		if (cuenta == int(result)): 
			print("el resultado es correcto")
			cont_correctas = cont_correctas + 1
		else : 
			print("el resultado es incorrecto")

	elif (operator == "*"):
		cuenta = number_1 * number_2
		if (cuenta == int(result)): 
			print("el resultado es correcto")
			cont_correctas = cont_correctas + 1

		else : 
			print("el resultado es incorrecto")
	elif (operator == "/"):
		cuenta = number_1 / number_2
		if (int(cuenta) == int(result)): 
			print("el resultado es correcto")
			cont_correctas = cont_correctas + 1

		else : 
			print("el resultado es incorrecto")

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")

#Mostramos cuantás respuestas correctas hay:
print(f"\n Tenes {cont_correctas} respuestas correctas.")
#Cuantas incorrectas:
cont_incorrectas = 5 - cont_correctas
print(f"\n Tenes {cont_incorrectas} respuestas correctas.")
