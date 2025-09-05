"""A generator expression in Python provides a concise way to create a generator object.
It is syntactically similar to a list comprehension but uses parentheses () instead of square brackets [].
Key characteristics of generator expressions:
Lazy Evaluation:
Unlike list comprehensions which construct the entire list in memory, generator expressions generate values one at a time, on demand.
This "lazy" evaluation makes them highly memory-efficient, especially when dealing with large datasets.
Iterator Protocol:
A generator expression returns an iterator. This means you can iterate over it once, and after all values have been yielded, it becomes "exhausted."
Conciseness:
They offer a compact syntax for creating generators, often used when a generator is needed for a single iteration or passed directly as an argument to a function."""


"""
| Feature     | List Comprehension                                    | Generator Expression                     |
| ----------- | ----------------------------------------------------- | ---------------------------------------- |
| Syntax      | `[expr for item in iterable]`                         | `(expr for item in iterable)`            |
| Output      | Returns a **list**                                    | Returns a **generator object**           |
| Memory      | **O(n)** (stores all items in memory)                 | **O(1)** (generates items one at a time) |
| Reusability | Can be reused, supports indexing/slicing              | One-time use, no indexing                |
| Use case    | When you need results multiple times or random access | When you only need to iterate once       |

✅ Summary / Rule of Thumb
Use list comprehension if:
    You need to store results
    You want indexing / slicing
    You’ll reuse the values multiple times
Use generator expression if:
    You’re streaming values into another function (all, any, sum, max etc.)
    You only need one pass through the data
    You want to save memory
"""


# all() inbuild function, returns true if all the values in iteratable are true, it opposite to any() which writtens true if any one value from iteratable is true
print(all([True, True, True]))     # True
print(all([True, False, True]))    # False
print(all({True}))                 # True
print(all([]))                     # True  (empty sequence is considered True)

nums = [2, 4, 6, 8]
# List comprehension (extra memory)
print([x % 2 == 0 for x in nums]) # Output: [True, True, True, True]
print(all([x % 2 == 0 for x in nums]))   # O(n) space

# Generator expression (memory efficient)
print(x % 2 == 0 for x in nums) #Output: <generator object <genexpr> at 0x00000217EAC758A0>
print(all(x % 2 == 0 for x in nums))     # O(1) space


# List comprehension (eager evaluation)
squares_list = [x**2 for x in range(5)]
print(squares_list) # Output: [0, 1, 4, 9, 16]

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(5))
print(squares_gen) # Output: <generator object <genexpr> at 0x...>
print(all(squares_gen)) # Output: True

# Iterating over the generator expression
for square in squares_gen:
    print(square)

# List comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)          # [0, 2, 4, 6, 8]
print(evens[2])       # 4  ✅ can index
print(evens[::-1])    # [8, 6, 4, 2, 0]

# Generator expression
evens_gen = (x for x in range(10) if x % 2 == 0)
print(list(evens_gen))  # [0, 2, 4, 6, 8]
print(list(evens_gen))  # [] ❌ consumed


