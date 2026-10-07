class Node:
    def __init__(self, email = "", name = "", parent = None):
        self.email = email
        self.name = name
        self.parent = parent if parent is not None else self
        self.rank = 0

    def root(self):
        if self.parent != self:
            self.parent = self.parent.root()
            return self.parent
        else:
            return self
    
    def join(self, node_2):
        root_1 = self.root()
        root_2 = node_2.root()
        if root_1 == root_2:
            return

        if root_1.rank > root_2.rank:
            root_2.parent = root_1
        elif root_2.rank > root_1.rank:
            root_1.parent = root_2
        else:
            root_2.parent = root_1
            root_1.rank += 1
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Needs hash table for emails -> nodes
        emails_to_nodes = {}
        for account in accounts:
            current_name = account[0]
            first_node = None
            for email in account[1:]:
                if email not in emails_to_nodes:
                    emails_to_nodes[email] = Node(email = email, name = current_name)
                if first_node is None:
                    first_node = emails_to_nodes[email]
                else:
                    emails_to_nodes[email].join(first_node)
        
        all_roots = {} # root_node -> [Name, list of emails]
        for email in emails_to_nodes.keys():
            r = emails_to_nodes[email].root()
            if r in all_roots:
                all_roots[r].append(email)
            else:
                all_roots[r] = [r.name, email]
                
        to_return = []

        for root in all_roots.keys():
            to_return.append([all_roots[root][0]] + sorted(all_roots[root][1:]))

        return to_return