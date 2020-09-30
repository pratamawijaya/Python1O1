# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

example_tuples = ("apple","banana","cherry")
print(example_tuples)

print(example_tuples[0])
print(example_tuples[-1])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple

y = list(example_tuples)
y[1] = "kiwi"
example_tuples = tuple(y)

print(example_tuples)