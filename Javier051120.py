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


# In[ ]:




