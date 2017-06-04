''' 
Multiplication table printer
'''

def multi_table(x):
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(x, i, x*i))

if __name__ == '__main__':
    x = input('Enter a number: ')
    multi_table(float(x))

