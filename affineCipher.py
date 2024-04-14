
class AffineCipher():
    letters_list=[' ','ñ' ,'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters=  {letter: index  for index, letter in enumerate(letters_list)}
    def __init__(self,message):
        self.x = message
        pass
    
    def encrypt(self,a,b):
        
        encryptText=""
        
        for i in self.x:
            index= self.letters.get(i)
            newIndex= (a*index+b) %len(self.letters_list)
            encryptText+=self.letters_list[newIndex]

        return encryptText
    
    def decrypt(self,y,a,b):
        
        a_invert= self.__inverse(a,len(self.letters_list))
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
    affineCipher= AffineCipher(message)
    y=affineCipher.encrypt(1,2)
    print(y)
    print(affineCipher.decrypt(y,1,2))
    