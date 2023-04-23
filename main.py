#Print prime numbers between 50 and 100
for num in range(50, 101):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)

#Pos integer whose square is less than 100:
i = 1
while i**2 <= 100:
    print(i * i)
    i = i + 1

#Pass statement:
a=int(input("Enter number"))
b=int(input("Enter number"))

if b<a:
    pass
else:
    print("B is the greater number")

#Fibonacci
num=int(input("Enter a number"))
def fib(num):
    a,b=0,1
    while a<num:
        print(a)
        a,b=b,a+b
fib(num)

#Define a list with heterogenoeus data:
l=['Faiz',998]
print(l)

#Differentiate append and extend func:
l.append('abc')
l.extend('xyz')
print(l)

#define a dict and display all keys:
d={"Kalyan:94","Faiz:21"}
d.keys()

#dict where keys have mult values:
d={"Kalyan":[94,"Gowda"],"faiz":[21,"Khan"]}
d.values()

#set with diff operations:
    s={2,6,3,5}
    s.intersection(s)
    s.union()
    s.difference()
    s.issubset()
    s.issuperset()

#smallest and largest:
# Ask the user for input
nums = input("Enter some numbers separated by spaces: ")

# Convert the input string to a list of integers
nums_list = list(map(int, nums.split()))

# Find the smallest and largest numbers in the list
smallest = min(nums_list)
largest = max(nums_list)

# Print the smallest and largest numbers
print("The smallest number is:", smallest)
print("The largest number is:", largest)

#split the list in half and show the elements in 2 diff lists
# Define the input list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calculate the midpoint of the list
midpoint = len(my_list) // 2

# Split the list in half
list1 = my_list[:midpoint]
list2 = my_list[midpoint:]

# Print the two lists
print("List 1:", list1)
print("List 2:", list2)

#remove multiple empty strings from a list of strings:
# Define the input list
my_list = ["hello", "", "world", "", "", "python", ""]

# Use a while loop to remove empty strings
i = 0
while i < len(my_list):
    if my_list[i] == "":
        my_list.pop(i)
    else:
        i += 1

# Print the updated list
print(my_list)

#interchange first and last element in  a list
# Define the input list
my_list = [1, 2, 3, 4, 5]

# Interchange the first and last elements using a temporary variable
temp = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp

# Print the updated list
print(my_list)

#Print elements with frequency greater than the give value k:
# Define the input list and value k
my_list = [1, 2, 3, 2, 4, 1, 5, 1]
k = 2

# Create a dictionary to count the frequency of each element
freq_dict = {}
for element in my_list:
    if element in freq_dict:
        freq_dict[element] += 1
    else:
        freq_dict[element] = 1

# Print the elements with frequency greater than k
for element, freq in freq_dict.items():
    if freq > k:
        print(element)

#Find all possible combination of a list with 3 elemetns
# Define the input list
my_list = [1, 2, 3]

# Find all possible combinations of the list with 3 elements
combinations = []
for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        for k in range(j+1, len(my_list)):
            combinations.append([my_list[i], my_list[j], my_list[k]])

# Print the list of combinations
print(combinations)

#Square each elemtnt in list and print list in reverse order
# Define the input list
my_list = [1, 2, 3, 4, 5]

# Square each element in the list
squared_list = [elem ** 2 for elem in my_list]

# Print the squared list in reverse order
for i in range(len(squared_list)-1, -1, -1):
    print(squared_list[i])

#Remove all occurences of an element in a given list:
# Define the input list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

# Define the element to remove
element_to_remove = 3

# Remove all occurrences of the element
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

# Print the new list without the removed element
print(my_list)

#Program to find LCM:
# Define the two numbers
num1 = 12
num2 = 18

# Find the maximum of the two numbers
max_num = max(num1, num2)

# Define a variable to store the LCM
lcm = max_num

# Find the LCM using a loop
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += max_num

# Print the LCM
print("The LCM of", num1, "and", num2, "is", lcm)

#To find HCF:
# Define the two numbers
num1 = 54
num2 = 24

# Find the smaller of the two numbers
smaller_num = min(num1, num2)

# Find the HCF using the Euclidean algorithm
while smaller_num > 0:
    if num1 % smaller_num == 0 and num2 % smaller_num == 0:
        hcf = smaller_num
        break
    smaller_num -= 1

