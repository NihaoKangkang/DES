from DES import *

if __name__ == "__main__":

    inputData = input('Input text,hex data or file location need to calculate des(press ENTER to abort): ')
    inputKey = input('Input 64 bits(including parity) or 56 bits(without parity) secret key in hex (like \'0123456789abcd\', input nothing to abort): ')
    # 因为示例为16进制字符串，所以这边进行了byte流输出，实际输入应当为string
    # inputData = b"\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10"
    # inputData = "681edf34d206965e86b3e94f536e4246"
    # Same Key
    # inputData = './LICENSE'
    # inputData = 'nihao woshi wang'
    # inputKey = "0123456789abcdeffedcba9876543210"

    # try:
    #     if inputData and len(inputKey) == 32:
    #         encodeFlag = input("Do you want to encode(y)/decode(n) this data?(Y/n): ")
    #         if encodeFlag == 'y' or encodeFlag == 'Y' or encodeFlag == '':
    #             result = des_encode(inputData, int(inputKey, 16), len(inputKey))
    #             print('DES encode result: ', result.hex() if isinstance(result, bytes) else result)
    #         else:
    #             print('DES decode result: ', des_decode(inputData, int(inputKey, 16), len(inputKey)))
    #     else:
    #         print("Check input data.")
    # except ValueError:
    #     print("Check input data.")


    if inputData and (len(inputKey) == 14 or len(inputKey) == 16):
        encodeFlag = input("Do you want to encode(y)/decode(n) this data?(Y/n): ")
        if encodeFlag == 'y' or encodeFlag == 'Y' or encodeFlag == '':
            result = des_encode(inputData, int(inputKey, 16), len(inputKey))
            print('DES encode result: ', result.hex() if isinstance(result, bytes) else result)
        else:
            print('DES decode result: ', des_decode(inputData, int(inputKey, 16), len(inputKey)))
    else:
        print("Check input data.")
