def gcd(testVariable1, testVariable2) :
  if testVariable1 == testVariable2:
    return testVariable1
  
  if testVariable1 > testVariable2:
    return gcd(testVariable1-testVariable2, testVariable2)
  else:
    return gcd(testVariable1, testVariable2-testVariable1)
