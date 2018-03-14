'''
------------
| IsUnique | 
------------
We must at least visit once each element of the string
-> Best Conceivable Algorithm : O(n)
'''

'''
-- Examples --
'''

true_smallExample = "abcd"
false_smallExample = "aabc"
true_bigExample = "abcdefghijklmnopqrstuvwxyz&é(§è!çà)-$*`£<>@#"
false_bigExample = "abzsamdriuopshtvnmwdisééaçex)$`:`:)-<<@d,zcm"

'''
Solution 1 - Naive
We take each character and compare it with the others
We return false if we meet the same character
Complexity: O(n^2)
'''

print("SOLUTION 1 - Naive - O(n^2)")

def isUnique1(inputString):
    for i in range(len(inputString)-1):
        for j in range(i+1, len(inputString)):
            if inputString[i] == inputString[j]:
                return False
    return True

print("Test 1 - Small example (Expected True) : {}".format(isUnique1(true_smallExample)))
print("Test 2 - Small example (Expected False) : {}".format(isUnique1(false_smallExample)))
print("Test 3 - Big example (Expected True) : {}".format(isUnique1(true_bigExample)))
print("Test 4 - Big example (Expected False) : {}".format(isUnique1(false_bigExample)))

'''
Solution 2 - Using a hash set
We can use a hash set to store all characters of the string
For each character visited, either he is already in the hashset, we return false
or we add it to the hashset
Complexity: O(n)
'''

print("")
print("SOLUTION 2 - Hash Set - O(n)")

def isUnique2(inputString):
    hashSet = set()
    for char in inputString:
        if char in hashSet:
            return False
        hashSet.add(char)
    return True

print("Test 1 - Small example (Expected True) : {}".format(isUnique2(true_smallExample)))
print("Test 2 - Small example (Expected False) : {}".format(isUnique2(false_smallExample)))
print("Test 3 - Big example (Expected True) : {}".format(isUnique2(true_bigExample)))
print("Test 4 - Big example (Expected False) : {}".format(isUnique2(false_bigExample)))

'''
Solution 3 - Without data structure
We create the list of ascii values of all the characters of the input string
We sort that list and we check if there is any duplicated value 
Complexity: O(nlog(n))
'''

print("")
print("Solution 3 - Without Data Structure - O(nlog(n))")

def isUnique3(inputString):
    stringToNumbers = [ord(char) for char in inputString]   # <-- O(n)
    stringToNumbers = sorted(stringToNumbers)               # <-- O(nlog(n))
    for i in range(len(stringToNumbers)-1):
        if (stringToNumbers[i] == stringToNumbers[i+1]):
            return False
    return True

print("Test 1 - Small example (Expected True) : {}".format(isUnique3(true_smallExample)))
print("Test 2 - Small example (Expected False) : {}".format(isUnique3(false_smallExample)))
print("Test 3 - Big example (Expected True) : {}".format(isUnique3(true_bigExample)))
print("Test 4 - Big example (Expected False) : {}".format(isUnique3(false_bigExample)))
