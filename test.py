# Function
# Write a function say_hello() that prints "Hello, World!". Call it once.
def say_hello():
    print("Hello World!")

say_hello()


# Greet User
# Write a function greet(name) that takes a name as an argument and prints "Hello, <name>!".
def greet(name):
    print("Hello", {name})

greet("name")


# Check Even or Odd
# Write a function is_even(n) that returns True if n is even and False otherwise.
def is_even(n):                                     # is_even(n): Prüft, ob eine Zahl gerade ist.
    return n % 2 == 0
# Test
print(is_even(4))
print(is_even(7))

# Find Maximum
# Write a function max_of_two(a, b) that returns the larger of two numbers.
def max_of_two(a, b):                               # max_of_two(a, b): Gibt die größere von zwei Zahlen zurück.
    return a if a > b else b
# Test
print(max_of_two(6, 2))
print(max_of_two(4, 10))


# Add Two Numbers
#Write a function add(a, b) that returns the sum of two numbers.
def add(a, b):
    return(a + b)


# Sum of List
# Write a function sum_list(numbers) that takes a list of numbers and returns their sum.
def sum_list(numbers):
    return sum(numbers)


# Fibonacci Sequence
# Write a function fibonacci(n) that returns the nth Fibonacci number using recursion.(https://de.wikipedia.org/wiki/Fibonacci-Folge)
def Fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
# Driver Program
print(Fibonacci(9))



# Reverse a String
# Write a function reverse_string(s) that takes a string and returns it reversed.
def reverse_strint(s):                              # reverse_string(s): Dreht einen String um.
    return s[::-1]

print(reverse_strint("hallo"))
print(reverse_strint("miralem"))

# Count Vowels
# Write a function count_vowels(s) that counts the number of vowels (a, e, i, o, u) in a given string.
def count_vowels(s):                                # count_vowels(s): Zählt die Anzahl der Vokale im String.
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("banana"))
print(count_vowels("miralem"))
print(count_vowels("beautiful"))