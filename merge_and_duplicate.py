def merge_and_deduplicate(list1, list2):
    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if len(result) == 0 or result[-1] != list1[i]:
                result.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if len(result) == 0 or result[-1] != list2[j]:
                result.append(list2[j])
            j += 1
        else:
            if len(result) == 0 or result[-1] != list1[i]:
                result.append(list1[i])
            i += 1
            j += 1

    while i < len(list1):
        if len(result) == 0 or result[-1] != list1[i]:
            result.append(list1[i])
        i += 1

    while j < len(list2):
        if len(result) == 0 or result[-1] != list2[j]:
            result.append(list2[j])
        j += 1

    return result








list1 = [12, 3, 2, 8]
list2 = [3, 4, 6, 7, 8]

