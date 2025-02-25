# Function
# Write a function say_hello() that prints "Hello, World!". Call it once.
def say_hello():
    print("Hello World!")

say_hello()



# Greet User
# Write a function greet(name) that takes a name as an argument and prints "Hello, <name>!".
def greet(name):
    print("Hello", name)

greet("Miralem")



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
# Test
print(add(3, 70))



# Sum of List
# Write a function sum_list(numbers) that takes a list of numbers and returns their sum.
def sum_list(numbers):
    return sum(numbers)
# Test
print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))



# Durchschnitt einer Liste berechnen
def average(numbers):
    if len(numbers) == 0:  # Überprüfung, um Division durch 0 zu vermeiden
        return 0
    return sum(numbers) / len(numbers)
# Test
numbers = [10, 20, 30, 40, 50]
print("Anzahl der Zahlen:", len(numbers))
print("Summe:", sum(numbers))
print("Durchschnitt:", average(numbers))


# Fibonacci Sequence
# Anzahl der Fibonacci-Zahlen, die ausgegeben werden sollen
n = 20  
# Die ersten beiden Zahlen der Fibonacci-Folge
num1 = 0  
num2 = 1  
next_number = num2                                      # # Die nächste Zahl in der Sequenz (startet mit num2)  
count = 1                                               # Zähler, um die Anzahl der ausgegebenen Zahlen zu verfolgen
# Die Schleife läuft, bis wir die gewünschte Anzahl an Zahlen ausgegeben haben
while count <= n:
    print(next_number, end=" ")                         # Die aktuelle Zahl ausgeben, mit Leerzeichen statt neuer Zeile
    
    count += 1                                          # Zähler um 1 erhöhen
    num1, num2 = num2, next_number                      # Werte aktualisieren: num1 wird zu num2, num2 wird zu next_number
    next_number = num1 + num2                           # Die nächste Zahl in der Fibonacci-Folge berechnen  
    if count > n:                                       # Anzahl zu hoch wird die Schleife beenden
        break
print()  

# Function for nth fibonacci number 
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
# Driver Program
print(fibonacci(12))

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
print(Fibonacci(20))

# Function for nth fibonacci ( nth = n-te Zahl in der Fibonacci-Folge.)
# number
FibArray = [0, 1]

def fibonacci(n):
  
    # Check is n is less 
    # than 0
    if n < 0:
        print("Incorrect input")
        
    # Check is n is less 
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:        
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]

# Driver Program
print(fibonacci(9))



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
print(count_vowels("aabccdeefgghiijkklmmnoopqqrsstuuvwwxyyz"))