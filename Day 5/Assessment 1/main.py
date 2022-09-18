def maxProduct():
    lst = [int(x) for x in input().split()]
    n = len(lst)
    if n < 2:
        print("No pairs exist")
        return
    item1 = lst[0]
    item2 = lst[1]
    for i in range(0, n):
        for j in range(i + 1, n):
            if (lst[i] * lst[j] > item1 * item2):
                item1 = lst[i];
                item2 = lst[j]

    print("Max product is ", item1*item2)
    return
maxProduct()
