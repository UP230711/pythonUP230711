edad = 19 #1
estatura = 1.85 #2
a= 7-30j #3

#4
print("area de un triangulo")
base= float(input("ingresa tu base: "))
altura = float(input("ingresa tu altura: "))
print((base*altura/2))

#5
print("perimetro de un triangulo")
lado_1= float(input("ingresa el valor de tu lado 1: "))
lado_2= float(input("ingresa el valor de tu lado 2: "))
lado_3= float(input("ingresa el valor de tu lado 3: "))
perimetro = lado_1+lado_2+lado_3
print (perimetro)

#6
largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
area = largo * ancho
perimetro = 2 * (largo + ancho)
print("Área del rectángulo:", area)
print("Perímetro del rectángulo:", perimetro)

#7
radio = float(input("Ingresa el radio del círculo: "))
pi = 3.14
area = pi * (radio **2)
circunferencia = 2 * pi * radio
print("Área del círculo:", area)
print("Circunferencia del círculo:", circunferencia)

#11
x = float(input("ingresa tu x: "))
y = x**2 + 6*x + 9
print("y es igual a: ", y)

#12
primera_palabra = "python"
segunda_palabra = "dragon"
longitud1 = len(primera_palabra)
longitud2 = len(segunda_palabra)
print("Longitud de 'python':", longitud1)
print("Longitud de 'dragon':", longitud2)
comparacion = longitud1 > longitud2
print("¿'python' es más larga?", comparacion) 

#15
estara = ('on' not in primera_palabra) and ('on' not in segunda_palabra)
print("¿No hay 'on' en ambas palabras?:", estara)

#13
z= ('on' in 'python') and ('on' in 'dragon')
print("¿'on' está en 'python' y en 'dragon'?:", z)

#14
oracion = "I hope this course is not full of jargon"
resultado = 'jargon' in oracion
print("¿'jargon' está?:", resultado)

#16
texto = "python"
longitud = len(texto)
longitud_float = float(longitud)
longitud_str = str(longitud_float)
print("Longitud como entero:", longitud)
print("Longitud como float:", longitud_float)
print("Longitud como string:", longitud_str)

#17
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#18
division_entera = 7 // 3
valor_convertido = int(2.7)
resultado = division_entera == valor_convertido
print("7 // 3 =", division_entera)
print("int(2.7) =", valor_convertido)
print("¿Son iguales?:", resultado)

#19
resultado = type('10') == type(10)
print("¿El tipo de '10' es igual al tipo de 10?:", resultado)

#20
int(9.8) == 10
#el valor representa un str

#21
horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
salario = horas * tarifa
print("Tu ganancia semanal es", salario)

#22
anios = int(input("Ingresa el número de años: "))
segundos= 365 * 24 * 60 * 60
segundos_totales = anios * segundos
print("Has vivido ", segundos_totales, "segundos.")

#23
for n in range(1, 6):
    print(n, 1, n, n**2, n**3)



