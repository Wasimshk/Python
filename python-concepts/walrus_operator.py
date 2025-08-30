# Walrus := = assign and use a variable in one expression.

a = 5
b = 10
print(a + b)
print((a:=5) + (b:=10))

for i in (arr:=[0, 5, 10, 15, 20]):
    print(i)



# while (user_input := input("Enter text: ")) != "quit":
#     print(f"You typed: {user_input}")
# # (user_input := input(...)) assigns and checks in the same line.
# # Without walrus, you’d need two lines: one for assignment, one for condition.


from functools import reduce

numbers = [10, 20, 30, 40]

# Use walrus to both assign and print intermediate reduce results
if (total := reduce(lambda x, y: x + y, numbers)) > 50:
    print(f"Sum is {total}, which is greater than 50")