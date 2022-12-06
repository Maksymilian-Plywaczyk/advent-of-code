
import random
with open("input.txt") as file:
    file_content = file.read()

# task1
x = min([x for x in range(0, len(file_content))
        if len(set(file_content[x-4:x])) == 4])
print(x)

# task2
x = min([x for x in range(0, len(file_content))
        if len(set(file_content[x-14:x])) == 14])
print(x)
