# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    if number % 2 == 0:
        return print(f"{number} is Even!")
    else:
        return print(f"{number} is Odd!")


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
is_even(num)
