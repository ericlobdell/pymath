'''
Exercise 1 - Even odd vending machine:
    - Print whether the number is even or odd
    - Display the number folloewd by the next 9 even or odd numbers
'''

def even_odd(x):
    return 'even' if x % 2 == 0 else 'odd'

def print_sequence(x):
    for n in range(x, x+18,2):
        print(n)

if __name__ == '__main__':
    x = int(input("Please enter your number: "))
    print("Your number ({0}) is {1}".format(x, even_odd(x)))
    print_sequence(x)

