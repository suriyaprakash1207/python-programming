def sort_dict(n, d):
    a = int(input("Enter the element: "))
    d[n+1] = a
    print("Before sort:", d)
    sorted_a = dict(sorted(d.items(), key=lambda x: x[1]))
    print("Sorted(ascending):", sorted_a)
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print("sorted(descending):",sorted_d)
c = {1:20, 2:32, 3:47, 4:7, 5:27}
print("Original sorted keys:", sorted(c))
n = len(c)
sort_dict(n, c)
