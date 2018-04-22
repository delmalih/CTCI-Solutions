import heapq

def smallestKnumbers(arr, k):
    heap = heapq.heapify(arr)
    smallests = list()
    for i in range(k):
        smallests.append(heapq.heappop(arr))
    return smallests

example = [1, 2, 1, 0, -2, 4, 3, 4, 7]

for k in range(1, 6):
    example_k = example[:]
    print(smallestKnumbers(example_k, k))
