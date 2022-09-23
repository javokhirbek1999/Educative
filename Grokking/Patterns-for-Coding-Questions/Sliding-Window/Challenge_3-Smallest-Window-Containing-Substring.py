"""
Time: O(n + m)
Space: O(m)

"""

def find_substring(str1, pattern):

  charFreq = {}

  for char in pattern:
    if char not in charFreq:
      charFreq[char] = 0
    charFreq[char] += 1
  
  
  windowStart, matched, substringStart = 0, 0, 0

  minLen = len(str1) + 1
  
  for windowEnd in range(len(str1)):

    rightChar = str1[windowEnd]

    if rightChar in charFreq:
      charFreq[rightChar] -= 1

      if charFreq[rightChar] >= 0:
        matched += 1
    

    while matched == len(pattern):

      if minLen > windowEnd - windowStart + 1:
        minLen = windowEnd - windowStart + 1
        substringStart = windowStart
      
      leftChar = str1[windowStart]

      windowStart += 1

      if leftChar in charFreq:
        if charFreq[leftChar] == 0:
          matched -= 1
        
        charFreq[leftChar] += 1
    
  if minLen > len(str1):
    return ""
  return str1[substringStart:substringStart + minLen]
  
