def recorrido(n,m):
    if n == '' or m == '':
        return None
    n = int(n)
    m = int(m)
    if (n > m):
        if (m % 2 == 0):
            print('U')
        else:
            print('D')
    else:
        if (n % 2 == 0):
            print('L')
        else:
            print('R')


if __name__ == '__main__':
    
    for _ in range(int(input("Introduce el numero de veces a evaluar: "))):

        n = input("valor de n: ")
        m = input("valor de m: ")

        r = recorrido(n, m)

        if r != None:
            print('El valor de la salida es: {}'.format())
