import random 
class LFSR():
    def __init__(self,pol, si=None):
        self.pol = pol
        if si is None:
            self.generate_initial_state()
            self.si=self.si
        else:
            self.si = si
        pass
    def generate_initial_state(self):
        length=max(self.pol)+1
        self.si=[random.randint(0, 1) for _ in range(length)]
        pass
    def generateSm(self):
        si_m=0
        for coef in self.pol:
            si_m+= self.si[coef]
        si_m=si_m%2
        self.si=self.si[1:]+[si_m]
        return si_m
    def sequence(self,length_key):
        sequence=[]
        for _ in range(length_key):
            sequence.append(self.generateSm())
        
        return sequence
    pass

if(__name__ == "__main__"):
    poly= (0,1,2,3)
    si=[0, 0, 0, 1]
    lfsr=LFSR(poly,si)
    len_key=5
    
    print("Key length:",len_key)
    print("key:\n", lfsr.sequence(len_key))
