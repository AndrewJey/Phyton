__author__ = 'Ronald'
class Operaciones:
    def ContarDigitos(num):
        cont = 0
        if(num == 0):
            cont = 1
        else:
            while(num > 0):
                num = num // 10
                cont = cont + 1
        return (cont)

    def Apariciones_Numero_enNumero(numero,numerocomprobar):
        cont = 0
        while numerocomprobar > 0:
            if numerocomprobar % 10 == numero:
                cont = cont + 1
            numerocomprobar // 10
        return cont

    def cambiarNumero(x,y,num):
        exp = 0
        nnum = 0
        while num > 0:
            if (num % 10 == x):
                nnum = nnum+ y * 10 ** exp
            else:
                nnum =nnum + (num // 10) * 10 **exp
            num = num//10
            exp = exp + 1
        return  nnum

    def invertir (num):
        exp = ContarDigitos(num)
