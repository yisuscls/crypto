# Tablas de permutación inicial y final (IP y FP)
class DES():
    IP =[58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]

    FP =[40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]

    # Tablas para la generación de subclaves
    PC1 = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

    PC2 = [14, 17, 11, 24, 1, 5,
                3, 28, 15, 6, 21, 10,
                23, 19, 12, 4, 26, 8,
                16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32]

    E = [32, 1, 2, 3, 4, 5, 4, 5,
            6, 7, 8, 9, 8, 9, 10, 11,
            12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21,
            22, 23, 24, 25, 24, 25, 26, 27,
            28, 29, 28, 29, 30, 31, 32, 1]

    P = [16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25]


    S_BOX = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    def __init__(self,key) -> None:
        self.key = key
        pass
    # Función para la permutación según una tabla
    def permute(self,block, table):
        return ''.join(block[i - 1] for i in table)

    # Función para rotar a la izquierda cada mitad de la clave
    def rotate_left(self,key, shifts):
        return key[shifts:] + key[:shifts]



    def xor(self,bits1, bits2):
        return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bits1, bits2))

    def s_box_transform(self,block):
        
        output = ''
        for i in range(8):  # 8 S-boxes
            six_bits = block[i*6:(i+1)*6]
            row = int("0b"+six_bits[0] + six_bits[5], 2)  # El primer y último bit determinan la fila
            col = int("0b"+six_bits[1:5], 2)
            s_value= bin(self.S_BOX[i][row][col])[2:]
            for i in range(4-len(s_value)):
                s_value="0"+s_value
            output += s_value# Acceso usando fila y columna
        return output

    def des_round(self,block, subkey):
        expanded_block = self.permute(block, self.E)
        xored_block = self.xor(expanded_block, subkey)
        substituted_block = self.s_box_transform(xored_block)
        final_permuted = self.permute(substituted_block, self.P)
        return final_permuted

    def des_encrypt(self,block):
        subkeys = self.generate_subkeys(self.key)
        block = self.permute(block, self.IP)
        left, right = block[:32], block[32:]
        i=0
        for subkey in subkeys:
            sbox_str = self.des_round(right, subkey)
            left= self.xor(left, sbox_str)
            if(i != 15):
                left, right = right, left
            i+=1
        combined = left + right
        encrypted = self.permute(combined, self.FP)
        return encrypted

    def des_decrypt(self,block):
        
        subkeys = self.generate_subkeys(self.key)  # Reuse subkey generation logic
        subkeys[::-1] # Reverse the order of the subkeys for decryption

        block = self.permute(block, self.IP)
        left, right = block[:32], block[32:]

        i=0
        for subkey in subkeys:
            sbox_str = self.des_round(right, subkey)
            left= self.xor(left, sbox_str)
            if(i != 15):
                left, right = right, left
            i+=1

        combined = left + right
        encrypted = self.permute(combined, self.FP)
        return encrypted

    def generate_subkeys(self,master_key):
        key = self.permute(master_key, self.PC1)
        left, right = key[:28], key[28:]
        shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        subkeys = []
        
        for shift in shifts:
            left = self.rotate_left(left, shift)
            right = self.rotate_left(right, shift)
            combined_key = left + right
            subkey = self.permute(combined_key, self.PC2)
            subkeys.append(subkey)
        
        return subkeys

    # Other supporting functions remain unchanged

if __name__ == "__main__":
    key = '1' * 64  # 64-bit key, note this should ideally be a valid DES key
    text = '0011111111111111111111111111111111111111111111111111111111111110' 
    des=DES(key)# 64-bit text
    encrypted_text =des.des_encrypt(text)
    decrypted_text = des.des_decrypt(encrypted_text)

    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
    print("Original  Text:", text)
