def merge_sort(a):

    l = len(a)
    if l == 1:
        return a
    a1 = merge_sort(a[:l//2])
    a2 = merge_sort(a[l//2:])
    a_sort = []
    idx1, idx2 = 0, 0
    while idx1 < len(a1) and idx2 < len(a2):
        if a1[idx1] >= a2[idx2]:
            a_sort.append(a2[idx2])
            idx2 += 1
        else:
            a_sort.append(a1[idx1])
            idx1 += 1
    if idx1 < len(a1):
        a_sort.extend(a1[idx1:])
    else:
        a_sort.extend(a2[idx2:])
    return a_sort
a=[3,8,2,9,4]
print(merge_sort(a))
