#!/usr/bin/env python
# coding: utf-8

# # Curso de Python
# 
# # Clase 3
# El curso tiene como proposito aprender los fundamentos de python.
# 
# Variables: Una variable es un espacio reservado en memoria, 
# que tiene un tipo de valor, un nombre, y el valor

# In[1]:


print("Hola mundo")


# # Clase 4

# In[3]:


var1 = 0
var2 = 0.0
print(type(var1))
print(type(var2))


# In[ ]:


initial = 3

variableNameCannotBegingWhitANumber = True

boolean = False

posInt = 5

cero = 0

negFloat = -5

initial = 5


# In[4]:


intVal = 9

floatVal = 5.4

boolVal = False

print(boolVal)

boolVal = True

print(intVal)

print(floatVal)

print(boolVal)


# In[6]:


#Comentario de una sola linea
"""
    FFFFFFFFFFFF
    Comentario multilinea
    FFFFFFFFFFFF
"""


# In[8]:


# Asignar el mismo valor a multiples variable
a = b = c = 0
print(a, b, c)

# Asignar a multiples varibales, valores diferentes
x, y, z = 10, 3.5, "Hola"
print("x=",x)
print("y=",y)
print("z=",z)


# # Clase 5
# Hoy estamos viendo los tipos de operaciones y los operadores de asignación.

# In[13]:


mi_dinero = 50
cafe, galletas, papas = 24, 12, 13

print("cafe = ", cafe, "galletas = ", galletas, "papas = ", papas)
print("Total = ", mi_dinero - cafe - galletas - papas)
print("Total = ", mi_dinero - cafe - galletas)


# In[15]:


cateto_opuesto, cateto_adyacente = 10, 5
hipotenusa = (cateto_adyacente * cateto_adyacente + cateto_opuesto * cateto_opuesto) ** 0.5
print(" Valor = ", hipotenusa, "\n", "cateto_opuesto = ", cateto_opuesto, "\n", "cateto_adyacente = ", cateto_adyacente)


# In[16]:


lado1, lado2 = 8, 5
area = (lado1 * 3.28084) * (lado2 * 3.28084)

print("Lado 1 = ", lado1, "\nLado2 = ", lado2, "\nArea = ", area, "pies")


# # Clase 6

# Ejercicio jerarquía de las operaciones
# Original: (9 -7) * 2 ** 3 + 10 % 6 // -1 * 2 -1
#    2 * 2 ** 3 + 10 % 6 // -1 * 2 -1 
#    2 * 8 + 10  % 6 // -1 * 2 -1 
#    16 - 8 -1
#    16 -9
#    7

# In[5]:


# comentario simple
"""
    Comentario multilinea
"""
suma = 2 + 3
resta = 5 - 3
mul = 8 * 2
div = 6 / 2
print("Resultado de la suma es: ",suma)
print("Resultado de la resta es: ",resta)
print("Resultado de la multiplicacion es: ",mul)
print("Resultado de la division es: ",div)


# In[3]:


operators1, operators2, operators3 = 5, 6, 7
operators1 **= 2
print(operators1)

operators2 //= 0.5
print(operators2)

operators3 %= 2
print(operators3)


# In[ ]:


#7 + 6 +9 - 4 * ((9-2)**2)/7
print(9-2)
print(7**2)
print(4 * 49)
print(196/7)
print(7 + 6 + 9 - 28)


# In[ ]:


#(6 % 4 *(7 + (7 + 2)*3))**2
print(7 + 2)
print(9 * 3)
print(7 + 27)
print(6 % 4)
print(2 * 34)
print(68 ** 2)


# # Clase 7

# In[ ]:


lannisters = "JaimeCerseiTyrion"
var1 = lannisters[1]
print(var1)

var2 = lannisters[0]
print(var2)

var3 = lannisters[:5]
print(var3)

var4 = lannisters[5:11]
print(var4)

var5 = lannisters[11:]
print(var5)


# In[22]:


print("Comillas dobles")
print('comillas simples')
print("Sentencia de \'escape'")

var = "alligator"
var2 = var[5]
print(var2)
var3 = var[:4]
print(var3)
var4 = var[4:7]
print(var4)
var5 = var[6:]
print(var5)


# # Clase 8

# In[9]:


var1="upper"
print(var1.upper())

var2="LOWER"
print(var2.lower())
var3=var2[1:4]
print(var3)


# In[10]:


