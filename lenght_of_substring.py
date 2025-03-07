def length_of_longest_substring(s):
    char_set = set()  # To store unique characters
    left = 0  # Left pointer of the sliding window
    max_length = 0  # To keep track of the longest substring length

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        max_length = max(max_length, right - left + 1)

    return max_length


print(length_of_longest_substring("aacat"))