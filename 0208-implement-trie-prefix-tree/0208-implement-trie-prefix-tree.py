class TreeNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            last_node = node
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TreeNode()
                node = node.children[char]
        node.is_word = True
                
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            last_node = node
            if char in node.children:
                node = node.children[char]
            else:
                return False
            
        if node.is_word == True:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            last_node = node
            if char in node.children:
                node = node.children[char]
            else:
                return False
        
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)