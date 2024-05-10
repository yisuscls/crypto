import random

def prueba_de_primalidad_fermat(p, s):
    """
    Realiza la prueba de primalidad de Fermat para determinar si un número es probablemente primo.

    Entradas:
    - p (int): Número que se quiere probar si es primo.
    - s (int): Número de veces que se realizará la prueba, conocido como parámetro de seguridad.

    Salida:
    - bool: Devuelve True si p es probablemente primo, False si es compuesto.
    """
    if p == 2:
        return True  # 2 es un número primo
    if not p & 1:
        return False  # Devuelve Falso si p es par y diferente de 2
    
    for _ in range(s):
        a = random.randint(2, p - 2)  # Escoge un a aleatorio entre 2 y p-2
        if pow(a, p-1, p) != 1:  # Calcula a^(p-1) % p usando la función pow incorporada de Python
            return False  # p es compuesto
    return True  # p es probablemente primo

# Ejemplo de uso:
if __name__ == '__main__':
    print("Prueba de primalidad de Fermat")
    p = 91  # Candidato a primo
    s = 5   # Parámetro de seguridad
    print("Numero a validar si es problamente primo:",p)
    print("Factor de seguridad",s)
    if prueba_de_primalidad_fermat(p, s):
        print(f"{p} es probablemente primo")
    else:
        print(f"{p} es compuesto")
