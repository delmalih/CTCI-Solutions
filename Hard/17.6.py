def numberOf2s(n):
    counter = 0
    for i in range(n+1):
        counter += str(i).count("2")
    return counter

n = 25
print(numberOf2s(n))