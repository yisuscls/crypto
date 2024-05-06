def square_and_multiply(x, H, n):
    # Convert H to binary
    h = bin(H)[2:]  # Remove the '0b' prefix and get the binary representation as a string
    if __name__ == '__main__':
        print("H:",h)
    # Initialize r with x
    r = x

    # Traverse the binary representation of H from the second most significant bit to the least significant bit
    for bit in h[1:]:  # Skip the first bit because r is already initialized to x
        r = (r * r) % n  # Square step
        if bit == '1':
            r = (r * x) % n  # Multiply step if the current bit is 1

    return r
if __name__ == '__main__':
    # ejemplo de uso
    x = 3  # BASE
    H = 13  # Exponente
    n = 17  # Modulo
    result = square_and_multiply(x, H, n)
    print(f"The result of {x}^{H} mod {n} is {result}")
