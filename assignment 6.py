#1. Count Boys (Tuples) and Girls (Strings) in a List

people = [('John', 'Alex'), 'Samantha', ('Chris', 'Mark'), 'Emily', 'Nina']

boys = [p for p in people if isinstance(p, tuple)]
girls = [p for p in people if not isinstance(p, tuple)]

print("Number of Boys:", len(boys))
print("Number of Girls:", len(girls))


#2. Split Tuples into Separate Lists

students = [(101, 'Alice', 18), (102, 'Bob', 19), (103, 'Charlie', 20)]

roll_nos = [s[0] for s in students]
names = [s[1] for s in students]
ages = [s[2] for s in students]

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)


#3. Find Days Between Two Dates (Tuples)

from datetime import date

date1 = (10, 4, 2023)  # (day, month, year)
date2 = (23, 4, 2025)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

diff = abs((d2 - d1).days)
print("Number of days between dates:", diff)


#4. Sort List of Food Items by Price (Descending)

foods = [('Pizza', 250), ('Burger', 150), ('Pasta', 200), ('Salad', 100)]

sorted_foods = sorted(foods, key=lambda x: x[1], reverse=True)
print("Sorted Food List by Price (Descending):", sorted_foods)


#5. Remove Empty Tuples from a List

tuple_list = [(), ('a', 1), (), ('b', 2), ()]

filtered_list = [t for t in tuple_list if t]
print("List After Removing Empty Tuples:", filtered_list)


#6. Modify an Element of a Tuple
#Tuples are immutable, so we recreate a new one:


t = (1, 2, 3, 4)
# Change 3rd element (index 2) to 30
t = t[:2] + (30,) + t[3:]
print("Modified Tuple:", t)


#7. Delete an Element from a Tuple
#You cant delete from a tuple directly; instead, convert to list then back to tuple:


t = (10, 20, 30, 40)
temp_list = list(t)
del temp_list[1]  # Delete second element
t = tuple(temp_list)
print("Tuple After Deletion:", t)
