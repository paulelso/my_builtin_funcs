_sentinel = object()
def my_adv_min(it, *, key=None, default=_sentinel):
    if not it and default is not _sentinel:
        return default
    key = key or (lambda x: x)
    minkey, minres = key(it[0]), it[0]
    for elem in it [1:]:
        k = key(elem)
        if k < minkey:
            minkey, minres = k, elem
    return minres

seq = ['xxxx', 'aaaaaaaa', 'yy', 'zzz']
print(min(seq), my_adv_min(seq))
print(min(seq, key=len), my_adv_min(seq, key=len))
print(min([], default=0), my_adv_min([], default=0))