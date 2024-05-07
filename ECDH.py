import sympy as sy
import random
class ECDH():
    def __init__(self,p=None,a=None,b=None):
        
        if p is None:
            self.p= sy.randprime(4,2**10)
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
        pass
    def check_point(self,point):
        x=point[0]
        y=point[1]
        if((y**2)%self.p!=(x**3 + self.a*x+self.b)%self.p):
            raise Exception("El punto no pertence a la curva creada")
        pass
    def key_creation(self):
        pass
        
    pass
if __name__ == '__main__':
    # se seleciona el p ,a,b para generar la curva
    ecdh= ECDH(p=17,a=2,b=2)
    # se seleciona un punto en la curva (x,y)
    p=(5,1)
    ecdh.check_point(p)