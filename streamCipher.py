import random

class StreamCipher():
    def __init__(self, key=None):
        """
        Constructor de la clase StreamCipher.
        Parámetros:
        - key (str, opcional): Clave binaria predefinida para cifrado y descifrado. Si no se proporciona, se puede generar una.
        """
        self.key = key
        
    def encrypt(self, x):
        """
        Método para cifrar un mensaje binario usando una clave de flujo.
        Parámetros:
        - x (str): Mensaje binario en texto plano a cifrar.
        
        Devuelve:
        - yi (str): Mensaje cifrado.
        """
        if self.key is  None:
            self.generateKey(len(x))
        if len(self.key)!=len(x):
            raise Exception("El tamaño de la llave y del mensaje deben ser el mismo")
        si = 0
        yi = ""
        for x1 in x:
            yi += str((int(x1) + int(self.key[si])) % 2)
            si += 1
        return yi
    
    def decrypt(self, y):
        """
        Método para descifrar un mensaje binario cifrado usando la misma clave de flujo.
        Parámetros:
        - y (str): Mensaje binario cifrado a descifrar.
        
        Devuelve:
        - xi (str): Mensaje descifrado.
        """
        si = 0
        xi = ""
        for yi in y:
            xi += str((int(yi) + int(self.key[si])) % 2)
            si += 1
        return xi

    def generateKey(self, length):
        """
        Método para generar una clave binaria aleatoria de longitud específica.
        Parámetros:
        - length (int): Longitud de la clave a generar.
        
        Establece:
        - key (str): Clave binaria generada.
        """
        key = ""
        for _ in range(length):
            key += str(random.randint(0, 1))
        self.key = key

    def getKey(self):
        """
        Método para obtener la clave actual del cifrador.
        
        Devuelve:
        - key (str): Clave actual del cifrador.
        """
        return self.key

if __name__ == "__main__":
    # Mensaje binario de ejemplo a cifrar.
    message = "101010101010101001101110110111"
    # Creación de una instancia de StreamCipher.
    # se puede ingresar la llave como para metro pero debe ser un 
    # un string de 1 y 0 del mismo tamaño que el mensaje
    streamCipher = StreamCipher()
    y = streamCipher.encrypt(message)
    
    print("llave: \n", streamCipher.key)
    
    # Cifrado del mensaje y muestra del resultado.
    print("\nMensaje Cifrado :\n",y)
    

    
    # Descifrado del mensaje cifrado y muestra del resultado.
    print("\nMensaje Descifrado:\n",streamCipher.decrypt(y))
    # mensaje Original
    print("\nMensaje Original: \n", message)
