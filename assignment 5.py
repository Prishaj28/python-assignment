#1. Odd & Even Lists, Replace, Flatten, Sort

import random

# Generate 5 odd integers
odd_list = [random.randrange(1, 50, 2) for _ in range(5)]
print("Original Odd List:", odd_list)

# Generate 4 even integers
even_list = [random.randrange(2, 50, 2) for _ in range(4)]
print("Even List:", even_list)

# Replace 3rd element of odd list with even_list
odd_list[2] = even_list
print("After Replacement:", odd_list)

# Flatten the list
flat_list = []
for item in odd_list:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

# Sort the list
flat_list.sort()
print("Flattened and Sorted List:", flat_list)


#2. Find All Occurrences of User-Input Number

nums = [random.randint(1, 10) for _ in range(20)]
print("Generated List:", nums)

target = int(input("Enter a number to search: "))
positions = [i for i, x in enumerate(nums) if x == target]
print(f"Positions of {target}:", positions)


#3. Remove Duplicates from Random Numbers

rand_list = [random.randint(1, 30) for _ in range(50)]
print("Original List (With Duplicates):", rand_list)

unique_list = list(set(rand_list))
print("List After Removing Duplicates:", unique_list)


#4. Separate +ve and -ve Numbers

mixed_list = [random.randint(-50, 50) for _ in range(30)]
print("Mixed List:", mixed_list)

positives = [x for x in mixed_list if x >= 0]
negatives = [x for x in mixed_list if x < 0]
print("Positive Numbers:", positives)
print("Negative Numbers:", negatives)


#5. Convert Strings to Uppercase

str_list = ['apple', 'banana', 'grape', 'mango', 'peach']
upper_list = [s.upper() for s in str_list]
print("Uppercase Strings:", upper_list)


#6. Convert Fahrenheit to Celsius

fahrenheit_list = [32, 68, 77, 95, 104]
celsius_list = [round((f - 32) * 5/9, 2) for f in fahrenheit_list]
print("Celsius Temperatures:", celsius_list)


#7. Stack Implementation (Menu-Driven)

stack = []

while True:
    print("\nSTACK MENU:\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        val = input("Enter value to push: ")
        stack.append(val)
    elif choice == '2':
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty.")
    elif choice == '3':
        print("Stack:", stack)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")

        
#8. Queue Implementation (Menu-Driven)

from collections import deque

queue = deque()

while True:
    print("\nQUEUE MENU:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        val = input("Enter value to enqueue: ")
        queue.append(val)
    elif choice == '2':
        if queue:
            print("Dequeued:", queue.popleft())
        else:
            print("Queue is empty.")
    elif choice == '3':
        print("Queue:", list(queue))
    elif choice == '4':
        break
    else:
        print("Invalid choice.")

        
#9. List Comprehension: Elements in List1 not in List2

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [x for x in list1 if x not in list2]
print("Elements in List1 not in List2:", list3)
