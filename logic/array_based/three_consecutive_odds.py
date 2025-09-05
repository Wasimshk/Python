arr1 = [3, 5, 3, 1]
arr2 = [5, 7, 34, 1, 4, 9, 7, 25, 12]

def three_consecutive_odds(arr):
    # for i in range(len(arr)-2):
    #     if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
    #         return True
    # return False

    # counter = 0
    # for num in arr:
    #     if num % 2 == 1:
    #         counter += 1
    #         if counter == 3:
    #             return True
    #     else:
    #         counter = 0
    # return False

    for i in range(len(arr) - 2):
        window = arr[i:i+3]
        if all(x % 2 == 1 for x in window):
            return f"found 3 consecutive odd numbers at position {i+1}:{i+3}"
    return False

print(three_consecutive_odds(arr1))
print(three_consecutive_odds(arr2))