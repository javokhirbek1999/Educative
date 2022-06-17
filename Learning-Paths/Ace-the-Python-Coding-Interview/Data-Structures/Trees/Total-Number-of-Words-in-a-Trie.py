def total_words(root):
    if not root:
        return 0
    
    cnt = 0

    for child in root.children:

        if child and child.is_end_word:
            cnt += 1
        
        cnt += total_words(child)

    return cnt
