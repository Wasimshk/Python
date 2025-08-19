

arr1 = [3, 5, 4, 1]
arr2 = [5, 7, 34, 1, 4, 9, 7, 25, 12]

def three_consecutive_odds(arr1):
    """
    This function checks if there are three consecutive odd numbers in the given array.
    :param arr1: List of integers
    :return: True if there are three consecutive odd numbers, False otherwise
    """
    counter = 0
    for i in arr1:
        if i % 2 ==1:
            counter += 1
            if counter == 3:
                return True
        else: 
            counter = 0
    return False

print(three_consecutive_odds(arr1))  # Output: True
print(three_consecutive_odds(arr2))  # Output: False