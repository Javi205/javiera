def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    lista_primos = []
    for i in range(1,numero):
        if es_primo(i):
            lista_primos.append(i)
        else:
            pass
    return lista_primos

print(es_primo(7))