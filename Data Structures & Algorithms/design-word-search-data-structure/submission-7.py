class Node:
    def __init__(self, char = None):
        self.char = char
        self.children = {}
        self.end_of_word = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = Node(char = c)
            current = current.children[c]
        current.end_of_word = True

    def search(self, word: str) -> bool:
        current_set = [self.root]
        for c in word:
            next_set = []
            for ele in current_set:
                if c == ".":
                    for child in ele.children.keys():
                        next_set.append(ele.children[child])
                elif c in ele.children:
                    next_set.append(ele.children[c])
            current_set = next_set
        for ele in current_set:
            if ele.end_of_word:
                return True
        return False