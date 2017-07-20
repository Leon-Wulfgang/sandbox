a = [5, 2, 4, 6, 1, 3]

print('insertion_sort: ', a)
total = 0

for j in range(1, len(a)):
    key = a[j]
    i = j - 1
    while (i>=0) and (a[i]>key):
        a[i+1] = a[i]
        i = i-1
        total+=1
    a[i+1] = key
    print('j++: key%s i%s j%s' % (key, i, j), a)

print('done in %s steps:' % total, a)

