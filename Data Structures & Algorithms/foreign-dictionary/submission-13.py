class Node:
    def __init__(self, char = None):
        self.char = char
        self.children = set()

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        nodes_hash = {} # char to node

        for word in words:
            for letter in word:
                if letter not in nodes_hash:
                    nodes_hash[letter] = Node(letter)


        for word_index in range(len(words)-1):
            current_word = words[word_index]
            next_word = words[word_index + 1]

            for char_index in range(len(current_word)):
                if char_index == len(next_word):
                    return ""
                if current_word[char_index] != next_word[char_index]:
                    nodes_hash[current_word[char_index]].children.add(next_word[char_index])
                    break
        
        # Lex sort the graph. Each node is in nodes_hash, and childern are the edges of that node. 

        to_return = []
        completed_set = set()

        def dfs(node, current_visited_set):
            if node in completed_set:
                return

            for child_char in node.children:
                child_node = nodes_hash[child_char]
                if child_node in current_visited_set:
                    return False
                if child_node in completed_set:
                    continue
                if dfs(child_node, current_visited_set + [node]) is False:
                    return False
            completed_set.add(node)
            to_return.append(node.char)
        
        for char, node in nodes_hash.items():
            if dfs(node, []) == False:
                return ""

        to_return.reverse()
        return "".join(to_return)