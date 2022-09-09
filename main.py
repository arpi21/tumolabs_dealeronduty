def movezeros(intlst):
    for i in intlst:
        if i == 0:
            intlst.remove(i)
            intlst.append(0)
    return intlst

print(movezeros([0, 1, 1, 2, 0]))
