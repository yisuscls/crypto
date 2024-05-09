class AffineCipher():
    # Lista de letras permitidas en el cifrado.
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Diccionario para mapear cada letra a su índice correspondiente.
    letters = {letter: index for index, letter in enumerate(letters_list)}

    def __init__(self, a, b):
        """
        Constructor de la clase AffineCipher.
        Parámetros:
        - a (int): Coeficiente 'a' del cifrado afín.
        - b (int): Coeficiente 'b' del cifrado afín.
        """
        self.a = a
        self.b = b

    def encrypt(self, x):
        """
        Método para cifrar un mensaje usando cifrado afín.
        Parámetros:
        - x (str): Mensaje en texto plano a cifrar.
        Devuelve:
        - encryptText (str): Mensaje cifrado.
        """
        encryptText = ""
        
        for i in x:
            i = i.lower()
            if i in self.letters_list:
                index = self.letters.get(i)
                newIndex = (self.a * index + self.b) % len(self.letters_list)
                encryptText += self.letters_list[newIndex]
            else:
                encryptText += i

        return encryptText

    def decrypt(self, y):
        """
        Método para descifrar un mensaje cifrado con cifrado afín.
        Parámetros:
        - y (str): Mensaje cifrado a descifrar.
        Devuelve:
        - decryptText (str): Mensaje descifrado.
        """
        a_invert = self.inverse(self.a, len(self.letters_list))
    
        if type(a_invert) == bool:
            return "a y 26 deben ser coprimos para que exista el inverso."
        decryptText = ""
        
        for i in y:
            i = i.lower()
            if i in self.letters_list:
                index = self.letters.get(i)
                newIndex = (a_invert * (index - self.b) % len(self.letters_list))
                decryptText += self.letters_list[newIndex]
            else:
                decryptText += i
        return decryptText

    def gcd(self, a, b):
        """
        Método para calcular el máximo común divisor (MCD) de dos números.
        Parámetros:
        - a (int): Primer número.
        - b (int): Segundo número.
        Devuelve:
        - a (int): MCD de a y b.
        """
        while b:
            a, b = b, a % b
        return a

    def inverse(self, a, m):
        """
        Método para encontrar el inverso multiplicativo de 'a' modulo 'm'.
        Parámetros:
        - a (int): Número del que se busca el inverso.
        - m (int): Módulo.
        Devuelve:
        - x0 (int) o bool: Inverso multiplicativo de 'a' modulo 'm', o False si no existe.
        """
        d0, d1, x0, x1 = a, m, 1, 0
        while d1 != 0:
            q = d0 // d1
            d0, d1 = d1, d0 - q * d1
            x0, x1 = x1, x0 - q * x1
        if d0 == 1:
            return int(x0) % m
        else:
            return self.gcd(a, m) > 1

if __name__ == "__main__":
    # Solicitar al usuario que ingrese el mensaje a cifrar.
    message = input("Insert message: ")
    # Solicitar al usuario los coeficientes 'a' y 'b' del cifrado afín.
    a = int(input("Insert the value of a: "))
    b = int(input("Insert the value of b: "))
    # Crear una instancia de AffineCipher con los coeficientes proporcionados.
    affineCipher = AffineCipher(a, b)

    # Cifrar el mensaje y mostrar el resultado.
    y = affineCipher.encrypt(message)
    print("\nMessage encrypted:")
    print(y)
    # Descifrar el mensaje cifrado y mostrar el resultado original.
    print("\nMessage decrypted:")
    print(affineCipher.decrypt(y))
