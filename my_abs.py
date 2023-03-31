def my_abs(n):
    if n < 0:
        return -n
    else:
        return n

# run number in for loop to compare results
for n in [-5, -3.14, 0, 9]:
    print(abs(n), my_abs(n))