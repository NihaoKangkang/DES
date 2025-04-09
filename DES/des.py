from os.path import isfile


PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
left_shift_box = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


# 只有两种长度的密钥，64bit = 16byte; 56bit = 14byte
def format_key(key, lengthOfKey):
    if lengthOfKey == 14:
        return key
    else:
        b_key = format(key, '064b')
        key = ''
        for i in range(0, len(b_key) // 8):
            key += b_key[i * 8: i * 8 + 7]
        return int(key, 2)


# input: data: binary string; table: list
# output: permute_result: string
def permuted_choice(data, table):
    # 注意：table 中的数字从 1 开始计数，而 Python 索引从 0 开始
    permute_result = ''
    for i in range(0, len(data) // len(table)):
        permute_result += ''.join([data[(i * len(table)) + j - 1] for j in table])
    return permute_result


# input: key: int
# output: rk: int list
def rk_generator(key):
    key_b = permuted_choice(f"{key, "048b"}", PC_1)
    C, D = [key_b[:28]], [key_b[28:]]
    rk = []
    for i in range(0, 16):
        left_sh = left_shift_box[i]
        C.append(C[i][left_sh:] + C[i][:left_sh])
        D.append(D[i][left_sh:] + D[i][:left_sh])
        temp_key = permuted_choice(C[i+1] + D[i+1], PC_2)
        rk.append(int(temp_key, 2))
    return rk


def padding_zero(data):
    if len(data) % 8 != 0:
        data += b'\x00' * (8 - len(data) % 8)
    return data


def remove_padding_zeros(data):
    length = len(data)
    while length > 0 and data[length - 1] == 0x00:
        length -= 1
    return data[:length]


def des_str_encode(data, key):
    rk = rk_generator(key)
    messages = padding_zero(data.encode())
    
    pass


def des_str_decode(data, key):
    pass


def des_file_encode(data, key):
    pass


def des_file_decode(data, key):
    pass


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