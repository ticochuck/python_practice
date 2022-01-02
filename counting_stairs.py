def counting_stairs(n:int):
    """
    You are climbing a staircase. It takes n steps to reach the top. 
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """

    if n == 1 or n == 2:
        return n

    one = 1
    two = 2

    arr = [one, two]

    for i in range(n-2):
        print(one, two)
        one, two = two, one + two
        arr.append(two)

    print('arr is', arr)
    print(two, 'distinct ways')
    return two

counting_stairs(6)