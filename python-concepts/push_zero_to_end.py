

arr = [0, 1, 10, 13, 2, 3, 0, 4, 0, 5]


# arr.remove(2) # removes first occurrence of 2
# arr.pop(2) # removes element at index 2

# arr.append(20) # adds 20 at the end of the list
# arr.insert(2, 15) # adds 15 at index 2

for i in range(len(arr)):
    if arr[i] == 0:
        arr.remove(0)  
        arr.append(0)
print(arr)