cadena = "Python"
cad2 = len (cadena)
print(cad2)

cad3 = cadena[1:4]
print(cad3)
cad4 = len(cad3)
print(cad4)

var1 = 1.32
cad5= str(var1)
print(cad5)
cad6 = cad5[3:]
print(cad6)


# In[11]:


cad = "Manchester United"
cad2 = len(cad)
print(cad2)

var3 = 12345
cad4 = str(var3)
cad5 = cad4[2]
print (cad5)

cad6 = "albania"
print(cad6.upper())

cad7 = "BELGIUM"
print(cad7.lower())


# # Clase 9

# In[13]:


ocup = input("Introduce tu ocupación")
ciudad = input("introduce tu ciudad")
edad = input("introduce tu edad")

print("Tu ocupacion: {}, tu ciudad {}, tu edad {}".format(ocup, ciudad, edad))


# In[15]:


cateto_opuesto = int(input("Introduce el cateto opuesto"))
cateto_adyacente =  int(input("introduce el cateto adyacente"))
hipotenusa = (cateto_adyacente * cateto_adyacente + cateto_opuesto * cateto_opuesto) ** 0.5
print(" Hipotenusa = ", hipotenusa, "\n", "cateto_opuesto = ", cateto_opuesto, "\n", "cateto_adyacente = ", cateto_adyacente)


# # Clase 10

# In[10]:


var1 = "Hello"
var2 = "world"
print("%s, %s"%(var1, var2))

var3 = 11
var4 = 38
print(("%s%s")%(str(var3), str(var4)))


# In[14]:


var = input("Restaurante favorito? ")
var2 = input("Lugar para visitar? ")
var3 = input("sobrenombre? ")
print("Tu restaurante favorito: %s, tu lugar favorito: %s, tu sobrenombre: %s."%(var, var2, var3))


# In[15]:


#Otra forma
var = input("Restaurante favorito? ")
var2 = input("Lugar para visitar? ")
var3 = input("sobrenombre? ")
print("Tu restaurante favorito: {}, tu lugar favorito: {}, tu sobrenombre: {}.".format(var, var2, var3))


# In[24]:


#Crea un programa en donde guardes el precio de un articulo y despues
#mostrarlo con IVA.
var = input("Ingresar el precio: ")
var1 = (0.16 * int(var)) + int(var)
var2 = (0.16 * int(var))
print("Valor del Producto con IVA: %s, el IVA fue de: %s"%(str(var1), str(var2)))


# In[30]:


var1 = int(input("ingresar el valor: "))
sum = (var1 * (var1 + 1) )/2
print(sum)


# In[39]:


var1 = 2 > 0
print(var1)
var2 = -2 > 0
print(var2)
var1 = 7 >= 5
print(var1)
var1 = 4 >= 5
print(var1)

var1 = 2 < 10
print(var1)
var2 = -2 < -10
print(var2)
var1 = 7 <= 8
print(var1)
var1 = 6 <= 5
print(var1)

var1 = 0 == 0
print(var1)
var2 = -2 == 0
print(var2)
var1 = 4 != 5
print(var1)
var1 = 5 != 5
print(var1)


# In[48]:


var1 = 2 > 0 and 5 > 2
print(var1)
var2 =  -3 > 0 and 5 > 8
print(var2)

var3 = 2 > 0 or 5 > 2
print(var3)
var4 =  -3 > 0 or 5 > 8
print(var4)

var5 = not 5 > 5
print(var5)
var6 =  not 9 > 8
print(var6)


# # Clase 11
# IF ELSE y ELIF

# In[ ]:


#EJERCICIO
var = input("Ingresa tu nombre")
var2 = len(var)
print(var2)
if var2 >= 0 and var2<=4:
    print("Tu nombre tiene entre 0 y 4 caracteres")
elif var2 >= 5 and var2<=10:
    print("Tu nombre tiene entre 5 y 10 caracteres")
elif var2 > 10:
    print("Tu nombre tiene mas de 10 caracteres")


# # Clase 12

# In[ ]:


var = int(input("Ingresa los grados"))
grados = int(input("Ingresa: 1 para celsius  y 2 para fahrenheit que deseas obtener"))

if grados == 1:
    c = (var - 32) / 1.8
    print("Los grados celsius: " + str(c))
elif grados == 2:
    f = (1.8 * var) + 32
    print("Los grados fahrenheit: " + str(f))
else:
    print("Error en la introduccion de datos")


