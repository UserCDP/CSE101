"""
Copyright Daniela Cojocaru 2022:)
"""

# Exercise 1
def gcd(a, b):
    """Find the greatest common divisor (gcd)"""
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a%b)

# Exercise 2
def is_palindrome(word):
    """
    We check if we have only one letter, then return True
    if we have 2 letters left and they are the same return True
    if len > 2 then check the first and last letter, return False if different
    """
    print (word)
    if len(word) <= 1:
        return True
    if word[0] != word[len(word)-1]:
        return False
    return is_palindrome(word[1:len(word)-1])

# Exercise 3
def rec_pow(a, b):
    """Raise a to the power of b"""
    if b == 0 or a == 1:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return rec_pow(a*a, b//2)
    return rec_pow(a*a, (b-1)//2)*a

# Exercise 4
def binary_search(sorted_list, lower, upper, element):
    """
    check if the middle element is the one we are searching
    if less, search from lower to the middle
    if more, search from the middle to upper
    """

    if lower > upper-1 or lower > len(sorted_list)-1:
        return -1
    middle = (lower+upper) // 2
    if sorted_list[middle] == element:
        return middle

    if element < sorted_list[middle]:
        return binary_search(sorted_list, lower, middle, element)
    else:
        return binary_search(sorted_list, middle+1, upper, element)

# Optional for Exercise 4
def binary_search_simple(sorted_list, element):
    return binary_search(sorted_list, 0, len(sorted_list) - 1, element)

# Exercise 5
def find_subsets(s):
    """Return all subsets of s"""
    result = []
    if len(s) == 0:
        return [set()]

    s_copy = s.copy()
    elem = s_copy.pop()
    result = find_subsets(s_copy)

    result_copy = result.copy()

    for item in result_copy:
        item_copy = item.copy()
        item_copy.add(elem)
        result.append(item_copy)
    return result

# Exercise 6
def find_permutations(arr):
    result = []
    #print(arr)
    if len(arr) == 0 or len(arr) == 1:
        return [arr]
    for item in arr:
        temp = arr.copy()
        temp.remove(item)
        remaining_perm = find_permutations(temp)
        for p in remaining_perm:
            result.append([item] + p)
    return result

# Exercise 7
def load_dictionary(filename):
    with open(filename, 'r') as f:
        words = [line.strip() for line in f]
        return words

def find_acronyms(phrase, word_list):
    """Find each word in word_list that can be constructed
    by taking one letter from each word in phrase, in order.
    """
    return find_acronyms_rec(phrase.split(), '', word_list)

def find_acronyms_rec(phrase_words, prefix, word_list):
    acronyms = set()
    if len(phrase_words) == 0:
        if binary_search_simple(word_list, prefix) != -1:
            return {prefix}
    else:
        for letter in phrase_words[0]:
            acronyms = acronyms.union(find_acronyms_rec(phrase_words[1:], prefix + letter, word_list))

    return acronyms
