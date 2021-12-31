def is_prime(n):
    """Determines if a given integer is Prime
    """
    count = 0
    x = n

    while x != 0:
        p, q = divmod(n, x)
        x -= 1
        if q == 0:
            count += 1
    if count > 2:
        return False
    else:
        return True
    

a = int(input('Enter a number\n'))
if is_prime(a):
    print(f'{a} is Prime')
else:
    print(f'{a} is not Prime')
