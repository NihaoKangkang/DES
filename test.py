def permute(bits: str, table: list) -> str:
    """按置换表重新排列位，例如 DES 的 IP/E 等步骤"""
    # 注意：table 中的数字从 1 开始计数，而 Python 索引从 0 开始
    permute_result = ''
    for i in range(0, len(bits) // len(table)):
        permute_result += ''.join([bits[(i * len(table)) + j - 1] for j in table])
    return permute_result# 将每个位置 i 转换为 bits[i-1]

# 示例：假设一个 8 位的输入和 4 位的置换表
original_bits = '11001010'  # 输入二进制字符串
perm_table = [4, 1, 3, 2]   # 自定义的置换表（将输出缩短为 4 位）

# 置换过程：取原第4位 → 第1位 → 第3位 → 第2位
result = permute(original_bits, perm_table)
print(result)  # 输出：'0101' （原第4位是 '0'，第1位是 '1'，依此类推）
print( hex(int(result,2)) )
# 01010110


PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

print(len(PC_1))
print(len(PC_2))