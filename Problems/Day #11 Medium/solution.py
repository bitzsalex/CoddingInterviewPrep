# simple list comperhension solution
possible_words = ['dog', 'deer', 'deal']
query = 'de'

print([word for word in possible_words if word.startswith(query)])


# Trie DataStructure
class TrieTree:
    def __init__(self) -> None:
        self.children_nodes = {}
        self.end_of_word = False
        
    def add_word(self, word) -> None:
        # start from the current node
        current_node = self
        for character in word:
            if character not in current_node.children_nodes:
                current_node.children_nodes[character] = TrieTree()
                
            current_node = current_node.children_nodes[character]
        current_node.end_of_word = True
        
    def auto_complete(self, prefix:str) -> list:
        auto_complete_list = []
        current_node = self
        
        for character in prefix:
            if character not in current_node.children_nodes:
                return auto_complete_list
            
            current_node = current_node.children_nodes[character]
            
        self.get_all_words(current_node, auto_complete_list, prefix)
        return auto_complete_list
    
    def get_all_words(self, current_node:object, words_storage:list, prefix:str):
        if not current_node: return
        
        if current_node.end_of_word:
            words_storage.append(prefix)
            
        for character in current_node.children_nodes:
            self.get_all_words(current_node.children_nodes[character], words_storage, prefix + character)


words = ['den', 'dear', 'deal', 'done', 'do', 'doing', 'disco']

root = TrieTree()
for word in words:
    root.add_word(word)
    
root.auto_complete('do')