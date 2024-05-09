import sympy as sy
import random
import miller_rabbin as mr

class ECDH():
    def __init__(self, p, a=None, b=None):
        """
        Inicializa una instancia de ECDH, configurando una curva elíptica sobre un campo finito.
        Parámetros:
        - p (int): Un número primo que define el tamaño del campo finito.
        - a (int, opcional): Coeficiente a de la ecuación de la curva elíptica.
        - b (int, opcional): Coeficiente b de la ecuación de la curva elíptica.
        
        Si 'a' o 'b' no se proporcionan, se seleccionarán valores aleatorios que satisfagan la condición 
        de no singularidad de la curva, 4*a^3 + 27*b^2 != 0 mod p.
        """
        if p <= 3:
            raise Exception('p debe ser mayor que 3')
        self.p = p
        if a is None or b is None:
            print("Warning: se seleccionarán los valores de a y b de forma aleatoria porque no se ingresaron ambos parámetros.\n")
            while True:
                self.a = random.randint(1, self.p-1)
                self.b = random.randint(1, self.p-1)
                if (4 * (self.a ** 3) + 27 * (self.b ** 2)) % self.p != 0:
                    break
        else:
            self.a = a
            self.b = b

        # Verifica que los coeficientes cumplan la condición de no singularidad
        if (4 * (self.a ** 3) + 27 * (self.b ** 2)) % self.p == 0:
            raise Exception("Los valores de a y b no cumplen con la condición de 4*a^3 + 27*b^2 != 0")

        # Imprime los límites estimados del número de puntos en la curva
        print("#E está entre", round(self.p + 1 - 2 * (self.p ** 0.5)), "y", round(self.p + 1 + 2 * (self.p ** 0.5)))
        self.E_min = round(self.p + 1 - 2 * (self.p ** 0.5))
        self.E_max = round(self.p + 1 + 2 * (self.p ** 0.5))

    def check_point(self, point):
        """
        Verifica si un punto dado pertenece a la curva elíptica definida por la instancia.

        Parámetros:
        - point (tuple): Un punto (x, y) a verificar.

        Levanta una excepción si el punto no se encuentra en la curva.
        """
        x, y = point
        if (y ** 2) % self.p != (x ** 3 + self.a * x + self.b) % self.p:
            raise Exception(f"El punto ({x},{y}) no pertenece a la curva x**3 + {self.a}*x + {self.b} creada")

    def key_creation(self, P):
        """
        Genera las llaves públicas y privadas para dos participantes (Alice y Bob) y calcula la clave compartida.

        Parámetros:
        - P (tuple): Punto base en la curva elíptica.

        Salida:
        - tuple: Contiene las claves privadas y públicas de Alice y Bob, y las claves compartidas.
        """
        # Generación de llaves para Alice y Bob, y computación de claves compartidas
        self.E = self.find_E(P)
        self.alfa = random.randint(2, self.E)
        self.A = self.scalar_mul(self.alfa, P)

        self.beta = random.randint(2, self.E)
        self.B = self.scalar_mul(self.beta, P)

        self.KmBob = self.scalar_mul(self.beta, self.A)
        self.KmAlice = self.scalar_mul(self.alfa, self.B)
        self.Km = self.KmAlice

        return self.alfa, self.A, self.KmAlice, self.beta, self.B, self.KmBob

    def addition(self, P, Q):
        """
        Suma dos puntos P y Q en la curva elíptica.
        
        Parámetros:
        - P (tuple): Primer punto en la curva.
        - Q (tuple): Segundo punto en la curva.

        Salida:
        - tuple: El resultado de la suma P + Q.
        """
        if P == Q:
            num = 3 * (P[0] ** 2) + self.a
            den = 2 * P[1]
        else:
            num = Q[1] - P[1]
            den = Q[0] - P[0]

        den = self.inverse(den, self.p)  # Inverso modular del denominador
        s = num * den % self.p
        x = (s * s - P[0] - Q[0]) % self.p
        y = (s * (P[0] - x) - P[1]) % self.p
        return (x, y)

    def inverse(self, a, m):
        """
        Calcula el inverso multiplicativo de 'a' modulo 'm' usando el algoritmo extendido de Euclides.
        Parámetros:
        - a (int): Elemento del que se busca el inverso.
        - m (int): Módulo.
        Devuelve:
        - int o bool: El inverso de 'a' modulo 'm' si existe, de lo contrario False.
        """
        d0, d1, x0, x1 = a, m, 1, 0
        while d1:
            q = d0 // d1
            d0, d1 = d1, d0 - q * d1
            x0, x1 = x1, x0 - q * x1
        if d0 == 1:
            return int(x0) % m
        else:
            return False

    def scalar_mul(self, d, P):
        """
        Multiplica un punto P de la curva elíptica por un escalar d.
        
        Parámetros:
        - d (int): Escalar por el cual multiplicar el punto.
        - P (tuple): Punto en la curva elíptica.

        Salida:
        - tuple: Punto resultante de la multiplicación escalar.
        """
        T = P
        d_bin = bin(d)[2:]  # Binario de d
        for di in d_bin[1:]:
            T = self.addition(T, T)
            if di == '1':
                T = self.addition(T, P)
        return T

    def find_E(self, P):
        """
        Encuentra el orden del punto P en la curva, buscando en el rango [E_min, E_max].

        Parámetros:
        - P (tuple): Punto base en la curva.

        Salida:
        - int: Orden del punto P.
        """
        for E in range(self.E_min, self.E_max):
            if self.scalar_mul(E, P) == (P[0], self.p - P[1]):
                return E
    pass
if __name__ == '__main__':
    # se seleciona el p ,a,b para generar la curva
    ecdh= ECDH(p=17,a=2,b=2)
    # se seleciona un punto en la curva (x,y)
    p=(5,1)

    ecdh.check_point(p)
    a, A,KmAlice,b, B, KmBob=ecdh.key_creation(p)
    print(f"Valor privado de Alice (a): {a}\n")
    print(f"Llave pública de Alice (A): {A}\n")
    print(f"Valor privado de Bob (b): {b}\n")
    print(f"Llave pública de Bob (B): {B}\n")
    print(f"Clave compartida calculada por Bob: {KmBob}\n")
    print(f"Clave compartida calculada por Alice: {KmAlice}\n")
    print(f"¿Las claves compartidas son iguales? {'Sí' if KmAlice == KmBob else 'No'}\n")