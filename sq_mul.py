def square_and_multiply(x, H, n):
    """
    Realiza la exponenciación modular usando el método de 'Square and Multiply' (Cuadrado y Multiplicación).

    Entradas:
    - x (int): Base del exponente, es el número que se va a elevar a la potencia H.
    - H (int): Exponente al que se eleva la base x.
    - n (int): Módulo bajo el cual se realiza la operación.

    Salida:
    - int: Resultado de x^H mod n.
    """
    # Convertir H a binario
    h = bin(H)[2:]  # Elimina el prefijo '0b' y obtiene la representación binaria como cadena
    if __name__ == '__main__':
        print("H:", h)
    # Inicializa r con x
    r = x

    # Recorre la representación binaria de H desde el segundo bit más significativo hasta el menos significativo
    for bit in h[1:]:  # Omite el primer bit porque r ya está inicializado a x
        r = (r * r) % n  # Paso de cuadrado
        if bit == '1':
            r = (r * x) % n  # Paso de multiplicación si el bit actual es 1

    return r

if __name__ == '__main__':
    # Ejemplo de uso
    x = 3  # BASE
    H = 13  # Exponente
    n = 17  # Módulo
    result = square_and_multiply(x, H, n)
    print(f"El resultado de {x}^{H} mod {n} es {result}")
