class Node(object):
    def __init__(self, data):
        self.data = data
        self.childrens = list()

    def addChildren(self, node):
        self.childrens.append(node)
    
    def __repr__(self):
        return self.data

class Trie(object):
    def __init__(self):
        self.start = Node("START")
         
    def addWord(self, word):
        pointer = self.start
        goDeeper = True
        i = 0
        while goDeeper and i < len(word):
            dataChildren = [n.data for n in pointer.childrens]
            if word[i] in dataChildren:
                pointer = pointer.childrens[dataChildren.index(word[i])]
                goDeeper = True
                i += 1
            else:
                goDeeper = False
        while i < len(word):
            newNode = Node(word[i])
            pointer.addChildren(newNode)
            pointer = newNode
            i += 1
        pointer.addChildren(Node("*"))
        

def createTrie(dic):
    trie = Trie()
    for word in dic:
        trie.addWord(word)
    return trie
    
def reSpace(seq, dic):
    

seq = "jesslookedjustliketimherbrother"
dic = {'looked', 'look', 'just', 'like', 'her', 'brother', 'sister', 'his', 'him'}

trie = createTrie(dic)
trie.read()