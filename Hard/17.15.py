def longestWord(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
print(longestWord(words))