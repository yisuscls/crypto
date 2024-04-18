
class AffineCipher():
    letters_list=['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters=  {letter: index  for index, letter in enumerate(letters_list)}
   
   
    def __init__(self,a,b):
        self.a=a
        self.b=b
        pass
    
    def encrypt(self,x):
        
        encryptText=""
        
        for i in x:
            index= self.letters.get(i)
            newIndex= (self.a*index+self.b) % len(self.letters_list)
            encryptText+=self.letters_list[newIndex]

        return encryptText
    
    def decrypt(self,y):
        a=self.a
        b=self.b
        a_invert= self.__inverse(a,len(self.letters_list))
    
        if type(a_invert)==bool:
            return "a y 26 deben ser coprimos para que exista el inverso."
        decryptText= ""
        
        for i in y:
            index =self.letters.get(i)
            newIndex= (a_invert*(index-b)) % len(self.letters_list)
            decryptText+=self.letters_list[newIndex]
            
        return decryptText
    
    def __gcd(self,a, b):
        while b:
            a, b = b, a % b
        return a
    
    def __inverse(self,a,m):
        d0, d1, x0,x1= a,m,1,0
        while d1 != 0:
            q = d0 // d1
            d0, d1 = d1, d0 - q * d1
            x0, x1 = x1, x0 - q * x1
        if d0 == 1:
            return int(x0) % m
        else:
            return self.__gcd(a, m)>1

pass

if(__name__ == "__main__"):
    message=input("Insert message: ")
    a=int( input("Insert the value of a: "))
    b=int(input("Insert the value of b: "))
    affineCipher= AffineCipher(a,b)
    
    y=affineCipher.encrypt(message)
    print("\nMessage encrypted :")
    print(y)
    print("\nMessage decrypted :")
    print(affineCipher.decrypt(y))
    