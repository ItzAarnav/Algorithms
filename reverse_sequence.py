def inverse_array(sequence):
    inverse = []
    for i in range(len(sequence) - 1, -1, -1):
        inverse.append(sequence[i])
    return inverse


array = [1, 2, 3]

print(inverse_array(array))

