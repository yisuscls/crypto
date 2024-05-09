import sympy as sy
import random
from sq_mul import square_and_multiply
import miller_rabbin as mr

class Elgamal():
    def __init__(self,p=None,alfa=None)->None:
        if p is None  :
            # Seleccionar un primo p entre 2^1023 y 2^1024
            self.p = self.generate_prime()
            # seleccionar un a 
            self.alfa =   random.randint(2,self.p-2)
            return
        else :
            self.p =p
            if alfa is None:
                self.alfa = random.randint(2,self.p-2)
            else :
                self.alfa = alfa
                
    def key_creation(self):
        # Creación de las llaves para Alice
        self.a = random.randint(2, self.p-2)
        self.A = square_and_multiply(self.alfa, self.a, self.p)

        # Creación de las llaves para Bob
        self.b = random.randint(2, self.p-2)
        self.B = square_and_multiply(self.alfa, self.b, self.p)

        # Computar la clave compartida por Bob
        self.KmBob = square_and_multiply(self.A, self.b, self.p)

        # Computar la clave compartida por Alice
        self.KmAlice = square_and_multiply(self.B, self.a, self.p)
        self.Km=self.KmAlice
        self.Km_inv=self.inverse(self.Km,self.p)
        if type(self.Km_inv)== bool:
            raise Exception(" No existe inverso para Km")
        return self.a, self.A,self.KmAlice,self.b, self.B, self.KmBob
    def encrypt(self,x):
        return (x*self.Km)%self.p
    def decrypt(self,y):
        return (y*self.Km_inv)%self.p
    
    def gcd(self,a, b):
        while b:
            a, b = b, a % b
        return a
    
    def inverse(self,a,m):
        d0, d1, x0,x1= a,m,1,0
        while d1 != 0:
            q = d0 // d1
            d0, d1 = d1, d0 - q * d1
            x0, x1 = x1, x0 - q * x1
        if d0 == 1:
            return int(x0) % m
        else:
            return self.gcd(a, m)>1
    def generate_prime(self):
        while True:
            p=random.getrandbits(1024)
            if mr.miller_rabin(p,15):
                return p
    pass

if __name__ == "__main__":
    #  creacion de p y alfa aleatoriamente
    gamal=Elgamal()
    p=gamal.p
    alfa= gamal.alfa
    
    print(f"Primo seleccionado (p): {p}\n")
    print(f"Alfa seleccionado: {alfa}\n")
    # creacion de llaves
    a, A,KmAlice,b, B, KmBob=gamal.key_creation()
    
    print(f"Valor privado de Alice (a): {a}\n")
    print(f"Llave pública de Alice (A): {A}\n")
    print(f"Valor privado de Bob (b): {b}\n")
    print(f"Llave pública de Bob (B): {B}\n")
    print(f"Clave compartida calculada por Bob: {KmBob}\n")
    print(f"Clave compartida calculada por Alice: {KmAlice}\n")
    print(f"¿Las claves compartidas son iguales? {'Sí' if KmAlice == KmBob else 'No'}\n")
    
    # Original message
    message = 128931746817246817642873618236871268736
    print(f"Original message: {message}")

    # Encrypting the message
    encrypt = gamal.encrypt(message)
    print(f"Encrypted message: {encrypt}")

    # Decrypting the message
    decrypt = gamal.decrypt(encrypt)
    print(f"Decrypted message: {decrypt}")

