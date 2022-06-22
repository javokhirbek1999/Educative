def search_next_letter(letters, key):

  n = len(letters)

  start, end = 0, n-1

  while start <= end:

    mid = start + (end - start) // 2

    if key < letters[mid]:
      end = mid - 1
    else:
      start = mid + 1
  
  return letters[start % n]
