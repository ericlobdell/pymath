'''
Find the factors of an integer
'''

def factors(x):
    for i in range(1, x+1):
        if x % i == 0:
            print(i)


if __name__ == '__main__':
    b = input('Your number please: ')
    b = int(b)

    if b > 0:
        factors(b)
    else:
        print('Please enter a positive integer.')

