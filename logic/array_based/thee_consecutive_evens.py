
def is_consecutive_evens(arr, method, k=2):

    match method:
        case 1:
            # direct indexing slightly difficult in scalable, to call this do not specity k value in function call
            for i in range(len(arr)-2):
                if arr[i] % 2 == 0 and arr[i+1] % 2 == 0 and arr[i+2] % 2 == 0:
                        return f"Method1: found {k} consecutive even numbers at position {i+1}:{i+3}"
            return f"Method1: {False}"

        case 2:
            # using generator expression, scalable
            for i in range(len(arr)-(k-1)):
                window = arr[i:i+k]
                if all(num%2==0 for num in window):
                    return f"Method2: found {k} consecutive even numbers at position {i+1}:{i+k}"
            return f"Method1: {False}"

        case 3:
            # simple and clean
            counter = 0
            for num in arr:
                if num % 2 == 0:
                    counter += 1
                    if counter == k:
                        return f"Method3: found {k} consecutive even numbers"
                else:
                    counter = 0
            return f"Method3: {False}"

arr1 = [3, 6, 4, 1, 2, 4, 6, 8]
arr2 = [5, 7, 34, 2, 5, 9, 7, 24, 12, 14, 17]

print(is_consecutive_evens(arr1, 2, 4))
print(is_consecutive_evens(arr1, 3, 4))
print(is_consecutive_evens(arr2, 2, 3))
print(is_consecutive_evens(arr2, 1))
