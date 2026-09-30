class Node:
    def __init__(self, name = "", email = "", parent = None, rank = 0):
        self.name = name
        self.email = email
        if parent is not None:
            self.parent = parent
        else:
            self.parent = self
        self.rank = rank
        
    def root(self):
        while self.parent != self:
            temp = self.parent
            self.parent = self.parent.parent
            self = temp
        return self

    def union(self, node):
        self_root = self.root()
        node_root = node.root()
        if self_root == node_root:
            return 
        if self_root.rank > node_root.rank:
            node_root.parent = self_root
        elif self_root.rank < node_root.rank:
            self_root.parent = node_root
        else: 
            node_root.parent = self_root
            self_root.rank += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        emails_to_nodes = {}
        for account in accounts:
            first = None
            name = account[0]
            for email in account[1:]:
                if email not in emails_to_nodes:
                    new_node = Node(name = name, email = email)
                    emails_to_nodes[email] = new_node
                if first is None:
                    first = emails_to_nodes[email]
                else:
                    first.union(emails_to_nodes[email])
        roots_to_emails = {} 
        for email, node in emails_to_nodes.items():
            root = node.root()
            if root in roots_to_emails:
                roots_to_emails[node.root()].append(email)
            else:
                roots_to_emails[node.root()] = [email]
            
        to_return = []
        for node, email_list in roots_to_emails.items():
            to_return.append([node.name] + sorted(email_list))

        return to_return