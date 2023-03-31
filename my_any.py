def my_any(it):
    for elem in it:
        if not elem:
            return False
    return True

print(any([0, False, (), {}]))
print(my_any([0, False, (), {}]))
print(any([0, False, 1, (), {}]))
print(my_any([0, False, 1, (), {}]))
print(any([]), my_any([]))