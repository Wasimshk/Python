# 1³ + 5³ + 3³ = 1 + 125 + 27 = 153.

from functools import reduce

def is_armstrong(num):
    numstr = str(num)
    l = len(numstr)
    arr = (int(num)**l for num in numstr)

    total = reduce(lambda a,b: a+b, arr)

    return total == num

num_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 54748]
num = 54748
print(is_armstrong(num))