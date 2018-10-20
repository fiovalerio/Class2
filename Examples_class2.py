# Ejemplos del if en python:

esta_lloviendo = True
tenemos_hambre = False
python_es_genial = True
ayer_pagaron = False
vamos_a_la_playa= False

# Funcion para solictar datos por consola input("mensage")
# La funcion input siempre retorna un string. Tenemos que
# convertirlo a numero antes de hacer operaciones numericas
numero_digitado2 = input("digite un numero: ") #Almaceno como numero digitado
numero_digitado_como_numero = int(numero_digitado)


if esta_lloviendo and tenemos_hambre:
    # Este codigo esta dentro del if
    print ("Esta lloviendo y tenemos hambre")
elif 12 < numero_digitado_como_numero and python_es_genial or vamos_a_la_playa:
    print ("Python es genial o vamos a la playa")
else:
    print("Esto se ejecuta si ninguna condicion es verdadera")






numero_digitado = float(input("digite un numero que va a ser evaluado: "))

if numero_digitado % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
