__author__ = 'ronald'
#Texto comillas simples
cadena = 'Texto entre comillas simples'
#Texto comillas dobles
texto = "Texto entre comillas dobles"

#type devuelve el tipo de la variable
print type(cadena)

#Salto de linea
cadena = 'Texto entre \n comillas simples'

print "Salto linea"
print cadena

#Tabulacion
cadena = 'Texto entre \t comillas simples'
print "Tabulacion"
print cadena

#Mediante comillas triples se puede evitar los caracteres de escape
cadena="""La cadena
 es
 esta la siguiente
"""
print cadena

#Repeticion de texto
print ("Repeticion de texto")
print (texto * 3)

#Concatenar cadenas
print("Concatenar cadenas")
print (texto + "el texto se concateno")

print ("\n")
#OPERADORES BOOLEANOS VERDAD O FALSO
verdaro = True
falso = False

#operadors logico and
bAnd= verdaro and falso

#Operador logico or
bor = verdaro or falso

#Operador logico not
bNot = not verdaro

print(bAnd)
print(bor)
print(bNot)