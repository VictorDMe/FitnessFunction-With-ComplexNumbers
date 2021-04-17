import cmath

for x in range(0, 11):
    a = x / 10
    for y in range(-10, 11):
        b = y / 10
        numero = complex(a, b)
        conta = (-(pow(numero, 3)) + 4 * (pow(numero, 2)) - 6 * numero + 4) / 5

        modulo = cmath.sqrt(conta.imag**2 + conta.real**2)

        if modulo.real > 0.90:
            print("\033[34m" + "Número complexo:" + "\033[0;0m" + f" {numero}")
            #print(f"Resultado da função polinomial: {conta}")
            print("\033[34m" + "A porcentagem de conveniência é de:" + "\033[0;0m" f" {round((modulo.real * 100), 2)}%")
            print("")
