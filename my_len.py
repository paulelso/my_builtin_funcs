def my_len(seq):
    res = 0
    for elem in seq:
        res += 1
    return res

print(len('Python'), my_len('Python'))
s = enumerate('Python')
len(s)
my_len(s)