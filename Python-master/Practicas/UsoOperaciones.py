__author__ = 'ronald'
from OperacionesBasicas import Operaciones


def main():
    print('ContarDigitos(12045):', Operaciones.ContarDigitos(12045))
    print('Apariciones_Numero_enNumero(2, 21225):', Operaciones.Apariciones_Numero_enNumero(2, 21225))
    print('cambiarNumero(2, 9, 21225):', Operaciones.cambiarNumero(2, 9, 21225))
    print('invertir(12345):', Operaciones.invertir(12345))


if __name__ == '__main__':
    main()
