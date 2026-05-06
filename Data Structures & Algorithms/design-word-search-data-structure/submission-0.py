class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.endofWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        curr = self.root

        if self.search(word):
            return

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.endofWord = True

    def search(self, word: str) -> bool:

        
        def dfs(j:int, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.endofWord

        return dfs(0, self.root)

        


        
        
        
