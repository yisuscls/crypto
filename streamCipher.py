import random
class StreamCipher():
    def __init__(self,key=None):
        if(key is not None):
            self.key = key
    def encrypt(self,x):
        si=0
        yi=""
        for x1 in x:
            yi+=str(( int(x1) +int(self.key[si])) %2)
            si+=1
        return yi
    
    def decrypt(self,y):
        si=0
        xi=""
        for yi in y:
            xi+=str(( int(yi) +int(self.key[si])) %2)
            si+=1
        return xi
    def generateKey(self,length):
        key=""
        for _ in range(length):
            key+= str(random.randint(0,1))
        self.key=key
        pass
    def getKey(self):
        return self.key
    pass

if(__name__ == "__main__"):
    message= "101010101010101001101110110111"
    streamCipher=StreamCipher()
    streamCipher.generateKey(len(message))
    print("Message: \n",message)
    print("Key: \n",streamCipher.getKey())
    print("\nMessage encrypted :")
    y=streamCipher.encrypt(message)
    print(y)
    print("\nMessage decrypted :")
    print(streamCipher.decrypt(y))