# In[1]:


años = 15
print(años)


# # Clase 14

# In[9]:


numero = 5
intento = 0
print("Adivina el numero entre 0 y 9")

while(intento < 3):
    
    num = int(input("Cual crees que es el numero ganador? "))

    if num > 10 or num < 0:
        print("Numero fuera de rango")

    elif num == numero:
        print("El numero es el indicadoooooo")
        break
        
    elif num < numero:
        print("El numero a adivinar es mayor")
        intento += 1
        
    elif num > numero:
        print("El numero a adivinar es menor")
        intento += 1
        
print("\nSe interrumpio el ciclo while")
print("Fin del programa")


# In[20]:


mes = input("Introduce el mes del año en minusculas")

if "febrero" == mes:
    print("El mes tiene 29 o 28 días")

elif "enero" == mes or "marzo" == mes or "mayo" == mes or "julio" == mes or "agosto" == mes or "octubre" == mes or "diciembre" == mes:
    print("El mes tiene 31 días")
        
elif "abril" == mes or "junio" == mes or "septiembre" == mes or "noviembre" == mes:
    print("El mes tiene 30 días")


# In[25]:


lado1 = int(input("Introduce el primer lado de tu triangulo"))
lado2 = int(input("Introduce el segundo lado de tu triangulo"))
lado3 = int(input("Introduce el tercer lado de tu triangulo"))

if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilatero")

elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("El triangulo es escaleno")
        
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("El triangulo es isoceles")


# In[26]:


def ejemplo():
    print("Ora que joven")


# In[27]:


ejemplo()


# In[31]:


def pitagoras():
    cateto_opuesto = int(input("Introduce el cateto opuesto "))
    cateto_adyacente =  int(input("introduce el cateto adyacente "))
    hipotenusa = (cateto_adyacente * cateto_adyacente + cateto_opuesto * cateto_opuesto) ** 0.5
    print(" Hipotenusa = ", hipotenusa, "\n", "cateto_opuesto = ", cateto_opuesto, "\n", "cateto_adyacente = ", cateto_adyacente)


# In[32]:


pitagoras()


# In[12]:


def formulageneral ():
    import math
    a = int(input("Introduce el coheficiente del termino cuadratico a = "))
    b = int(input("Introduce el coheficiente del termino lineal b = "))
    c = int(input("Introduce el coheficiente del termino independiente c = "))
    r = b*b - 4*a*c
    if r <= 0:
        print("\nLo siento los números introducidos daran un número imaginario, no se puede continuar.")
    elif r >= 0:
        raiz = math.sqrt((b*b)-4*a*c)
        x1 = (-b + raiz)/(2*a)
        x2 = (-b - raiz)/(2*a)
        print("\nEl valor de x1 = {}\nEl valor de x2 = {}".format(x1, x2))
    
    opc = int(input("\nPresiona 1 para introducir nuevos valores.\nPresiona 2 para salir. "))
    if opc == 1:
        formulageneral()
    elif opc == 2:
        print("\nGracias por usar la funsion :D")
    else:
        print("Error de parametros, de todos modos me saldree :D")
    


# In[14]:


formulageneral()


# # Clase 15
# Funciones

# In[23]:


def hipot(v1, v2):
    hipo = (v1 ** 2 + v2 ** 2) ** 0.5
    return hipo


# In[24]:


valor = hipot(3, 4)


# In[25]:


print(valor)


# In[28]:


def areacirculo():
    radio = int(input("Introduce el radio del circulo"))
    r = 3.14 * (radio * radio)
    print("Su área es: ", r)


# In[29]:


areacirculo()


# In[33]:


lista = ['papel', 'shampoo', 'etc', 'etc2', True, 4, 8]


# In[34]:


print(lista)


# In[35]:


print(lista[2])


# # Clase 16
# Listas

# In[1]:


bandas = ['Wolfmothert', 'Banda MS', 'Muse', 'Ghost', 'Sleeping whit sirens', 'Interpol']


# In[2]:


metal = bandas [3]
print(metal)


# In[3]:


norte = bandas [1]
print(norte)


# In[4]:


grupos = bandas [4:]
print(grupos)


# In[5]:


print(len(bandas))


# In[8]:


# agregar un nuevo elemento
bandas.append('Little jesus')


# In[9]:


print(bandas)


# In[10]:


bandas[2] = 'Bloc Party'


# In[11]:


print(bandas)


# In[13]:


