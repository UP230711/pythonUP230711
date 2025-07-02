#1
Dia = "Treinta"
espacio = " "
dias = "Dias"
En = "En"
Py = "Python"
oracion = Dia + espacio + dias + espacio + En + espacio + Py
print(oracion)
#2
Co = "Coding"
por = "For"
Todo = "All"
#3
Comp= Co + espacio + por + espacio + Todo
#4
print(Comp)
#5
print(len(Comp))
#6
print(Comp.upper())
#7
print(Comp.lower())
#8
print(Comp.capitalize())
print(Comp.title())
print(Comp.swapcase())
#9
print(Comp.strip("Coding"))
#10
print(Comp.index("Coding"))
print(Comp.find("Coding"))
#11
print(Comp.replace("Coding", "Python"))
#12
Eve = "Everyone"
Pyt = Py + espacio + por + espacio + Eve
print(Pyt)
print(Pyt.replace("Everyone","All"))
#13
print(Comp.split())
#14
Go = "Google"
Fb = "Facebook"
Mc = "Microsoft"
Apple = "Apple"
Ibm = "IBM"
Ora = "Oracle"
Amz= "Amazon"
Apps = Fb + espacio + Go + espacio + Mc + espacio + Apple + espacio + Ibm + espacio + Ora + espacio + Amz
print(Apps.split())
#15
Com = Comp[0]
print(Com)
#16
Ult = Comp[12]
print(Ult)
#17
Va = Comp[10]
print(Va)
#18 
Acro = Py[0] + por[0] + Eve[0]
print(Acro)
#19
Acro2 = Co[0] + por[0] + Todo[0]
print(Acro2)
#20
print(Comp.index("C"))
#21
print(Comp.index("F"))
#22
Personas = "People"
Sub_Company = Comp + espacio + Personas
print(Sub_Company.rfind("l"))
#23
Segunda_oracion = "You cannot end a sentence with because because because is a conjunction"
print(Segunda_oracion.find("because"))
#24
print(Segunda_oracion.rindex("because"))
#25
print(Segunda_oracion.replace(' because', ''))
#26
print(Segunda_oracion.index("because"))
#27
print(Segunda_oracion.replace(' because', ''))
#28

print(Comp.find("Coding"))
#29

print(Comp.rfind("Coding"))
#30
Tri_Company = espacio + Comp + espacio
print(Tri_Company)
print(Tri_Company.strip(" "))
#31
uno =  "30DaysOfPython"
dos = "thirty_days_of_python"
print(uno.isidentifier()) #False, lo marca porque empieza por numero, cosa que no se puede
print(dos.isidentifier()) #True, al iniciar con letras este es el correcto
#32
Lista =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(Lista)
print(" ".join(Lista))
#33
print("I am enjoying this challenge. \nI just wonder what is next.")
#34
print("Name    \tAge  \tCountry   \tCity")
print("Asabeneh\t250\tFinland   \tHelsinki")
#35
Radio = 10
area = 3.14 *Radio**2
formando = "The area of circle with a radius %d is %.2f." %(Radio, area)
print(formando)
#36
d = 8
f = 6
print('{} + {} = {}'.format(d, f, d + f))
print('{} - {} = {}'.format(d, f, d - f))
print('{} * {} = {}'.format(d, f, d * f))
print('{} / {} = {}'.format(d, f, d / f)) 
print('{} % {} = {}'.format(d, f, d % f))
print('{} // {} = {}'.format(d, f, d // f))
print('{} ** {} = {}'.format(d, f, d ** f))

