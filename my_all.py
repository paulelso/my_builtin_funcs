def my_all(it):
    for elem in it:
        if not elem:
            return False
    return True

print(all([1, True, 'X']))
print(my_all([1, True, 'X']))
print(all([1, True, 0, 'X']))
print(my_all([1, True, 0, 'X']))
print(all([]), my_all([]))