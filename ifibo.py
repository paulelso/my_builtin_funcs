def ifibo(num):
    """Find num fibonacci numbers iteratively"""
    """first two terms"""
    fst, snd = 0, 1
    nums = []
    for x in range(num):
        """print statement to show how Python is"""
        """computing all the Fibonacci numbers"""
        print('fst={:02}; snd={:02}; nums={}'.format(fst, snd, nums))
        nums.append(fst)
        fst, snd = snd, fst+snd
    return nums

print(ifibo(10))