variables = bandas[2:5]


# In[15]:


print(variables)


# In[16]:


var2 = bandas[:2]


# In[17]:


print(var2)


# In[18]:


var3 = bandas[5:]
print(var3)


# In[19]:


var4 = []
var4.append(bandas[2])
var4.append(bandas[5])
print(var4)


# In[20]:


# Agregar elementos en una lista en cualquier posicion
print(bandas)
bandas.insert(1, 'Artic Monkeys')


# In[21]:


print(bandas)


# In[22]:


# Eliminar elementos de una lista a traves de su nombre
bandas.remove('Banda MS')


# In[23]:


print(bandas)


# In[24]:


for elemento in bandas:
    print('{} Es la mejor banda'.format(elemento))


# In[29]:


lista1 = [1,2,3,4,5,6]
lista2 = []
indice = 0
for num in lista1:
    lista2.append(num**2)
    print(indice, num)
    indice += 1
    
print(lista1)
print(lista2)


# In[31]:


for i in range (5,20,2):
    print(i)


# In[33]:


for i in range (30,20,-1):
    print(i)


# In[67]:


cad = input('Introduce una cadena: ')
indice = len(cad)
for p in range (indice, 0, -1):
    p -= 1
    print(cad[p])


# In[69]:


#Tarea
i = int(input('introduce un número positivo'))
if i > 0:
    print("hola")
else:
    print("Número incorrecto")


# In[13]:


var = input("Ingresa un numero: ")
try:
    var = int(var)
    print(var)
except:
    print('Dato no valido')


# In[12]:


# While

i = 0
while i < 10:
    print("Hola ", i)
    i += 1


# In[1]:


#Tarea

num = input("Ingresa un número: ")
var = 0
try:
    num = int(num)
    while num != 0:
        var += num
        num -= 1
except:
    print("Valor no valido.")

print("Suma total: ", var)


# In[41]:


i = 1
while i <= 100: 
    if i%5 == 0  and i%3 == 0:
        print(i, "trentacinque")
    elif i%5 == 0:
        print(i, "cinque")
    elif i%3 == 0:
        print(i, "tre")
    else:
        print(i)
    i += 1


# In[55]:


var = input("Ingresa una cadena: ")
var2 = input("Ingresa la letra a buscar: ")
n = len(var) - 1
var3 = 0

while n != 0:
    if var[n] == var2:
        var3 += 1
    n -= 1    
print("Número de aparición: ", var3)


# In[60]:


num = [1, 2, 8, 4, 5, 6, 7]
num2 = [11, 222, 333, 44]


# In[61]:


num.extend(num2)
print (num)


# In[62]:


num.count(2)


# In[63]:


num.sort()
print(num)


# In[65]:


num.sort(reverse = True)
print(num)


# In[66]:


lista = ["ho"]
print(lista)


# In[67]:


lista * 5
print(lista * 5)


# # Clase 18
# pop()

# In[3]:


bandas = ['Wolfmothert', 'Banda MS', 'Muse', 'Ghost', 'Sleeping whit sirens', 'Interpol']


# In[5]:


lis = bandas.pop(1)


# In[6]:


print(lis)


# In[8]:


#Tuplas

bandas_tupla = ('Wolfmothert', 'Banda MS', 'Muse', 'Ghost', 'Sleeping whit sirens', 'Interpol')
bandas_listas = ['Wolfmothert', 'Banda MS', 'Muse', 'Ghost', 'Sleeping whit sirens', 'Interpol']

print(bandas_tupla)
print(bandas_listas)


# In[14]:


bandas_listas[0]='Banda MS'


# In[15]:


bandas_listas


# In[17]:


#No se pueden modificar
bandas_tupla[0]='Banda MS'


# In[33]:


var = [1, 2, 3, 4]
print(var[1])

print(var[:2])

print(var[1:3])

print(var[2:])

for i in var:
    print(i)


# In[43]:


#Diccionarios

d = {'rock':'Estefania', 'banda':'Ulises', 'metal':'david'}


# In[44]:


print(d['rock'])


# In[45]:


d ['pop'] = ['carlos','arlette','javier']


# In[47]:


print(d)


# In[48]:


d ['banda'] = 'isai'


# In[49]:


print(d)


# In[52]:


d['pop'][1] = 'Estafniaa'


# In[53]:


print(d)


# In[54]:


del(d['metal'])


# In[55]:


print(d)


# In[ ]:




