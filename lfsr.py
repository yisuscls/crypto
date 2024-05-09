import random 

class LFSR():
    def __init__(self, pol, si=None):
        """
        Constructor para inicializar un registro de desplazamiento con retroalimentación lineal (LFSR).
        Parámetros:
        - pol (tuple of int): Tupla que define los índices de los bits que afectan el desplazamiento.
        - si (list of int, opcional): Estado inicial del LFSR. Si no se proporciona, se genera uno aleatorio.
        """
        self.pol = pol
        if si is None:
            self.generate_initial_state()
        else:
            self.si = si
        if(len(self.si)!=max(self.pol)+1):
            raise Exception("La cantidad de estados no concuerdan con el grado del polinomio ")

    def generate_initial_state(self):
        """
        Genera un estado inicial aleatorio para el LFSR basado en la longitud máxima definida por el polinomio.
        """
        length = max(self.pol) + 1
        self.si = [random.randint(0, 1) for _ in range(length)]

    def generateSm(self):
        """
        Genera el siguiente bit en la secuencia del LFSR aplicando la retroalimentación especificada por el polinomio.
        
        Devuelve:
        - si_m (int): El siguiente bit generado.
        """
        si_m = sum(self.si[coef] for coef in self.pol) % 2  # Calcula el siguiente bit según el polinomio
        self.si = self.si[1:] + [si_m]  # Actualiza el estado interno del LFSR
        return si_m

    def sequence(self, length_key):
        """
        Genera una secuencia de bits de la longitud especificada utilizando el LFSR.
        Parámetros:
        - length_key (int): Longitud de la secuencia de bits a generar.
        
        Devuelve:
        - sequence (list of int): Secuencia de bits generada.
        """
        sequence = []
        for _ in range(length_key):
            sequence.append(self.generateSm())
        return sequence

if __name__ == "__main__":
    # Definición del polinomio y el estado inicial.
    poly = (0, 1, 2, 8)
    si = [0, 0, 0, 1,0, 0, 0, 1,1]
    lfsr = LFSR(poly)
    len_key = 100
    
    # Mostrar la longitud de la clave y la clave generada.
    print("Key length:", len_key)
    print("key:\n", lfsr.sequence(len_key))
