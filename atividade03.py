#Sendo H = 1 +12+13+14+ ⋯ + +1n, escreva um programa para calcular o valor de H. O número n é lido.

def calculo_h(numero):
    h = 0
    while numero:
        h += 1/(numero)
        numero -= 1
    return h

def main():
    n = input()
    n = int(n)

    resultado = calculo_h(n)
    print(f'{resultado:.4f}')


if __name__ == '__main__':
    main()