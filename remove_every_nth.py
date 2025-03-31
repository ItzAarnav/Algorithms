def remove_every_nth(arr, n):
    return arr[::(n+1)]


array = [1, 2, 3, 4, 5, 6]
print(remove_every_nth(array, 2))
