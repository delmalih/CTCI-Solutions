'''
--------------------------
| Palindrome Permutation | 
--------------------------
We must at least visit once each character the string
-> Best Conceivable Algorithm : O(n)
'''

'''
-- Examples --
'''

true_smallExample = "4521343125"
false_smallExample = "4421243825"
true_bigExample = "846264320197654900987890123983210615758177655456723490123843"
false_bigExample = "824220571043333294325231433375866474592141405935095541006474"

'''
Solution 1 - Naive
We can simply count each occurence of a character in the string.
If thoses numbers are all divisible by 2, the it is a permutation of a palindromic number.
Complexity: O(n^2)
'''

print("SOLUTION 1 - Naive - O(n^2)")

def palindromePermutation1(string):
    for char in string:                     # <-- O(n)
        if string.count(char)%2 != 0:       # <-- O(n)
            return False
    return True

print("Test 1 - Small example (Expected True) : {}".format(palindromePermutation1(true_smallExample)))
print("Test 2 - Small example (Expected False) : {}".format(palindromePermutation1(false_smallExample)))
print("Test 3 - Big example (Expected True) : {}".format(palindromePermutation1(true_bigExample)))
print("Test 4 - Big example (Expected False) : {}".format(palindromePermutation1(false_bigExample)))

'''
Solution 2 - Hash Table
We can improve the wat we count each occurence using a hash table.
Complexity: O(n)
'''

print("")
print("SOLUTION 2 - Hash Table - O(n)")

def palindromePermutation2(string):
    hashTable = dict()
    for char in string:             # <-- O(n)
        if char in hashTable:       # <-- O(1)
            hashTable[char] += 1
        else:
            hashTable[char] = 1
    for char in hashTable:          # <-- O(n)
        if hashTable[char]%2 != 0:
            return False
    return True

print("Test 1 - Small example (Expected True) : {}".format(palindromePermutation2(true_smallExample)))
print("Test 2 - Small example (Expected False) : {}".format(palindromePermutation2(false_smallExample)))
print("Test 3 - Big example (Expected True) : {}".format(palindromePermutation2(true_bigExample)))
print("Test 4 - Big example (Expected False) : {}".format(palindromePermutation2(false_bigExample)))
