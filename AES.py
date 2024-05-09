
import galois
import random
class AES():
    SBOX = [
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
    ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
    ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
    ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
    ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
    ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
    ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
    ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
    ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
    ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
    ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
    ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
    ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
    ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
    ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
    ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']
]
    INV_SBOX = [
    ['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
    ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
    ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
    ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
    ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
    ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
    ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
    ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
    ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
    ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
    ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
    ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
    ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
    ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
    ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
    ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']
]

    RC = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']


    def __init__(self, key=None):
        """
        Inicializa una instancia de AES con una clave específica.
        Entrada:
        - key (str): Clave binaria de 128 bits. Si no se provee, se genera una aleatoriamente.
        """
        self.key = key
        if key==None:
            self.key=self.generate_key(128)
            key = self.key
        match len(key):
            case 128:
                self.nr=10
            case _:
                raise Exception("Tamaño de la llave no valida. La llave debe tener un largo de 128 bits.")
    def encrypt(self,text):
        """
        Cifra un bloque de texto usando el algoritmo AES.
        Entrada:
        - text (str): Bloque de texto de 128 bits.
        Salida:
        - str: Texto cifrado como cadena binaria.
        """
        if(len(text)!=128):
            raise Exception("Tamaño del mensaje no valido. El mensaje debe tener un largo de 128 bits")
        keys=self.generate_keys(self.key)
        
        A= self.split_data(text,8)
        A=self.bi_hex(A)
        A=self.xor(A,keys[0])
        for i in range(self.nr-1):
            B= self.byte_substitution(A)
            B=self.shift_rows(B)
            C=self.mix_column(B)
            A=self.xor(C,keys[i+1])
        B= self.byte_substitution(A)
        B=self.shift_rows(B)
        A=self.xor(B,keys[10])
        A=self.hex_bi(A)
        result=""
        for i in A:
            result+=i
        return result
    def decrypt(self, text):
        """
        Descifra un bloque de texto cifrado usando el algoritmo AES.
        Entrada:
        - text (str): Texto cifrado como cadena binaria.
        Salida:
        - str: Texto descifrado como cadena binaria.
        """
        if(len(text)!=128):
            raise Exception("Tamaño del mensaje no valido. El mensaje debe tener un largo de 128 bits")
        keys = self.generate_keys(self.key)
        text_hex = self.bi_hex(self.split_data(text, 8))
    
        A = self.xor(text_hex, keys[self.nr])
        
        
        A = self.byte_substitution_inv(A)
        
        A = self.shift_rows_inv(A)
        
        for i in range(self.nr - 1, 0, -1):
            A = self.xor(A, keys[i])
            A = self.mix_columns_inv(A)
            A = self.byte_substitution_inv(A)
            A = self.shift_rows_inv(A)

        
        A = self.xor(A, keys[0])

        
        result = self.hex_bi(A)
        final_result = "".join(result)
        return final_result

    def byte_substitution_inv(self, A):
        """
        Aplica la sustitución inversa de bytes usando la INV_SBOX a un bloque de datos.
        Entrada:
        - A (list): Lista de bytes en hexadecimal.
        Salida:
        - list: Lista de bytes tras aplicar la SBOX.
        """
        B = []
        for ai in A:
            row, column = self.get_row_columns(ai)
            B.append(self.INV_SBOX[row][column])
        return B

    def shift_rows_inv(self, B):
        """
        Aplica el desplazamiento inverso de filas a un bloque de datos.
        Entrada:
        - B (list): Lista de bytes en hexadecimal.
        Salida:
        - list: Lista de bytes tras desplazar las filas.
        """
        return [
            B[0], B[13], B[10], B[7],
            B[4], B[1], B[14], B[11],
            B[8], B[5], B[2], B[15],
            B[12], B[9], B[6], B[3]
        ]


    

    
    def byte_substitution(self,A):
        """
        Aplica la sustitución de bytes usando la SBOX a un bloque de datos.
        Entrada:
        - A (list): Lista de bytes en hexadecimal.
        Salida:
        - list: Lista de bytes tras aplicar la SBOX.
        """
        B=[]
        for ai in A:
            row,column=self.get_row_columns(ai)
            B.append(self.SBOX[row][column])
        return B
    def shift_rows(self,B):
        """
        Aplica el desplazamiento de filas a un bloque de datos.
        Entrada:
        - B (list): Lista de bytes en hexadecimal.
        Salida:
        - list: Lista de bytes tras desplazar las filas.
        """
        return [
        B[0], B[5], B[10], B[15],
        B[4], B[9], B[14], B[3],
        B[8], B[13], B[2], B[7],
        B[12], B[1], B[6], B[11]
    ]
    
    def mix_columns_inv(self,B):
        """
        Aplica la inversa operación de mezcla de columnas a un bloque de datos.
        Entrada:
        - B (list): Lista de bytes en hexadecimal.
        Salida:
        - list: Lista de bytes después de mezclar columnas.
        """
        B=self.split_data(B,4)
        result=[]
        for Bi in B:
            for c in self.C_inv(Bi):
                result.append(c)
            
        return result
    def mix_column(self,B):
        """
        Aplica la operación de mezcla de columnas a un bloque de datos.
        Entrada:
        - B (list): Lista de bytes en hexadecimal.
        Salida:
        - list: Lista de bytes después de mezclar columnas.
        """
        B=self.split_data(B,4)
        result=[]
        for Bi in B:
            for c in self.C(Bi):
                result.append(c)
            
        return result
    def C_inv(self,Bi):
        """
        calcula la multiplicación de la matrices del MixcolumnInv layer.
        Entrada:
        - Bi (list): Sublista de 4 bytes representando una columna.
        Salida:
        - list: Lista de bytes resultante de aplicar la mezcla de columnas.
        """
        GF = galois.GF(2)
        matriz = [
        ['E', 'B', 'D', '9'],
        ['9', 'E', 'B', 'D'],
        ['D', '9', 'E', 'b'],
        ['B', 'D', '9', 'E']]
        Ci=[]
        p= galois.Poly([1,0,0,0,1,1,0,1,1])
        for i in range(4):
            sum=GF(0)
            for j in range(4):
                a = galois.Poly(self.pol(matriz[i][j])) 
                b= galois.Poly(self.pol(Bi[j]))
                sum+=(a*b)%p
            c= list()
            for x in list(sum.coefficients()):
                c.append(int(x))
            binary_string = ''.join(str(bit) for bit in c)
            hex_string = format(int(binary_string, 2), '02x')
            Ci.append(hex_string.upper())
        return  Ci
    def C(self,Bi):
        """
        calcula la multiplicación de la matrices del Mixcolumn layer.
        Entrada:
        - Bi (list): Sublista de 4 bytes representando una columna.
        Salida:
        - list: Lista de bytes resultante de aplicar la mezcla de columnas.
        """
        GF = galois.GF(2)
        matriz = [
        ['2', '3', '1', '1'],
        ['1', '2', '3', '1'],
        ['1', '1', '2', '3'],
        ['3', '1', '1', '2']]
        Ci=[]
        p= galois.Poly([1,0,0,0,1,1,0,1,1])
        for i in range(4):
            sum=GF(0)
            for j in range(4):
                a = galois.Poly(self.pol(matriz[i][j])) 
                b= galois.Poly(self.pol(Bi[j]))
                sum+=(a*b)%p
            c= list()
            for x in list(sum.coefficients()):
                c.append(int(x))
            binary_string = ''.join(str(bit) for bit in c)
            hex_string = format(int(binary_string, 2), '02x')
            Ci.append(hex_string.upper())
        return  Ci
    def pol(self,hex_number):
        """
        Convierte un número hexadecimal en una lista de coeficientes binarios que representan un polinomio.
        
        Este método es utilizado en las transformaciones de mezcla de columnas donde se necesitan
        representaciones polinomiales de los bytes para realizar multiplicaciones en el campo de Galois GF(2^8).

        Entrada:
        - hex_number (str): Número en formato hexadecimal que se convertirá a su representación polinomial.
        
        Salida:
        - list: Lista de enteros (0 o 1) que representan los coeficientes del polinomio correspondiente al
                número hexadecimal dado. Los coeficientes se ordenan desde el término de grado más alto al más bajo.
        """
        bin_list = [int(b) for b in bin(int(hex_number, 16))[2:]]
        return bin_list
    
    def generate_keys(self, key):
        """
        Genera todas las subclaves necesarias para el cifrado AES a partir de la clave maestra.
        Entrada:
        - key (str): Clave maestra en formato binario.
        Salida:
        - list: Lista de subclaves en formato hexadecimal.
        """
        keys=[]
        key= self.split_data(key,8)
        key=self.bi_hex(key)
        keys.append(key)
        W=self.split_data(key,4)
        for i in range(10):
            w3_g=self.g_func(W[3],i+1)
            w4=self.xor(W[0],w3_g)
            w5=self.xor(w4,W[1])
            w6=self.xor(w5,W[2])
            w7=self.xor(w6,W[3])
            W=[w4,w5,w6,w7]
            keys.append(w4+w5+w6+w7)
        return keys
    def g_func(self,V32,round):
        """
        Función que modifica el último bloque de subclave de 32 bits según la ronda específica.
        Entrada:
        - V32 (str): Subclave de 32 bits en formato hexadecimal.
        - round (int): Número de ronda actual.
        Salida:
        - str: Subclave de 32 bits modificada.
        """
        V32= self.rotate_left(V32,1)
        Vi=self.byte_substitution(V32)
        Vi[0]=self.xor_hexadecimal(Vi[0],self.RC[round-1])
        
        return Vi


    def get_row_columns(self,Ai):
        """
        Determina la fila y columna para el acceso a las SBOX o INV_SBOX usando un byte en hexadecimal.
        Entrada:
        - Ai (str): Byte en formato hexadecimal.
        Salida:
        - tuple: Tupla de dos elementos (fila, columna) determinados a partir del byte.
        """
        row, column=Ai[0],Ai[1]
        row,column=int("0x"+row,16),int("0x"+column,16)
        return row,column
        
    def split_data(self,data,n):
        """
        Divide una cadena de datos en bloques de tamaño n.
        Entrada:
        - data (str): Cadena de datos en formato binario.
        - n (int): Tamaño del bloque.
        Salida:
        - list: Lista de bloques divididos.
        """
        return [data[i:i + n] for i in range(0, len(data), n)]
    def bi_hex(self,data):
        """
        Convierte una lista de bloques binarios en hexadecimal.
        Entrada:
        - data (list): Lista de bloques binarios.
        Salida:
        - list: Lista de bloques en formato hexadecimal.
        """
        result = []
        for value in data:
            n_int = int('0b'+value, 2)
            n_hex = hex(n_int)[2:]
            result.append(n_hex)
        return result
    def hex_bi(self,data):
        """
        Convierte una lista de bloques hexadecimales en binario.
        Entrada:
        - data (list): Lista de bloques en formato hexadecimal.
        Salida:
        - list: Lista de bloques en formato binario.
        """
        result = []
        for value in data:
            # Convertir cada valor hexadecimal a un entero
            n_int = int(value, 16)
            # Convertir el entero a una cadena binaria, quitando el prefijo '0b' y asegurándose de que tenga 8 bits
            n_bin = bin(n_int)[2:].zfill(8)
            result.append(n_bin)
        return result
    def rotate_left(self,key, shifts):
        """
        Rota los bits de una clave hacia la izquierda.
        Entrada:
        - key (str): Clave en formato binario.
        - shifts (int): Número de desplazamientos hacia la izquierda.
        Salida:
        - str: Clave rotada.
        """
        return key[shifts:] + key[:shifts]
    def xor_hexadecimal(self,hex1, hex2):
        """
        Realiza una operación XOR entre dos números hexadecimales.
        Entrada:
        - hex1 (str), hex2 (str): Números hexadecimales a operar.
        Salida:
        - str: Resultado en formato hexadecimal.
        """
        num1 = int(hex1, 16)
        num2 = int(hex2, 16)
        
        # Realizar la operación XOR
        resultado_xor = num1 ^ num2
        
        # Convertir el resultado de vuelta a hexadecimal y asegurarse de que tenga dos dígitos
        resultado_hex = format(resultado_xor, '02x')
        return resultado_hex
    def xor(self,a,b):
        """
        Realiza una operación XOR entre dos listas de bloques hexadecimales.
        Entrada:
        - a (list), b (list): Listas de bloques hexadecimales.
        Salida:
        - list: Lista de bloques después de la operación XOR.
        """
        result=[]
        for i in range(len(a)):
            result.append(self.xor_hexadecimal(a[i],b[i]))
        return result
    def generate_key(self,length):
        """
        Genera una llave aleatoria de la longitud especificada.
        Entrada:
        - length (int): Longitud de la llave en bits.
        Salida:
        - str: Llave generada aleatoriamente.
        """
        return ''.join(random.choice(['0', '1']) for _ in range(length))
    pass

if __name__ == '__main__':
    text='10111101111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    aes = AES()
    
    encrypted_text=aes.encrypt(text)
    decrypted_text=aes.decrypt(encrypted_text)
    print("llave: \n", aes.key)
    # Cifrado del mensaje y muestra del resultado.
    print("\nMensaje Cifrado :\n",encrypted_text)
    # Descifrado del mensaje cifrado y muestra del resultado.
    print("\nMensaje Descifrado:\n",decrypted_text)
    # mensaje Original
    print("\nMensaje Original: \n", text)

    
    pass