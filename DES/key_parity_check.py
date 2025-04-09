# 密钥奇偶校验位的生成和去除
# 输入：key: int
# 输出: int
def parity_generator(key):
    # string
    b_key = format(key, '056b')
    result = ''
    for i in range(0, len(b_key) // 7):
        block_key = b_key[i * 7: (i + 1) * 7 ]
        if block_key.count('1') % 2 == 0:
            result += block_key + '1'
        else:
            result += block_key + '0'
    return int(result, 2)

def parity_remove(key):
    b_key = format(key, '064b')
    result = ''
    for i in range(0, len(b_key) // 8):
        result += b_key[i * 8: i * 8 + 7]
    # print(format(int(result, 2), '014x'))
    return int(result, 2)


def main():
    key = int('0123456789abcd', 16)
    key = parity_generator(key)
    print(f"{key:x}")
    result = parity_remove(key)
    print(hex(result))

main()