# Print the HCF
print("The HCF of", num1, "and", num2, "is", hcf)

#Convert decimal to binary,octal,hexa:
# Define the decimal number
decimal_num = 42

# Convert to binary
binary_num = bin(decimal_num)

# Convert to octal
octal_num = oct(decimal_num)

# Convert to hexadecimal
hex_num = hex(decimal_num)

# Print the results
print("The decimal number", decimal_num, "in binary is", binary_num)
print("The decimal number", decimal_num, "in octal is", octal_num)
print("The decimal number", decimal_num, "in hexadecimal is", hex_num)

#Find ASCII value of a character:
c='L'
ord(c)

#Program to make a simple calculator:
# Define the function for addition
def add(x, y):
    return x + y

# Define the function for subtraction
def subtract(x, y):
    return x - y

# Define the function for multiplication
def multiply(x, y):
    return x * y

# Define the function for division
def divide(x, y):
    return x / y

# Get the input from the user
print("Select operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")

#Dsiaply calendar of the given month and year:
import calendar

# Get input from the user
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Display the calendar
print(calendar.month(year, month))

#Fibonacci seq using recursion:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# Get input from the user
n = int(input("Enter the number of terms: "))

# Check if the input is valid
if n <= 0:
    print("Invalid input! Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))

#Factorail using recursion:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get input from the user
n = int(input("Enter a positive integer: "))

# Check if the input is valid
if n < 0:
    print("Invalid input! Please enter a positive integer.")
else:
    result = factorial(n)
    print(f"{n}! = {result}")

#Max of 3 numbers:
# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum of the three numbers using if-else statements
if num1 > num2 and num1 > num3:
    max_num = num1
elif num2 > num1 and num2 > num3:
    max_num = num2
else:
    max_num = num3

# Print the maximum number
print(f"The maximum number is {max_num}")

#sum of all numbers in a list:
# Define a list of numbers
num_list = [5, 10, 15, 20, 25]

# Find the sum of all numbers in the list using a for loop
sum = 0
for num in num_list:
    sum += num

# Print the sum of all numbers in the list
print(f"The sum of all numbers in the list is {sum}")

#calculate factorial of a number:
# Get input from the user
num = int(input("Enter a number: "))

# Calculate the factorial of the number
factorial = 1
for i in range(1, num + 1):
    factorial *= i

# Print the factorial of the number
print(f"The factorial of {num} is {factorial}")

#Whethere a give number falls within the given range:
# Get input from the user
num = float(input("Enter a number: "))
lower = float(input("Enter the lower end of the range: "))
upper = float(input("Enter the upper end of the range: "))

# Check if the number falls within the range
if num >= lower and num <= upper:
    print(f"{num} falls within the range of {lower} and {upper}")
else:
    print(f"{num} does not fall within the range of {lower} and {upper}")

#accept string and count the no of upper and lower case:

# Get input from the user
string = input("Enter a string: ")

# Initialize counters
upper_count = 0
lower_count = 0

# Iterate through each character in the string
for char in string:
    # Check if the character is uppercase or lowercase
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

# Print the counts of uppercase and lowercase characters
print(f"Number of uppercase characters: {upper_count}")
print(f"Number of lowercase characters: {lower_count}")

#takes a list and returns a new list with disticnt ele from the first list:

# Get input from the user
input_list = input("Enter a list of elements separated by spaces: ").split()

# Convert input to a list of integers (if applicable)
try:
    input_list = [int(elem) for elem in input_list]
except ValueError:
    pass

# Create a new list with distinct elements from the input list
output_list = []
for elem in input_list:
    if elem not in output_list:
        output_list.append(elem)

# Print the output list
print(output_list)


#prime or not:
# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            is_prime = False
            break

# Print the result
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

#print even numbers in a list:

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the list and print even numbers
for num in numbers:
    if num % 2 == 0:
        print(num)

#String passed is palindrome or not

# Get input from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
is_palindrome = True
for i in range(len(string)//2):
    if string[i] != string[-i-1]:
        is_palindrome = False
        break

# Print the result
if is_palindrome:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")

#print out first n rows of pascals triangle

# Define a function to generate Pascal's triangle
def pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

# Get input from the user
n = int(input("Enter the number of rows to generate: "))

# Print out the first n rows of Pascal's triangle
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
