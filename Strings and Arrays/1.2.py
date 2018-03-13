'''
---------------------
| Check Permutation | 
---------------------
We must at least visit once each characters of both strings
(Tip) - If the two strings does not have the same length, the result if False
        Thus, let n be the lenght of both strings
-> Best Conceivable Algorithm : O(n)
'''

'''
-- Examples --
'''

true_smallExample = ("abcd", "badc")
true_bigExample = ("abcdefghijklmnopqrstuvwxyz&é(§è!çà)-$*`£<>@#", "ué(§)-$*`ogwrabcdnhisxèjlmqtpefk!çàyz&£<>@#")
false_smallExample = ("aabc", "aze")
false_bigExample = ("abzsamdriuopshtvnmwdisééaçex)$`:`:)-<<@d,zcm", "abzsamdriuopshtvnmwdisééaçex)$`:`:)-<<@d,zcn")

'''
Solution 1 - Naive
For each character of string A, we check if it is in string B
Complexity: O(n^2)
'''

print("SOLUTION 1 - Naive - O(n^2)")

def checkPermutation1(stringA, stringB):
    if len(stringA) == len(stringB):
        return False
    for char in stringA:
        if char not in stringB:
            return False
    return True

print("Test 1 - Small example (Expected True) :", checkPermutation1(true_smallExample[0], true_smallExample[1]))
print("Test 2 - Small example (Expected False) :", checkPermutation1(false_smallExample[0], false_smallExample[1]))
print("Test 3 - Big example (Expected True) :", checkPermutation1(true_bigExample[0], true_bigExample[1]))
print("Test 4 - Big example (Expected False) :", checkPermutation1(false_bigExample[0], false_bigExample[1]))

'''
Solution 2 - Quick Sort
Two strings that are permutations should have the same characters, but in different orders
Why don't we make the orders the same ? Using a quick sort for example
Complexity: O(nlog(n))
'''

print("SOLUTION 2 - Quick Sort - O(nlog(n))")

def checkPermutation2(stringA, stringB):
    if len(stringA) == len(stringB):
        return False
    stringToNumbersA = [ord(char) for char in stringA]  # <-- O(n)
    stringToNumbersB = [ord(char) for char in stringB]  # <-- O(n)
    stringToNumbersA = sorted(stringToNumbersA)         # <-- O(nlog(n))
    stringToNumbersB = sorted(stringToNumbersB)         # <-- O(nlog(n))
    for i in range(len(stringA)):
        if (stringToNumbersA[i] !== stringToNumbersB[i]):
            return False
    return True

print("Test 1 - Small example (Expected True) :", checkPermutation2(true_smallExample[0], true_smallExample[1]))
print("Test 2 - Small example (Expected False) :", checkPermutation2(false_smallExample[0], false_smallExample[1]))
print("Test 3 - Big example (Expected True) :", checkPermutation2(true_bigExample[0], true_bigExample[1]))
print("Test 4 - Big example (Expected False) :", checkPermutation2(false_bigExample[0], false_bigExample[1]))

'''
Solution 3 - Hash Set
By using a hash set and the same algorithm as solution 1, the lookup time complexity is now constant - O(1)
Complexity: O(n)
'''

print("SOLUTION 3 - Hash Set - O(n)")

def checkPermutation3(stringA, stringB):
    if len(stringA) == len(stringB):
        return False
    hashSet = set()
    for char in stringA:
        hashSet.add(char)
    for char in stringB:
        if char not in hashSet:
            return False
    return True

print("Test 1 - Small example (Expected True) :", checkPermutation3(true_smallExample[0], true_smallExample[1]))
print("Test 2 - Small example (Expected False) :", checkPermutation3(false_smallExample[0], false_smallExample[1]))
print("Test 3 - Big example (Expected True) :", checkPermutation3(true_bigExample[0], true_bigExample[1]))
print("Test 4 - Big example (Expected False) :", checkPermutation3(false_bigExample[0], false_bigExample[1]))
