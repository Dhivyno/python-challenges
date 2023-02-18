def tower(num, first, second, third):
    if num == 0:
        return
    tower(num-1, first, third, second)
    print("Move disk of size", num, "from rod", first, "to rod", second)
    tower(num-1, third, second, first)

n = 3

tower(n, 'firstRod', 'secondRod', 'thirdRod')
 