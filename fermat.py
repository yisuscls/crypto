import random

def prueba_de_primalidad_fermat(p, s):
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
    p = 17  # Candidato a primo
    s = 5   # Parámetro de seguridad
    if prueba_de_primalidad_fermat(p, s):
        print(f"{p} es probablemente primo")
    else:
        print(f"{p} es compuesto")