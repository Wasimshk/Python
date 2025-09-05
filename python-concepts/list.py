# filepath: /python-collections-app/python-collections-app/src/list.py
# arr.remove(2) # removes first occurrence of 2
# arr.pop(2) # removes element at index 2

# arr.append(20) # adds 20 at the end of the list
# arr.insert(2, 15) # adds 15 at index 2


def add_element(my_list, element):
    my_list.append(element)
    return my_list

def remove_element(my_list, element):
    if element in my_list:
        my_list.remove(element)
    return my_list

def display_list(my_list):
    return my_list

# Usage examples
if __name__ == "__main__":
    my_list = [1, 2, 3]
    print("Original List:", display_list(my_list))
    
    my_list = add_element(my_list, 4)
    print("After Adding 4:", display_list(my_list))
    
    my_list = remove_element(my_list, 2)
    print("After Removing 2:", display_list(my_list))