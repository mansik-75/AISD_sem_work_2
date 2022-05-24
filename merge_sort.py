def merge_sort(lst: list):
    if len(lst) <= 1:
        return lst
    length = len(lst) // 2
    a, b = lst[:length], lst[length:]
    a = merge_sort(a)
    b = merge_sort(b)
    res = []
    ia = 0
    ib = 0
    length_a = len(a)
    length_b = len(b)
    while ia < length_a or ib < length_b:
        if length_a == ia:
            res.append(b[ib])
            ib += 1
            continue
        if length_b == ib:
            res.append(a[ia])
            ia += 1
            continue
        if a[ia] < b[ib]:
            res.append(a[ia])
            ia += 1
        else:
            res.append(b[ib])
            ib += 1
    return res
