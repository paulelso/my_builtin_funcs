def rfibo(num, fst=0, snd=1):
    """Find num fibonacci number recursively"""
    """print statement to show how Python is"""
    """computing all the Fibonacci numbers"""
    print('fst={:02}; snd={:02}; nums={}'.format(num, fst, snd))
    if num > 0:
        return [fst] + rfibo(num-1, snd, fst+snd)
    else:
        return []
    
print(rfibo(10))