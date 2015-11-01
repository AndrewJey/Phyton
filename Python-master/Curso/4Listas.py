__author__ = 'ronald'
#Declaracion de lista
lista = [2,"tres",True,["uno","dos"]]

print "Lista \n "
print lista

#Acceder a los valores de la lista
print lista[3][0]

#CAmbiar el valor de un elemento de una lista
lista[0] = 4
print lista

#Acceder al rango de valores de una lista
print lista[0:2]

#Acceder cada n rangos
print lista[0::2]

#Sustituir un rango de elementos por uno
lista[0:2] = [7]
print lista
