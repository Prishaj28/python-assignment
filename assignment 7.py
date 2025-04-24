# 1. concatenate 3 dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Concatenating all dictionaries
dict4 = {**dict1, **dict2, **dict3}
print("Concatenated Dictionary:", dict4)


#2. Check if a Dictionary is Empty

my_dict = {}

if not my_dict:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")

    
#3. Department-wise Min and Max Salary

employees = [
    {'dept': 'HR', 'roll_no': 101, 'salary': 50000},
    {'dept': 'IT', 'roll_no': 102, 'salary': 80000},
    {'dept': 'HR', 'roll_no': 103, 'salary': 45000},
    {'dept': 'IT', 'roll_no': 104, 'salary': 95000},
    {'dept': 'Finance', 'roll_no': 105, 'salary': 60000}
]

from collections import defaultdict

dept_salaries = defaultdict(list)

for emp in employees:
    dept_salaries[emp['dept']].append(emp['salary'])

for dept, salaries in dept_salaries.items():
    print(f"{dept} - Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")

    
#4. Frequency of Each Character in a String

input_str = input("Enter a string: ")
char_freq = {}

for char in input_str:
    char_freq[char] = char_freq.get(char, 0) + 1

print("Character Frequency:", char_freq)


#5. Compute Total Grocery Bill

prices = {
    'rice': 50,
    'wheat': 30,
    'sugar': 40
}

quantities = {
    'rice': 2,
    'wheat': 5,
    'sugar': 1
}

total_bill = 0
for item in prices:
    total_bill += prices[item] * quantities.get(item, 0)

print("Total Bill: Rs.", total_bill)
