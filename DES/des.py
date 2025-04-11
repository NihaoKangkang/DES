from os.path import isfile


PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
left_shift_box = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
S_box = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
         [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
         [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
         [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
         [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
         [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
         [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
         [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

# 只有两种长度的密钥，64bit = 16byte; 56bit = 14byte
def format_key(key, lengthOfKey):
    if lengthOfKey == 16:
        return key
    else:
        b_key = format(key, '056b')
        result = ''
        for i in range(0, len(b_key) // 7):
            block_key = b_key[i * 7: (i + 1) * 7]
            if block_key.count('1') % 2 == 0:
                result += block_key + '1'
            else:
                result += block_key + '0'
        return int(result, 2)


# input: data: binary string; table: list
# output: permute_result: binary string
def permuted_choice(data, table):
    # 注意：table 中的数字从 1 开始计数，而 Python 索引从 0 开始
    permute_result = ''
    permute_result += ''.join([data[j - 1] for j in table])
    return permute_result


# input: key: int
# output: rk: int list
def rk_generator(key):
    key_b = permuted_choice(f"{key:064b}", PC_1)
    C, D = [key_b[:28]], [key_b[28:]]
    rk = []
    for i in range(0, 16):
        left_sh = left_shift_box[i]
        C.append(C[i][left_sh:] + C[i][:left_sh])
        D.append(D[i][left_sh:] + D[i][:left_sh])
        temp_key = permuted_choice(C[i+1] + D[i+1], PC_2)
        rk.append(int(temp_key, 2))
    return rk

# input: R: binary string key: int
# output: binary string
def F(R, key):
    expansion = permuted_choice(R, E)
    xor_rk = format(int(expansion, 2) ^ key, '048b')
    # S_box replace
    result = ''
    for i in range(0, 8):
        # 每六个二进制为一组，b0,b1,b2,b3,b4,b5 其中b0b5作为row number, b1b2b3b4作为column number
        row_number = int(xor_rk[i * 6] + xor_rk[(i+1) * 6 - 1], 2)
        column_number = int(xor_rk[i * 6 + 1] + xor_rk[i * 6 + 2] + xor_rk[i * 6 + 3] + xor_rk[i * 6 + 4], 2)
        # S盒替换
        result += format(S_box[i][row_number * 16 + column_number], "04b")
    return permuted_choice(result, P)


# input: data : byte
# output: data : byte
def padding_zero(data):
    if len(data) % 8 != 0:
        data += b'\x00' * (8 - len(data) % 8)
    return data


def remove_padding_zeros(data):
    length = len(data)
    while length > 0 and data[length - 1] == 0x00:
        length -= 1
    return data[:length]

def bytes2binary_string(data):
    return ''.join(format(byte, '08b') for byte in data)

def binary_string2bytes(data):
    return bytes(int(data[i:i + 8], 2) for i in range(0, len(data), 8))

# DES 核心实现代码
# input: data : byte  rk: int list
# output: byte
def data_encryption_standard(data, rk):
    blockNumber = len(data) // 8
    result = b''
    for block in range(0, blockNumber):
        blockData = data[block * 8: (block + 1) * 8]
        b_data = permuted_choice(bytes2binary_string(blockData), IP)
        L, R = [b_data[:32]], [b_data[32:]]
        for i in range(0, 16):
            L.append(R[i])
            # print(i, R[i], type(R[i]))
            R.append(format(int(L[i], 2) ^ int(F(format(int(R[i], 2), '032b'), rk[i]), 2), '032b'))
        binary_result = permuted_choice(R[16] + L[16], IP_1)
        result += binary_string2bytes(binary_result)
    return result


def des_str_encode(data, key):
    rk = rk_generator(key)
    b_messages = padding_zero(data.encode())
    return data_encryption_standard(b_messages, rk)


def des_str_decode(data, key):
    rk = rk_generator(key)
    rk.reverse()
    byte_code = bytes.fromhex(data)
    return remove_padding_zeros(data_encryption_standard(byte_code, rk))


def des_file_encode(filename, key):
    rk = rk_generator(key)
    # 文件读写部分
    file_count = 0
    c_fname = filename + '_encoded' + format(file_count, '02d')
    while isfile(c_fname):
        file_count += 1
        c_fname = filename + '_encoded' + format(file_count, '02d')
    # 加密后文件名c_fname
    with open(filename, 'rb') as text_file:
        byte_file = text_file.read()
    byte_file = padding_zero(byte_file)
    encodeMessage = data_encryption_standard(byte_file, rk)
    with open(c_fname, 'wb') as out_file:
        out_file.write(encodeMessage)
    return c_fname

def des_file_decode(filename, key):
    rk = rk_generator(key)
    rk.reverse()
    # 文件读写部分
    file_count = 0
    c_fname = filename + '_decoded' + format(file_count, '02d')
    while isfile(c_fname):
        file_count += 1
        c_fname = filename + '_decoded' + format(file_count, '02d')
    # 加密后文件名c_fname
    with open(filename, 'rb') as text_file:
        byte_file = text_file.read()
    decodeMessage = data_encryption_standard(byte_file, rk)
    with open(c_fname, 'wb') as out_file:
        out_file.write(remove_padding_zeros(decodeMessage))
    return c_fname


# 输入：data：string or file location; key：int; lengthOfKey: int
# 输出: hex string
def des_encode(data, key, lengthOfKey):
    key = format_key(key, lengthOfKey)
    if isfile(data):
        file_location = des_file_encode(data, key)
        return f"File encode success! File location: {file_location}"
    else:
        return des_str_encode(data, key)
        # 测试用
        # return sm4_str_encode(str(data), key)


# 输入: data: hex string; key: int; lengthOfKey: int
# 输出： byte string or file
def des_decode(data, key, lengthOfKey):
    key = format_key(key, lengthOfKey)
    if isfile(data):
        return des_file_decode(data, key)
    else:
        return des_str_decode(data, key)