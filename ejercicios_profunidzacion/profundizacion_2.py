# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
nu_1 = int(input("Ingresar el primer numero:\n"))
nu_2 = int(input("Ingresar el segundo numero:\n"))
nu_3 = int(input("Ingresar el ultimo numero:\n"))

if (nu_1 % 2) == 0:
    print("El numero" , nu_1 , "es un numero par")
else:
    print("El numero", nu_1 , "es un numero impar")

if (nu_2 % 2) == 0:
    print("El numero" , nu_2 , "es un numero par")
else:
    print("El numero", nu_2 , "es un numero impar")

if (nu_3 % 2) == 0:
    print("El numero", nu_3 , "es un numero par")
else:
    print("El numero", nu_3 , "es un numero impar")