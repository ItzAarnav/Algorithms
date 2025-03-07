def replace_negatives_with_absolute(lst):
    for i in range(len(lst)):
        if type(i) == "int":
            if lst[i] < 0:
                lst[i] = lst[i] * -1
                # Apparently, a negative number times -1 = positive number
        return lst


array = ["i", -3, 20, -15, -30, 5, 40, -1]
print(replace_negatives_with_absolute(array))
