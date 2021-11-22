# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(texto_1 , "es mayor que" , texto_2)
else:
    print(texto_1 , "es menor que" , texto_2)

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print(texto_1 , "tiene mayor cantidad de letras que" , texto_2)
elif len(texto_1) < len(texto_2):
    print(texto_1 , "tiene menor cantidad de letras que" , texto_2)
else: 
    print(texto_1 , "tiene la misma cantidad de letras que" , texto_2)

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if texto_1[0] > texto_2[1]:
    print(texto_1[0] , "es mayor que" , texto_2[0])
else:
    print(texto_1[0] , "es menor que" , texto_2[0])

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print("Las variables son iguales")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if not copia_texto_1 == texto_2:
    print("Las variables son distintas")