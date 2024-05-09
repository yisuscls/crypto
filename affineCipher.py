import random
class AffineCipher():
    # Lista de letras permitidas en el cifrado.
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Diccionario para mapear cada letra a su índice correspondiente.
    letters = {letter: index for index, letter in enumerate(letters_list)}

    def __init__(self, a=None, b=None):
        """
        Constructor de la clase AffineCipher.
        Parámetros:
        - a (int): Coeficiente 'a' del cifrado afín.
        - b (int): Coeficiente 'b' del cifrado afín.
        """
        #si no se ingresan los valores se selecionan de forma aleatoria
        if  a is None:
            a=self.select_a(random.randint(1,len(self.letters_list)))
        if b is None:
            b=random.randint(1,len(self.letters_list))
        if type(self.inverse(a, len(self.letters_list))) == bool:
            raise Exception(f"El valor de 'a' es invalido, 'a' debe ser coprimo de {len(self.letters_list)}")
        self.a = a
        self.b = b

    def select_a(self,a):
        if type(self.inverse(a, len(self.letters_list))) == bool:
            return self.select_a(random.randint(1,len(self.letters_list)))
        return a

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
    # El mensaje a cifrar.
    message = "Hola"
    # se generan los coeficientes a y b para el cifrado de forma aleatoria pero tambien 
    # pueden pasar como parametros: AffineCipher(a,b)
    affineCipher = AffineCipher()

    # Cifrar el mensaje y mostrar el resultado.
    y = affineCipher.encrypt(message)
    # Descifrar el mensaje cifrado y mostrar el resultado original.
    decrypt=affineCipher.decrypt(y)
    
    # Imprimir los coeficientes a y b usados en el cifrado
    print(f"Coeficientes para el cifrado afín: a = {affineCipher.a}, b = {affineCipher.b}")
    # Cifrar el mensaje y mostrar el resultado.
    print(f"Mensaje cifrado: {y}")
    # Descifrar el mensaje cifrado y mostrar el resultado original.
    print(f"Mensaje descifrado: {decrypt}")
    print(f"Mensaje original: {message}")
