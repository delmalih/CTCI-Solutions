def getLastBit(number):
    return number & 1

def sumBits(bit1, bit2, ret):
    res = (bit1 ^ bit2) ^ ret
    ret = (bit1 == bit2 == 1) or (bit1 == ret == 1) or (bit2 == ret == 1)
    return (res, ret)

def addWithoutPlus(number1, number2):
    ret = 0
    result = ""
    while number1 != 0 or number2 != 0:
        bit1 = getLastBit(number1)
        bit2 = getLastBit(number2)
        res, ret = sumBits(bit1, bit2, ret)
        result = str(res) + result 
        number1 >>= 1
        number2 >>= 1
    return int(result, 2)

number1 = 517   # bin --> 1000000101
number2 = 6721  # bin --> 1101001000001
# expected : 7238 (bin --> 1110001000110)

print(addWithoutPlus(number1, number2))