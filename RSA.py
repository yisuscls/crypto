import math
import random 
class RSA():
    def __init__(self,p,q,e=None,d=None) -> None:
        self.p = p
        self.q = q
        self.n = p*q
        phi_n=(self.p-1)*(self.q-1)
        if(e is None and d is None):
            self.key_generation(phi_n)
        elif(e is None ):
            self.e=self.inverse(d,phi_n)
            if(type(self.e)==bool):
                self.e=None
                raise Exception(f"e no tiene inverso en Z{phi_n}")
            self.d = d
        elif(d is None):
            self.e=e
            self.d = self.inverse(e,phi_n)
            if(type(self.d)==bool):
                self.d=None
                raise Exception(f"d no tiene inverso en Z{phi_n}")
        else:
            if(((e*d)%phi_n)==1):
                self.e=e
                self.d=d
            else:
                raise Exception(f"e y d no son inversos en Z{phi_n}")
        pass
    def key_generation(self,phi_n):
        # choose e
        while True:
            e=random.randint(2, phi_n)
            while True:
                if(self.gcd(e, phi_n)==1):
                    break
                else:
                    e=random.randint(2, phi_n)
            self.e=e
            d=self.inverse(e, phi_n)
            if type(d)==bool or d==e:
                continue
            else:
                break
            
        self.d=d
        pass
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
    def encrypt(self,x):
        return (x**(self.e))%self.n
    def decrypt(self,y):
        return (y**(self.d))%self.n
    pass
if __name__ == '__main__':
    #insertar los valores de p y q que son ambos numeros primos
    rsa= RSA(7,11)
    #mensaje a encriptar
    message=20
    #encripción del mensaje
    encrypt=rsa.encrypt(message)
    # desencriptar el mensaje
    decrypt=rsa.decrypt(encrypt)
    #mostras los resultados obtenidos y los valores de e y d que se escogieron 
    print(f"e= {rsa.e}; d= {rsa.d}")
    print("Encrypted Text:", encrypt)
    print("Decrypted Text:", decrypt)
    print("Original  Text:", message)
    