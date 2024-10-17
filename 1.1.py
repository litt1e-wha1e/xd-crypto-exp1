NUM_CIPHER = len(ciphertexts)
THRESHOLD_VALUE = 7  # 认为该位置是空格的阈值


def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def letter_position(s):
    position = []
    for idx in range(len(s)):
        if ('A' <= s[idx] <= 'Z') or ('a' <= s[idx] <= 'z') or s[idx] == chr(0):
            position.append(idx)
    return position


def find_space(cipher):
    space_position = {}
    space_possible = {}
    # 两两异或
    for cipher_idx_1 in range(NUM_CIPHER):
        space_xor = []
        c = ''.join(
            [chr(int(d, 16)) for d in [cipher[cipher_idx_1][i:i + 2] for i in range(0, len(cipher[cipher_idx_1]), 2)]])
        for cipher_idx_2 in range(NUM_CIPHER):
            # 16进制字符串转ascii码
            e = ''.join([chr(int(d, 16)) for d in
                         [cipher[cipher_idx_2][i:i + 2] for i in range(0, len(cipher[cipher_idx_2]), 2)]])
            plain_xor = strxor(c, e)
            if cipher_idx_2 != cipher_idx_1:
                # 记录可能的空格位置
                space_xor.append(letter_position(plain_xor))
        space_possible[cipher_idx_1] = space_xor

    for cipher_idx_1 in range(NUM_CIPHER):
        spa = []
        for position in range(400):
            count = 0
            for cipher_idx_2 in range(NUM_CIPHER - 1):
                if position in space_possible[cipher_idx_1][cipher_idx_2]:
                    count += 1
            if count > THRESHOLD_VALUE:
                spa.append(position)
        space_position[cipher_idx_1] = spa
    return space_position


# 破解出密钥key
def calculate_key(cipher):
    key = [0] * 200
    space = find_space(cipher)
    for cipher_idx_1 in range(NUM_CIPHER):
        for position in range(len(space[cipher_idx_1])):
            idx = space[cipher_idx_1][position] * 2
            a = cipher[cipher_idx_1][idx] + cipher[cipher_idx_1][idx + 1]
            key[space[cipher_idx_1][position]] = int(a, 16) ^ ord(' ')
    key_str = ""
    for k in key:
        key_str += chr(k)
    return key_str


result = ""
key = calculate_key(ciphertexts)
key_hex = ''.join([hex(ord(c)).replace('0x', '') for c in key])
f = ''.join([chr(int(d, 16)) for d in [ciphertexts[10][i:i + 2] for i in range(0, len(ciphertexts[10]), 2)]])
for letter in strxor(f, key):
    if ' ' <= letter <= '~ ':
        result += letter
print(result)