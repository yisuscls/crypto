
import random 
import miller_rabbin as mr
import sq_mul as sm
#usar test primo
class RSA():
    def __init__(self,p=None, q=None,e=None,d=None) -> None:
        """
        Inicializa una instancia de RSA con parámetros opcionales para los primos p y q, y las llaves e, d.
        Si p y q no son proporcionados, se generan automáticamente como primos grandes.
        Si e y d no son proporcionados, se generan a partir de p y q.

        Entradas:
        - p (int, opcional): Número primo p.
        - q (int, opcional): Número primo q.
        - e (int, opcional): llave pública e.
        - d (int, opcional): llave privada d.

        Excepciones:
        - Levanta una excepción si los valores dados de e y d no son inversos modulares adecuados.
        """
        if p is  None:
            p = self.generate_prime()
        if q is  None:
            q = self.generate_prime()
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
        """
        Genera una llave pública e y privada d que sean inversos modulares bajo phi_n.
        
        Entrada:
        - phi_n (int): Valor de la función totient de Euler para n = p*q.
        
        Salida:
        Establece internamente las variables self.e y self.d.
        """
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
        """
        Calcula el máximo común divisor de a y b usando el algoritmo de Euclides.
        
        Entradas:
        - a (int): Primer número.
        - b (int): Segundo número.
        
        Salida:
        - int: Máximo común divisor de a y b.
        """
        while b:
            a, b = b, a % b
        return a
    
    def inverse(self,a,m):
        """
        Calcula el inverso modular de a bajo m usando el algoritmo de Euclides extendido.
        
        Entradas:
        - a (int): Número del que se busca el inverso.
        - m (int): Módulo.
        
        Salida:
        - int/bool: Inverso modular de a bajo m si existe, False si no existe.
        """
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
        """
        Cifra un mensaje x usando la llave pública e y el módulo n.
        
        Entrada:
        - x (int): Mensaje a cifrar.
        
        Salida:
        - int: Mensaje cifrado.
        """
        return sm.square_and_multiply(x,self.e,self.n)
    def decrypt(self,y):
        """
        Descifra un mensaje y usando la llave privada d y el módulo n.
        
        Entrada:
        - y (int): Mensaje cifrado.
        
        Salida:
        - int: Mensaje descifrado.
        """
        return  sm.square_and_multiply(y,self.d,self.n)
    def generate_prime(self):
        """
        Genera un número primo grande usando el test de primalidad de Miller-Rabin.
        
        Salida:
        - int: Un número primo de 1024 bits.
        """
        while True:
            p=random.getrandbits(1024)
            if mr.miller_rabin(p,15):
                return p
    pass
if __name__ == '__main__':
    #insertar los valores de p y q que son ambos numeros primos
    rsa= RSA()
    #mensaje a encriptar
    message=20
    #encripción del mensaje
    encrypt=rsa.encrypt(message)
    # desencriptar el mensaje
    decrypt=rsa.decrypt(encrypt)
    #mostras los resultados obtenidos y los valores de e y d que se escogieron 
    print(f"p: {rsa.p}\n\nq: {rsa.q}\n\nn: {rsa.n}\n\ne: {rsa.e}\n\nd: {rsa.d}")
    # Cifrado del mensaje y muestra del resultado.
    print("\nMensaje Cifrado :\n",encrypt)
    # Descifrado del mensaje cifrado y muestra del resultado.
    print("\nMensaje Descifrado:\n",decrypt)
    # mensaje Original
    print("\nMensaje Original: \n", message)
    