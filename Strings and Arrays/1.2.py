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
false_smallExample = ("aabc", "aze")
true_bigExample = ("abcdefghijklmnopqrsmqatuvwxyz&é(§è!çà)-$*`£<>@#", "pweu`£è!çà)jqmakldvxbcfghrstqo*<>@#yz&éimn(§a-$")
false_bigExample = ("abzsamdriuopshtvnmwdisééaçex)$`:`:)-<<@d,zcm", "abzsamdriuopshtvnmwdisééaçex)$`:`:)-<<@d,zcn")

'''
Solution 1 - Naive
We take each character of A and compare the number of time it occurs in strings A and B
If A and B are permutations, thoses numbers has to be equals
Complexity: O(n^2)
'''

print("SOLUTION 1 - Naive - O(n^2)")

def checkPermutation1(stringA, stringB):
    if len(stringA) != len(stringB):
        return False
    for char in stringA:
        if stringB.count(char) != stringA.count(char):
            return False
    return True

print("Test 1 - Small example (Expected True) : {}".format(checkPermutation1(true_smallExample[0], true_smallExample[1])))
print("Test 2 - Small example (Expected False) : {}".format(checkPermutation1(false_smallExample[0], false_smallExample[1])))
print("Test 3 - Big example (Expected True) : {}".format(checkPermutation1(true_bigExample[0], true_bigExample[1])))
print("Test 4 - Big example (Expected False) : {}".format(checkPermutation1(false_bigExample[0], false_bigExample[1])))

'''
Solution 2 - Quick Sort
Two strings that are permutations should have the same characters, but in different orders
Why don't we make the orders the same ? Using a quick sort for example
Complexity: O(nlog(n))
'''

print("")
print("SOLUTION 2 - Quick Sort - O(nlog(n))")

def checkPermutation2(stringA, stringB):
    if len(stringA) != len(stringB):
        return False
    stringToNumbersA = [ord(char) for char in stringA]  # <-- O(n)
    stringToNumbersB = [ord(char) for char in stringB]  # <-- O(n)
    stringToNumbersA = sorted(stringToNumbersA)         # <-- O(nlog(n))
    stringToNumbersB = sorted(stringToNumbersB)         # <-- O(nlog(n))
    for i in range(len(stringA)):
        if (stringToNumbersA[i] != stringToNumbersB[i]):
            return False
    return True

print("Test 1 - Small example (Expected True) :", checkPermutation2(true_smallExample[0], true_smallExample[1]))
print("Test 2 - Small example (Expected False) :", checkPermutation2(false_smallExample[0], false_smallExample[1]))
print("Test 3 - Big example (Expected True) :", checkPermutation2(true_bigExample[0], true_bigExample[1]))
print("Test 4 - Big example (Expected False) :", checkPermutation2(false_bigExample[0], false_bigExample[1]))

'''
Solution 3 - Hash Table
We can use a hash tables and store each time we visit a character for stirngs A and B
Complexity: O(n)
'''

print("")
print("SOLUTION 3 - Hash Table - O(n)")

def storeCounting(string):
    hashTable = dict()
    for char in string:
        if char in hashTable:
            hashTable[char] += 1
        else:
            hashTable[char] = 1
    return hashTable

def checkPermutation3(stringA, stringB):
    if len(stringA) != len(stringB):
        return False
    hashTableA = storeCounting(stringA)     # <-- O(n)
    hashTableB = storeCounting(stringB)     # <-- O(n)
    for char in hashTableA:                 # <-- O(n)
        if char not in hashTableB:
            return False
        if hashTableA[char] != hashTableB[char]:
            return False
    return True

print("Test 1 - Small example (Expected True) :", checkPermutation3(true_smallExample[0], true_smallExample[1]))
print("Test 2 - Small example (Expected False) :", checkPermutation3(false_smallExample[0], false_smallExample[1]))
print("Test 3 - Big example (Expected True) :", checkPermutation3(true_bigExample[0], true_bigExample[1]))
print("Test 4 - Big example (Expected False) :", checkPermutation3(false_bigExample[0], false_bigExample[1]))
