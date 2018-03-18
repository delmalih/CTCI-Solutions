'''
----------
| URLify | 
----------
We must at least visit each character of the string
-> Best Conceivable Algorithm : O(n)
'''

'''
-- Examples --
'''

smallExample = ("Mr John Smith     ", 13)
bigExample = ("  Hello  World : This is a    test to URLify function   ", 51)

'''
Solution 1 - Naive
First, we can "strip" the string to remove spaces before and after the string
We can create a new string and for each character, either append it to the new string if
it is not a space or add '%20' if it is
Since we create a copy of the string for each append, the complexity is O(n^2)
Complexity: O(n^2)
'''

print("SOLUTION 1 - Naive - O(n^2)")

def URLify1(string, length):
    string = string.strip() 
    newString = ""
    for char in string:
        if char == " ":
            newString += "%20"
        else:
            newString += char
    return newString

print("Test 1 - Small example : {} -> {}".format(smallExample[0], URLify1(smallExample[0], smallExample[1])))
print("Test 2 - Big example : {} -> {}".format(bigExample[0], URLify1(bigExample[0], bigExample[1])))

'''
Solution 2 - Counting Spaces
First, we can "strip" the string to remove spaces before and after the string
We can count the number of spaces in the string, knowing its length, we can find the length of the new string
We create an array containing the characters of the new string and concat this array (simulation of a StringBuilder)
Complexity: O(n)
'''

print("")
print("SOLUTION 2 - Counting Spaces - O(n)")

def URLify2(string, length):
    string = string.strip()
    numberSpaces = string.count(" ")                # <-- O(n)
    newStringLength = length + 2*numberSpaces
    newStringArray = [""] * newStringLength         # <-- O(n)
    indexString = 0; indexNewString = 0
    while indexNewString < newStringLength:         # <-- O(n)
        if string[indexString] == " ":
            newStringArray[indexNewString] = "%"
            newStringArray[indexNewString+1] = "2"
            newStringArray[indexNewString+2] = "0"
            indexNewString += 3
        else:
            newStringArray[indexNewString] = string[indexString]
            indexNewString += 1
        indexString += 1
    newString = "".join(newStringArray)              # <-- O(n)  
    return newString

print("Test 1 - Small example : {} -> {}".format(smallExample[0], URLify2(smallExample[0], smallExample[1])))
print("Test 2 - Big example : {} -> {}".format(bigExample[0], URLify2(bigExample[0], bigExample[1])))
