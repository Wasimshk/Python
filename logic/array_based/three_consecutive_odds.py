arr1 = [3, 5, 4, 1]
arr2 = [5, 7, 34, 1, 4, 9, 7, 25, 12]

def three_consecutive_odds(arr1):
    """
    This function checks if there are three consecutive odd numbers in the given array.
    :param arr1: List of integers
    :return: True if there are three consecutive odd numbers, False otherwise
    """
    # counter = 0
    # for i in arr1:
    #     if i % 2 ==1:
    #         counter += 1
    #         if counter == 3:
    #             return True
    #     else: 
    #         counter = 0
    # return False

    for i in arr1:
        if i % 2 == 1:
            if arr1.index(i) + 2 < len(arr1) and arr1[arr1.index(i) + 1] % 2 == 1 and arr1[arr1.index(i) + 2] % 2 == 1:
                return True

print(three_consecutive_odds(arr1))  # Output: True
print(three_consecutive_odds(arr2))  # Output: False