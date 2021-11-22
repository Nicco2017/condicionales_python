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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

text_1 = str(input("Ingrese una palabra:\n"))
text_2 = str(input("Ingrese otra palabra:\n"))
text_3 = str(input("Ingrese la ultima palabra:\n"))
orden = int(input("Ingrese la opcion 1 o 2:\n"))

if not orden == 1 or orden == 2:
    print("Ingrese solamente las opciones 1 o 2, mencionadas anteriormente")
    orden = int(input("ingrese la opcion 1 o 2:\n"))

# si ingresa otra opcion que no sea 1 o 2 hay que hacer un bucle para que vulva a ejecutar la orden OPCION
# al no restringir como en este caso al ingresar una opcion como un valor a 3, el programa sigue su ejecucion.

if orden == 1:
    if text_1 > text_2:
        if text_1 > text_3:
            print(text_1 ,"," ,  text_2 , "y" , text_3 , "ese es su orden alfabetico")
        else:
            print(text_3 ,"," ,  text_1 , "y" , text_2 , "ese es su orden alfabetico")
    else:
        if text_2 > text_3:
            print(text_2 , "," ,  text_3 , "y" , text_1 , "ese es su orden alfabetico")
        else:
            print(text_3 , "," ,  text_2 , "y" , text_1 , "ese es su orden alfabetico")
elif orden == 2:
    if len(text_1) > len(text_2):
        if len(text_1) > len(text_3):
            print(text_1 ,"," ,  text_3 , "y" , text_2 , "se ordeno por cantidad de letras de mayor a menor")
        else:
            print(text_3 ,"," ,  text_1 , "y" , text_2 , "se ordeno por cantidad de letras de mayor a menor")
    else:
        if len(text_2) > len(text_3):
            print(text_2 ,"," ,  text_3 , "y" , text_1 , "se ordeno por cantidad de letras de mayor a menor")
        else:
            print(text_3 ,"," ,  text_2 , "y" , text_1 , "se ordeno por cantidad de letras de mayor a menor")