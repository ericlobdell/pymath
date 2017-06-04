'''
Exercise 2:
    - Enhance multiplication table generator to allow user to spicify 
    - how many multiples they want to see
'''

def multi_table(x, n):
    for i in range(1,n + 1):
        print('{0} x {1} =\t{2}'.format(x, i, x*i))

if __name__ == '__main__':
    x = input('Enter a number: ')
    n = input('How many multiples would you like to generate? ')
    multi_table(float(x), int(n))