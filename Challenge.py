convert_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def decimalToHex(decimal):
    hexadec = ''
    if decimal == 0:
        hexadec = '00'
        return hexadec
    #If the decimal number less 16, start the number 0 and plus hexnumber
    elif decimal < 16:
        while(decimal > 0):
            remainder = decimal % 16
            hexadec =  hexadec + '0' + convert_table[remainder] 
            decimal = decimal // 16
        return hexadec
    else:
        while(decimal > 0):
            remainder = decimal % 16
            hexadec = hexadec + convert_table[remainder]
            decimal = decimal // 16
        return hexadec

def rgbToHex(red, green , blue):
    first = decimalToHex(red)
    second = decimalToHex(green)
    third = decimalToHex(blue)
    return first + second + third

print(rgbToHex(120, 145, 200))