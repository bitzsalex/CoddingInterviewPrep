from typing import List

# can be implemented using trie tree, to store the possible words

def get_the_base_words(words:List[str], combinations:str) -> List:
    base_words = []
    
    # check if the combinations contain any of the word
    if any([word for word in words if combinations.startswith(word)]):
        # loop until the combinations string is empty
        while combinations:
            # pick the first character from the current combinations string
            first_char = combinations[0]
            # filter the words from the list those start with the picked letter
            filtered_words = filter(lambda word: word.startswith(first_char), words)
            
            # loop over the picked words
            for word in filtered_words:
                # check if the combinations string start with that letter
                if combinations.startswith(word):
                    # add the word to the base_words list
                    base_words.append(word)
                    # update the combinations string
                    combinations = combinations[len(word):]
                    break
                
    return base_words

words = ['quick', 'brown', 'the', 'fox']
get_the_base_words(words, "thequickbrownfox")
get_the_base_words(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond")
