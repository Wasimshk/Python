
def rotate_arr(k, arr):
    k = k % len(arr)
    arr = arr[k:] + arr[:k]
    return arr

try:
    k = int(input("Enter rotating position"))
    list_elem = input("Enter list elements")
    arr = list(map(int, list_elem.split()))
except ValueError:
    print("Please enter a number")

print(rotate_arr(k, arr))