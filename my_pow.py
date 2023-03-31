def my_pow(x, y, z=None):
    result = x**y
    if z is not None:
        result %= z
    return result
    
# comparing original pow
print(my_pow(2, 8), my_pow(2, 8))
print(my_pow(-2, 8), my_pow(-2, 8))
print(my_pow(-2.5, 8), my_pow(-2.5, 8))
print(my_pow(-2, 8, 50), my_pow(-2, 8, 50))