# 1. Add two numbers
a, b = 10, 5
print("Add:", a + b)

# 2. Subtract two numbers
print("Subtract:", a - b)

# 3. Multiply two numbers
print("Multiply:", a * b)

# 4. Divide two numbers
print("Divide:", a / b)

# 5. All operations
print("All Operations - Add:", a + b, "Subtract:", a - b, "Multiply:", a * b, "Divide:", a / b)

# 6. Convert hours into minutes
hours = 2
print("Minutes:", hours * 60)

# 7. Convert minutes into hours
minutes = 120
print("Hours:", minutes / 60)

# 8. Convert dollars into Rs
dollars = 10
print("Rs:", dollars * 48)

# 9. Convert Rs into dollars
rupees = 480
print("Dollars:", rupees / 48)

# 10. Convert dollars into pounds
# 1$ = 48 Rs, 1 Pound = 70 Rs
pounds = (dollars * 48) / 70
print("Pounds:", pounds)

# 11. Convert grams into kg
grams = 1000
print("Kg:", grams / 1000)

# 12. Convert kg into grams
kg = 1
print("Grams:", kg * 1000)

# 13. Convert bytes into KB, MB, GB
bytes_val = 1048576
print("KB:", bytes_val / 1024)
print("MB:", bytes_val / (1024 ** 2))
print("GB:", bytes_val / (1024 ** 3))

# 14. Celsius to Fahrenheit
c = 0
f = (9/5 * c) + 32
print("Fahrenheit:", f)

# 15. Fahrenheit to Celsius
f = 32
c = 5/9 * (f - 32)
print("Celsius:", c)

# 16. Calculate interest I = P*R*N/100
P, R, N = 1000, 5, 2
I = P * R * N / 100
print("Interest:", I)

# 17. Area & perimeter of square
L = 4
print("Square - Area:", L**2, "Perimeter:", 4*L)

# 18. Area & perimeter of rectangle
L, B = 4, 2
print("Rectangle - Area:", L*B, "Perimeter:", 2*(L+B))

# 19. Area of circle
R = 7
print("Circle Area:", 22/7 * R * R)

# 20. Area of triangle
H, L = 4, 8
print("Triangle Area:", H * L / 2)

# 21. Net salary = gross + allowance - deduction (10% allowance, 3% deduction)
gross_salary = 10000
allowance = 0.10 * gross_salary
deduction = 0.03 * gross_salary
net_salary = gross_salary + allowance - deduction
print("Net Salary:", net_salary)

# 22. Net sales = gross sales - 10% discount
gross_sales = 5000
net_sales = gross_sales - 0.10 * gross_sales
print("Net Sales:", net_sales)

# 23. Average and total of three subjects
s1, s2, s3 = 80, 90, 85
total = s1 + s2 + s3
average = total / 3
print("Total:", total, "Average:", average)

# 24. Swap two values
x, y = 5, 10
x, y = y, x
print("Swapped values: x =", x, "y =", y)
