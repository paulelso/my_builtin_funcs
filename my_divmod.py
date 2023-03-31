def my_divmod(q, d):
    return (q//d, q%d)

qds = [(8, 3), (-8, 3),
       (10, -6), (-9, 4)]

for q, d in qds:
    print(divmod(q, d),
          my_divmod(q, d))