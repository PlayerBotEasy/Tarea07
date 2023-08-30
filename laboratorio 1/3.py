def encontrar_primos_menores_que(n):
    primos = []
    for numero in range(2, n):
        if es_primo(numero):
            primos.append(numero)
    return primos

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese un número: "))
primos_menores_que_n = encontrar_primos_menores_que(n)
print("Los números primos menores que", n, "son:", primos_menores_que_n)
