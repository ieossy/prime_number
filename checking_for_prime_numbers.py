# checking if a number is a prime number
def is_prime_number(z):
    # number must be positive and greater than one
    if z >= 2:
        # iterate through 2 and half the number
        for y in range(2, z // 2):
            if z % y == 0:
                return False 
        else:
            return True
            
    else:
        return False

number = int(input('Please enter a number: '))

if is_prime_number(number):
    print('{} is a prime number'. format(number))
else:
    print('{} is not a prime number'.format(number))
