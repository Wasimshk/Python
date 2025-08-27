# filepath: /python-collections-app/python-collections-app/src/tuple.py

def create_tuple(*args):
    """Create a tuple from the given arguments."""
    return tuple(args)

def access_element(tup, index):
    """Access an element in the tuple by index."""
    try:
        return tup[index]
    except IndexError:
        return "Index out of range."

def display_tuple(tup):
    """Display the elements of the tuple."""
    return tup

# Usage examples
if __name__ == "__main__":
    # Creating a tuple
    my_tuple = create_tuple(1, 2, 3, 4, 5)
    print("Created Tuple:", display_tuple(my_tuple))

    # Accessing elements
    print("Element at index 2:", access_element(my_tuple, 2))
    print("Element at index 5:", access_element(my_tuple, 5))  # Out of range example