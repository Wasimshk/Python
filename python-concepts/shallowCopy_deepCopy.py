# l1 = l2 → both variables point to the same list object in memory (aliasing).

# l1 = l2.copy() → l1 gets a shallow copy of l2, so they are different objects, but nested objects inside are still shared.

"""
Assignment (l1 = l2)
No new list is created.
Both l1 and l2 reference the same underlying list.
Changes to one affect the other."""

l2 = [1, 2, 3]
l1 = l2
l1.append(4)
print(l2)  # [1, 2, 3, 4]


"""
Shallow copy (l1 = l2.copy() or l1 = list(l2) or l1 = l2[:])
Creates a new list object with the same elements.
The outer list is independent, but if elements are mutable (like nested lists), both lists still share references to those inner objects."""

l2 = [[1, 2], [3, 4]]
l1 = l2.copy()
l1[0].append(99)
print(l2)  # [[1, 2, 99], [3, 4]] → inner list still shared

# To avoid that, use deep copy:
import copy
l1 = copy.deepcopy(l2)
# Now l1 and l2 are fully independent, including nested objects.

"""Rule of thumb:

= just makes a new label.

.copy() makes a new container but keeps references inside.

deepcopy() makes a totally independent structure."""