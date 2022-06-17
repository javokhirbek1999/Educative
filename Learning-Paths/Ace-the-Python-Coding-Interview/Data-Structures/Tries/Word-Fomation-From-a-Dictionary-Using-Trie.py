def is_formation_possible(dictionary, word):
    # Write your code here
    
    trie = Trie()

    for w in dictionary:
        trie.insert(w)
    
    words = {}

    find_words(trie.root, words, "")

    j = 0
    c = 0
    w = []
    for i in range(len(word)):

        current = word[j:i+1]
        if current in words:
            w.append(current)
            c += 1
            j = i+1
    
    if "".join(w) == word:
        for k in w:
            if k not in words:
                return False
        return True
    
    return False
