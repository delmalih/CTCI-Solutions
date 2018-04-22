'''
------------
| One Away | 
------------

-> Best Conceivable Algorithm : O(n)
'''

'''
-- Examples --
'''

true_Example1 = ("pale", "ple")     # -> true
true_Example2 = ("pales", "pale")   # -> true
true_Example3 = ("pale", "bale")    # -> true
false_Example4 = ("pale", "bake")   # -> false

'''
Solution 1 - Hash Table

Complexity: O(n)
'''

print("SOLUTION 1 - Hash Table - O(n)")

def strToHashMap(string):
    hashMap = dict()
    for s in string:
        if s in hashMap:
            hashMap[s] += 1
        else:
            hashMap[s] = 1
    return hashMap

def delta(hashMap1, hashMap2):
    diff = 0
    for el in hashMap1:
        if el in hashMap2:
            diff += abs(hashMap1[el] - hashMap2[el])
        else:
            diff += hashMap1[el]
    for el in hashMap2:
        if el not in hashMap1:
            diff += hashMap2[el]
    return diff

def oneReplace(str1, str2):
    if len(str1) != len(str2):
        return False
    diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1
    return diff == 1

def oneBlank(str1, str2):
    if abs(len(str1) - len(str2)) != 1:
        return False
    hashMap1 = strToHashMap(str1)
    hashMap2 = strToHashMap(str2)
    diff = delta(hashMap1, hashMap2)
    return diff == 1

def oneAway1(data):
    str1, str2 = data
    one_blank = oneBlank(str1, str2)        # <-- O(n)
    one_replace = oneReplace(str1, str2)    # <-- O(n)
    return one_blank or one_replace

print("Test 1 - (Expected True) : {}".format(oneAway1(true_Example1)))
print("Test 2 - (Expected True) : {}".format(oneAway1(true_Example2)))
print("Test 3 - (Expected True) : {}".format(oneAway1(true_Example3)))
print("Test 4 - (Expected False) : {}".format(oneAway1(false_Example4)))
