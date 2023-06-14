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


dato = int(input("Que numero quieres ingresar: "))
a = input("Que funcion quieres utilizar: (primera/segunda/ambas): ")

if a == "primera":
    print(es_primo(dato))
elif a == "segunda":
    print(primos(dato))
else:
    print(es_primo(dato))
    print(primos(dato))


def des_prima(numero):
    factores_primos = []
    
    if es_primo(numero):
        factores_primos.append(numero)
        return factores_primos
    
    primos_menores = primos(numero)
    for primo in primos_menores:
        while numero % primo == 0:
            numero = numero // primo
            factores_primos.append(primo)
    
    return factores_primos

