"""
N = # of characters
M = # of words
Len = size of each word

Time: O(N * M * Len)
"""

def find_word_concatenation(str1, words):
  
  if not words or not words[0]:
    return []
 
  result_indices = []
  
  wordFreq = {}

  for word in words:
    if word not in wordFreq:
      wordFreq[word] = 0
    
    wordFreq[word] += 1

  word_count = len(words)
  word_length = len(words[0])
  
  for i in range((len(str1) - word_count * word_length) + 1):

    word_seen = {}

    for j in range(0, word_count):
      start_word_index = i + j * word_length

      word = str1[start_word_index:start_word_index + word_length]

      if word not in word_seen:
        word_seen[word] = 0
      word_seen[word] += 1
      
      if word_seen[word] > wordFreq.get(word, 0):
        break
      
      if j + 1 == word_count:
        result_indices.append(i)

  return result_indices
