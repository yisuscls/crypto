import random
from sq_mul import square_and_multiply
import miller_rabbin as mr

class Elgamal():
    def __init__(self, p=None, alfa=None):
        """
        Inicializa una instancia de ElGamal, generando valores p y alfa si no se proporcionan.
        p debe ser un número primo y alfa un generador en el grupo multiplicativo de Z/pZ.

        Entradas:
        - p (int, opcional): Un número primo grande.
        - alfa (int, opcional): Un generador del grupo multiplicativo de Z/pZ.

        Si p o alfa no se proporcionan, se generan automáticamente.
        """
        if p is None:
            self.p = self.generate_prime()  # Genera un primo p si no se proporciona
            self.alfa = random.randint(2, self.p - 2)  # Selecciona un alfa aleatorio
        else:
            self.p = p
            if alfa is None:
                self.alfa = random.randint(2, self.p - 2)  # Selecciona un alfa si no se proporciona
            else:
                self.alfa = alfa
                
    def key_creation(self):
        """
        Genera las claves públicas y privadas para dos entidades, Alice y Bob, y computa las claves compartidas.

        Salida:
        - tuple: Contiene las claves privadas y públicas de Alice y Bob, y las claves compartidas.
        """
        # Claves para Alice
        self.a = random.randint(2, self.p - 2)  # Valor privado de Alice
        self.A = square_and_multiply(self.alfa, self.a, self.p)  # Llave pública de Alice

        # Claves para Bob
        self.b = random.randint(2, self.p - 2)  # Valor privado de Bob
        self.B = square_and_multiply(self.alfa, self.b, self.p)  # Llave pública de Bob

        # Claves compartidas calculadas por Bob y Alice
        self.KmBob = square_and_multiply(self.A, self.b, self.p)
        self.KmAlice = square_and_multiply(self.B, self.a, self.p)
        
        # Verificar que existe inverso para Km en Z/pZ
        self.Km = self.KmAlice
        self.Km_inv = self.inverse(self.Km, self.p)
        if type(self.Km_inv) == bool:
            raise Exception("No existe inverso para Km")
        
        return self.a, self.A, self.KmAlice, self.b, self.B, self.KmBob

    def encrypt(self, x):
        """
        Cifra un mensaje x usando la clave compartida Km.

        Entrada:
        - x (int): Mensaje a cifrar.

        Salida:
        - int: Mensaje cifrado.
        """
        return (x * self.Km) % self.p

    def decrypt(self, y):
        """
        Descifra un mensaje y usando el inverso de la clave compartida Km_inv.

        Entrada:
        - y (int): Mensaje cifrado.

        Salida:
        - int: Mensaje descifrado.
        """
        return (y * self.Km_inv) % self.p

    def gcd(self, a, b):
        """
        Calcula el máximo común divisor de a y b.

        Entrada:
        - a (int): Primer número.
        - b (int): Segundo número.

        Salida:
        - int: MCD de a y b.
        """
        while b:
            a, b = b, a % b
        return a

    def inverse(self, a, m):
        """
        Calcula el inverso modular de a bajo m.

        Entrada:
        - a (int): Número.
        - m (int): Módulo.

        Salida:
        - int/bool: Inverso modular si existe, False si no.
        """
        d0, d1, x0, x1 = a, m, 1, 0
        while d1 != 0:
            q = d0 // d1
            d0, d1 = d1, d0 - q * d1
            x0, x1 = x1, x0 - q * x1
        if d0 == 1:
            return int(x0) % m
        else:
            return False

    def generate_prime(self):
        """
        Genera un número primo de 1024 bits usando el test de primalidad de Miller-Rabin.

        Salida:
        - int: Un número primo.
        """
        while True:
            p = random.getrandbits(1024)
            if mr.miller_rabin(p, 15):
                return p

# Código para ejecutar y probar la clase ElGamal
if __name__ == "__main__":
    # Creación de una instancia de ElGamal con p y alfa aleatorios
    gamal = Elgamal()
    p = gamal.p
    alfa = gamal.alfa
    
    print(f"Primo seleccionado (p): {p}\n")
    print(f"Alfa seleccionado: {alfa}\n")
    # Generación de claves
    a, A, KmAlice, b, B, KmBob = gamal.key_creation()
    
    print(f"Valor privado de Alice (a): {a}\n")
    print(f"Llave pública de Alice (A): {A}\n")
    print(f"Valor privado de Bob (b): {b}\n")
    print(f"Llave pública de Bob (B): {B}\n")
    print(f"Clave compartida calculada por Bob: {KmBob}\n")
    print(f"Clave compartida calculada por Alice: {KmAlice}\n")
    print(f"¿Las claves compartidas son iguales? {'Sí' if KmAlice == KmBob else 'No'}\n")
    
    # Mensaje original
    message = 128931746817246817642873618236871268736
    print(f"Mensaje original: {message}")

    # Cifrado del mensaje
    encrypt = gamal.encrypt(message)
    print(f"Mensaje cifrado: {encrypt}")

    # Descifrado del mensaje
    decrypt = gamal.decrypt(encrypt)
    print(f"Mensaje descifrado: {decrypt}")
