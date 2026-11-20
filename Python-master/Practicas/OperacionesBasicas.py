__author__ = 'Ronald'


class Operaciones:
    @staticmethod
    def ContarDigitos(num):
        n = abs(int(num))
        if n == 0:
            return 1
        cont = 0
        while n > 0:
            n //= 10
            cont += 1
        return cont

    @staticmethod
    def Apariciones_Numero_enNumero(numero, numerocomprobar):
        digito = abs(int(numero))
        if digito > 9:
            raise ValueError('numero debe ser un dígito entre 0 y 9')
        n = abs(int(numerocomprobar))
        if n == 0:
            return 1 if digito == 0 else 0
        cont = 0
        while n > 0:
            if n % 10 == digito:
                cont += 1
            n //= 10
        return cont

    @staticmethod
    def cambiarNumero(x, y, num):
        objetivo = abs(int(x))
        reemplazo = abs(int(y))
        if objetivo > 9 or reemplazo > 9:
            raise ValueError('x e y deben ser dígitos entre 0 y 9')
        signo = -1 if int(num) < 0 else 1
        n = abs(int(num))
        if n == 0:
            return reemplazo if objetivo == 0 else 0
        exp = 0
        nnum = 0
        while n > 0:
            digito = n % 10
            nuevo = reemplazo if digito == objetivo else digito
            nnum += nuevo * (10 ** exp)
            n //= 10
            exp += 1
        return signo * nnum

    @staticmethod
    def invertir(num):
        signo = -1 if int(num) < 0 else 1
        n = abs(int(num))
        invertido = 0
        while n > 0:
            invertido = invertido * 10 + (n % 10)
            n //= 10
        return signo * invertido
