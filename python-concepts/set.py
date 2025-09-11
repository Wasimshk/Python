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

    # def mergeList(l1, l2):
    #     return sorted(set(l1+l2))
    list1 = [0, 1, 3, 5, 7, 9, 10, 0, 0, 12, 1]
    list2 = [2, 4, 6, 8, 10, 12, 0]


    #
    # print(mergeList(list1, list2))

    def mergelists(l1, l2):
        return sorted(set(l1 + l2))


    # print(mergelists(list1, list2))

    set1 = set(list1)
    set2 = {2, 4, 6, 8, 10, 12, 0, 15}

    # Union of set1 and set2 → all items from both sets
    print("Union: ", set1 | set2)
    # Intersection → items present in both sets
    print("Intersection: ",set1 & set2)
    # Difference → items in set1 but not in set2
    print("Difference: ", set1 - set2)
    # Symmetric difference → items in either set1 or set2, but not in both
    print("Symmetric difference: ", set1 ^ set2)

    # set comprehension
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}
    common = {n for n in set1 if n in set2}
    print(common)


    # important note
    set1 = {1, 2, 3}
    set3 = set1 # Here, set3 does NOT create a new set., Both set3 and set1 point to the same object in memory.

    set3.add(4)
    print(set1)  # {1, 2, 3, 4}
    print(set3)  # {1, 2, 3, 4}

    set1 = {1, 2, 3}
    set3 = set1.copy() #.copy() creates a new set with the same elements.

    set3.add(4)
    print(set1)  # {1, 2, 3}
    print(set3)  # {1, 2, 3, 4}
