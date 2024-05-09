import sympy as sy
import random
import miller_rabbin as mr
class ECDH():
    def __init__(self,p=None,a=None,b=None):
        
        if p is None:
            self.p= self.generate_prime()
        else:
            if p <=3:
                raise Exception('p  debe ser mayor que 3')
            self.p= p
        if a==None or b==None:
            print("Warning: se selecionaran los valores de a y b de forma aleatoria por que no se ingresaron ambos parametros.\n")
            while True:
                self.a= random.randint(1,self.p-1)
                self.b= random.randint(1,self.p-1)
                test=(4* (self.a**3) +27 *(self.b**2))%self.p
                if test!=0:
                    break
        else:
            self.a= a
            self.b= b
        test=(4* (self.a**3) +27 *(self.b**2))%self.p
        if test==0:
            raise Exception("Los valores de a y b no cumplen con la condicion de 4*a^3+27*b^2 !=0")
        print("#E esta entre",round(self.p+1-2*(self.p**(0.5))), "y",round(self.p+1+2*(self.p**(0.5))))
        self.E_min=round(self.p+1-2*(self.p**(0.5)))
        self.E_max=round(self.p+1+2*(self.p**(0.5)))
        pass
    def check_point(self,point):
        x=point[0]
        y=point[1]
        if((y**2)%self.p!=(x**3 + self.a*x+self.b)%self.p):
            raise Exception(f"El punto ({x},{y}) no pertence a la curva x**3 + {self.a}*x+{self.b} creada")
        pass
    def key_creation(self,P):
        # Creación de las llaves para Alice
        self.E= self.find_E(P)
        self.a = random.randint(2, self.E_min)
        self.A = self.scalar_mul(self.a,P)

        # Creación de las llaves para Bob
        self.b = random.randint(2, self.E_min)
        self.B = self.scalar_mul(self.b,P)

        # Computar la clave compartida por Bob
        self.KmBob =self.scalar_mul(self.b,self.A)

        # Computar la clave compartida por Alice
        self.KmAlice = self.scalar_mul(self.a,self.B)
        self.Km=self.KmAlice
        if self.KmAlice == self.KmBob : 
            return self.a, self.A,self.KmAlice,self.b, self.B, self.KmBob
        return self.key_creation(P)
    def generate_prime(self):
        while True:
            p=random.getrandbits(1024)
            if mr.miller_rabin(p,15):
                return p
    def select_point(self):
        x=random.randint(1,self.p-1)
        y=((x**3 + self.a*x+self.b)%self.p)**(0.5)
        return (x,y)
    def addition(self,P,Q):
        if(P==Q):
            num=3*(P[0]**2)+self.a
            den=2*P[1]
            den=self.inverse(den,self.p)
        else:
            num=Q[1]-P[1]
            den=Q[0]-P[0]
            den=self.inverse(den,self.p)
        s= num*den%self.p
        x=(s*s-P[0]-Q[0]) %self.p
        y=(s*(P[0]-x)-P[1]) %self.p
        return(x,y)
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
    def scalar_mul(self, d, P):
        T=P
        d_bin=bin(d)[2:]
        for di in d_bin[1:]:
            T = self.addition(T,T)
            if di == '1':
                T = self.addition(T,P)
        return T
    def find_E(self,P):
        for E in range(self.E_min, self.E_max):
            if self.scalar_mul(E,P)==(P[0],self.p-P[1]):
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