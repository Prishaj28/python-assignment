#1. Convert Words in a List to Uppercase and Store in a Set

words = ['apple', 'banana', 'cherry', 'date']
upper_set = {word.upper() for word in words}
print("Uppercase Set:", upper_set)


#2. Create a Set of Random Numbers, Count < 30, Delete > 35

import random

random_set = {random.randint(15, 45) for _ in range(10)}
print("Original Set:", random_set)

# Count numbers less than 30
count_lt_30 = len([x for x in random_set if x < 30])
print("Count of numbers < 30:", count_lt_30)

# Delete numbers greater than 35
filtered_set = {x for x in random_set if x <= 35}
print("Filtered Set (<= 35):", filtered_set)


#3. Create, Add, Modify and Delete Names from a Set
names = set()

# Add five names
names.update(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
print("After Adding:", names)

# Modify one name: simulate by removing and adding a new one
names.discard('Charlie')
names.add('Clara')
print("After Modifying:", names)

# Delete two names
names.discard('David')
names.discard('Eve')
print("After Deletion:", names)


#4. Separate Names into Two Sets (Start with A or B)

name_set = {'Alice', 'Andrew', 'Ben', 'Brenda', 'Alex', 'Brian'}

set_A = {name for name in name_set if name.startswith('A')}
set_B = {name for name in name_set if name.startswith('B')}

print("Names starting with A:", set_A)
print("Names starting with B:", set_B)
