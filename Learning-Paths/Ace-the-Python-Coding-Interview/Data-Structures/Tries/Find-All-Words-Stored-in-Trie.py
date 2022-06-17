def find_words(root):
    
    words = []
    find(root, words, "")
    
    return words
    

def find(root, words, current):

    if not root:
        return
    
    current += root.char

    if root.is_end_word:
        words.append(current)
    
    for child in root.children:
        find(child, words, current)
    
    current = ""
    return words
