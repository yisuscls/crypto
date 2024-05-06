import random

def miller_rabin(p, s):
    if p == 2 or p == 3:
        return True
    if p % 2 == 0 or p < 2:
        return False

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
