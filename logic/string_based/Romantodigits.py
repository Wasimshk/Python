# convert roman numbers to digit

from functools import reduce
roman = {"i":1,"iv":4,"v":5,"x":10}

numarr = []
def convertRoman(num):

    for char in num:
        if char in roman:
          numarr.append(roman[char])
    return reduce(lambda a, b: a+b, numarr)

num = ("iii")

print(convertRoman(num))



