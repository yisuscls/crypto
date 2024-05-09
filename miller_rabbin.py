import random

def miller_rabin(p, s):
    """
    Realiza la prueba de primalidad de Miller-Rabin, que es una prueba probabilística de primalidad.

    Entradas:
    - p (int): Número que se quiere probar si es primo.
    - s (int): Número de rondas de la prueba para aumentar la precisión.

    Salida:
    - bool: Devuelve True si p es probablemente primo, False si es compuesto.
    """
    if p == 2 or p == 3:
        return True  # 2 y 3 son números primos
    if p % 2 == 0 or p < 2:
        return False  # Devuelve False si p es par y mayor que 2, o si p es menor que 2

    # Escribir p-1 como d*2^r por medio de la extracción de factores de 2
    r, d = 0, p - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(s):
        a = random.randint(2, p - 2)
        x = pow(a, d, p)  # x = a^d % p
        if x == 1 or x == p - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, p)  # x = x^2 % p
            if x == p - 1:
                break
        else:
            return False  # p es compuesto

    return True  # p es probablemente primo

# Ejemplo de uso:
if __name__ == '__main__':
    p = 14983  # Candidato a primo
    s = 5   # Parámetro de seguridad
    if miller_rabin(p, s):
        print(f"{p} es probablemente primo")
    else:
        print(f"{p} es compuesto")
