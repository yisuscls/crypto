
import galois
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


    def __init__(self, key):
        self.key = key
        match len(key):
            case 128:
                self.nr=10
            case _:
                raise Exception("invalid key length. The length must be 128/192/256.")
    def encrypt(self,text):
        if(len(text)!=128):
            raise Exception("invalid input length. The length must be 128")
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
        # Convert the binary string input into hex for processing
        keys = self.generate_keys(self.key)
        text_hex = self.bi_hex(self.split_data(text, 8))
    
        # Start decryption by applying the last round key
        A = self.xor(text_hex, keys[self.nr])
        
        # Perform the last round without the MixColumns
        A = self.byte_substitution_inv(A)
        
        A = self.shift_rows_inv(A)
        # Iterate over the remaining rounds in reverse order
        for i in range(self.nr - 1, 0, -1):
            A = self.xor(A, keys[i])
            A = self.mix_columns_inv(A)
            A = self.byte_substitution_inv(A)
            A = self.shift_rows_inv(A)

        # Final round key application
        A = self.xor(A, keys[0])

        # Convert hex back to binary to return the result
        result = self.hex_bi(A)
        final_result = "".join(result)
        return final_result

    def byte_substitution_inv(self, A):
        # Implement inverse S-box substitution
        B = []
        for ai in A:
            row, column = self.get_row_columns(ai)
            # Find the value in the inverse S-box; you would need to define the inverse S-box
            B.append(self.INV_SBOX[row][column])
        return B

    def shift_rows_inv(self, B):
        # Inverse of the shift_rows method
        return [
            B[0], B[13], B[10], B[7],
            B[4], B[1], B[14], B[11],
            B[8], B[5], B[2], B[15],
            B[12], B[9], B[6], B[3]
        ]

    def mix_columns_inv(self, B):
        # Implement the inverse of mix_column using your C_inv method
        B = self.split_data(B, 4)
        result = []
        for Bi in B:
            result.extend(self.C_inv(Bi))
        return result

    def C_inv(self, Bi):
        GF = galois.GF(2**8)
        matriz = [
            ['0E', '0B', '0D', '09'],
            ['09', '0E', '0B', '0D'],
            ['0D', '09', '0E', '0B'],
            ['0B', '0D', '09', '0E']
        ]
        Ci = []
        p = galois.Poly([1, 1, 0, 1, 1, 0, 0, 0, 1], field=GF)
        for i in range(4):
            sum = GF(0)
            for j in range(4):
                a = galois.Poly(self.pol(matriz[i][j]), field=GF) 
                b = galois.Poly(self.pol(Bi[j]), field=GF)
                sum += (a * b) % p
            c = []
            for x in list(sum.coefficients):
                c.append(int(x))
            binary_string = ''.join(str(bit) for bit in c)
            hex_string = format(int(binary_string, 2), 'x')
            Ci.append(hex_string.upper())
        return Ci

    
    def byte_substitution(self,A):
        B=[]
        for ai in A:
            row,column=self.get_row_columns(ai)
            B.append(self.SBOX[row][column])
        return B
    def shift_rows(self,B):
        return [
        B[0], B[5], B[10], B[15],
        B[4], B[9], B[14], B[3],
        B[8], B[13], B[2], B[7],
        B[12], B[1], B[6], B[11]
    ]
    
    def mix_columns_inv(self,B):
        B=self.split_data(B,4)
        result=[]
        for Bi in B:
            for c in self.C_inv(Bi):
                result.append(c)
            
        return result
    def mix_column(self,B):
        B=self.split_data(B,4)
        result=[]
        for Bi in B:
            for c in self.C(Bi):
                result.append(c)
            
        return result
    def C_inv(self,Bi):
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
        # Convert hex to binary string, then to a list of integers (0 and 1)
        bin_list = [int(b) for b in bin(int(hex_number, 16))[2:]]
        return bin_list
    
    def generate_keys(self, key):
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
        
        V32= self.rotate_left(V32,1)
        Vi=self.byte_substitution(V32)
        Vi[0]=self.xor_hexadecimal(Vi[0],self.RC[round-1])
        
        return Vi


    def get_row_columns(self,Ai):
        row, column=Ai[0],Ai[1]
        row,column=int("0x"+row,16),int("0x"+column,16)
        return row,column
        
    def split_data(self,data,n):
        return [data[i:i + n] for i in range(0, len(data), n)]
    def bi_hex(self,data):
        result = []
        for value in data:
            n_int = int('0b'+value, 2)
            n_hex = hex(n_int)[2:]
            result.append(n_hex)
        return result
    def hex_bi(self,data):
        result = []
        for value in data:
            # Convertir cada valor hexadecimal a un entero
            n_int = int(value, 16)
            # Convertir el entero a una cadena binaria, quitando el prefijo '0b' y asegurándose de que tenga 8 bits
            n_bin = bin(n_int)[2:].zfill(8)
            result.append(n_bin)
        return result
    def rotate_left(self,key, shifts):
        return key[shifts:] + key[:shifts]
    def xor_hexadecimal(self,hex1, hex2):
        # Convertir los números hexadecimales a enteros
        num1 = int(hex1, 16)
        num2 = int(hex2, 16)
        
        # Realizar la operación XOR
        resultado_xor = num1 ^ num2
        
        # Convertir el resultado de vuelta a hexadecimal y asegurarse de que tenga dos dígitos
        resultado_hex = format(resultado_xor, '02x')
        return resultado_hex
    def xor(self,a,b):
        result=[]
        for i in range(len(a)):
            result.append(self.xor_hexadecimal(a[i],b[i]))
        return result
    pass

if __name__ == '__main__':
    key= '01111111111111111111111111111110111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    text='10111101111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    aes = AES(key)
    
    encrypted_text=aes.encrypt(text)
    decrypted_text=aes.decrypt(encrypted_text)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
    print("Original  Text:", text)

    
    pass