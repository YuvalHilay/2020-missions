def insert_into_sorted(a, index):
    num=a[index]
    i=index-1
    while a[i]>num and i>=0:
        a[i+1]=a[i]
        i-=1
    a[i+1]=num

def insertion_sort(a, n):
    for i in range (1, n):
        insert_into_sorted(a, i)

a=[5, 4, 3, 1, 2]
print(insertion_sort(a,5))
