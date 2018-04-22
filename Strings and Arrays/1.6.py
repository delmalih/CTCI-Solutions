'''
----------------------
| String compression | 
----------------------

-> Best Conceivable Algorithm : O(n)
'''

'''
-- Examples --
'''

example1 = "aabcccccaaa"    # --> a2b1c5a3

'''
Solution 1 - Naive

Complexity: O(n)
'''

print("SOLUTION 1 - Naive - O(n)")

def stringCompression1(string):
    res_array = list()
    counter = 0
    currentChar = string[0]
    currentCounter = 0
    while counter < len(string):
        if string[counter] == currentChar:
            currentCounter += 1
        else:
            res_array.append(currentChar)
            res_array.append(str(currentCounter))
            currentChar = string[counter]
            currentCounter = 1
        counter += 1
    res_array.append(currentChar)
    res_array.append(str(currentCounter))
    return ''.join(res_array)

print("Test 1 - (Expected 'a2b1c5a3') : {}".format(stringCompression1(example1)))
        