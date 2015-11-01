__author__ = 'ronald'

numero = 45 #Numero entero normal
numerolong = 4L #Numero entero largo
real = 0.454 #Real comun float
real2 = 0.45e-3 #Elebado a un exponente

print "Numero entero comun" + str(numero)
print "Numero largo comun" + str(numerolong)
print "Numero real comun" + str(real)
print "Numero real eleabado " + str(real2)

#Suma
print "La suma de "+str(numero) + " + "+str(numerolong)+ " es = "+str(numero+numerolong)
#Resta
print "La resta de "+str(numero) + " - "+str(numerolong)+ " es = "+str(numero-numerolong)
#Multiplicacion
print "La multiplicacion de "+str(numero) + " * "+str(numerolong)+ " es = "+str(numero*numerolong)
#Exponente
print "El numero " + str(numero) +" elevado al 3 es igual a "+str(numero ** 3)
#Division
print "La Division de "+str(numero) + " / "+str(numerolong)+ " es = "+str(float(numero)/numerolong)
#Division Entera
print "La Division entera de "+str(numero) + " // "+str(numerolong)+ " es = "+str(numero//numerolong)
#Modulo
print "El modulo de  "+str(numero) + " % "+str(numerolong)+ " es = "+str(numero%numerolong)
