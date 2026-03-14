def are_anagrams(w1, w2):

    if len(w1) != len(w2):
        return False
    count = {}

    for char in w1:
        count[char] = count.get(char, 0) + 1 #count.get(char, 0) returns the current count of char in the dictionary, or 0 if char is not yet a key in the dictionary. Then it adds 1 to that count and updates the dictionary with the new count for char.

    for char in w2:
        if char not in count:
            return False
        count[char] -= 1 #decrements the count of char in the dictionary by 1. This is because we are checking if w2 has the same characters as w1, so we need to decrease the count for each character found in w2.
        if count[char] < 0: #if the count of char becomes negative, it means that w2 has more occurrences of char than w1, which indicates that w1 and w2 cannot be anagrams. Therefore, the function returns False.
            return False
    return True
print(are_anagrams("listen", "silent"))
print(are_anagrams("aabb", "abba"))
