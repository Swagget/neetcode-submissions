class Node:
    def __init__(self, val = "", term = False, parent = None):
        self.val = val
        self.term = term
        self.children = {}
        self.parent = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            current = root
            for letter in word:
                if letter in current.children:
                    current = current.children[letter]
                else:
                    current.children[letter] = Node(val = letter, parent = current)
                    current = current.children[letter]
            current.term = word
        
        def search(node, coordinates, board):
            to_return = []
            if board[coordinates[0]][coordinates[1]] in node.children:
                ch = board[coordinates[0]][coordinates[1]]
                if node.children[board[coordinates[0]][coordinates[1]]].term:
                    to_return.append(node.children[board[coordinates[0]][coordinates[1]]].term)
                    node.children[board[coordinates[0]][coordinates[1]]].term = False
                board[coordinates[0]][coordinates[1]] = "#"
                for d_i, d_j in [(-1,0), (0,-1), (1,0), (0,1)]:
                    if coordinates[0] + d_i >= 0 and coordinates[1] + d_j >= 0 and coordinates[0] + d_i < len(board) and coordinates[1] + d_j < len(board[0]):
                        to_return.extend(search(node = node.children[ch],
                                                        coordinates = [coordinates[0] + d_i, coordinates[1] + d_j],
                                                        board = board))
                board[coordinates[0]][coordinates[1]] = ch
            else:
                return []
            return to_return

        answer = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                answer.extend(search(root, [i,j], board))

        return answer