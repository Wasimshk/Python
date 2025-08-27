# filepath: /python-collections-app/python-collections-app/src/set.py

def add_item(s, item):
    """Add an item to the set."""
    s.add(item)

def remove_item(s, item):
    """Remove an item from the set if it exists."""
    s.discard(item)  # discard does not raise an error if the item is not found

def display_set(s):
    """Display the contents of the set."""
    print("Set contents:", s)

# Usage examples
if __name__ == "__main__":
    my_set = set()

    # Adding items
    add_item(my_set, 1)
    add_item(my_set, 2)
    add_item(my_set, 3)
    display_set(my_set)

    # Removing an item
    remove_item(my_set, 2)
    display_set(my_set)

    # Attempting to remove an item that doesn't exist
    remove_item(my_set, 4)  # This will not raise an error
    display_set(my_set)