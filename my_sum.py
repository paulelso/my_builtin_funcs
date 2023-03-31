def my_sum(it, start=0):
    res = start
    for elem in it:
        res += elem
    return res

print(sum(range(6)), my_sum(range(6)))
print(my_sum(range(6), 5), my_sum(range(6), 5))
print(sum([[0, 1], [2, 3]], []))
print(my_sum([[0, 1], [2, 3]], []))
print(sum([[0, 1], [2, 3]], []))
print(my_sum([[0, 1], [2, 3]], []))
print(sum(['a', 'b', 'c',], ''))
print(my_sum(['a', 'b', 'c',], ''))