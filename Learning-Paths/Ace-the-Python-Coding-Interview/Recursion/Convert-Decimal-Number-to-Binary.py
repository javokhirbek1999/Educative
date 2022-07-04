def decimalToBinary(testVariable) :
  if testVariable <= 1:
    return str(testVariable)
  else:
    return decimalToBinary(testVariable//2)+decimalToBinary(testVariable%2)
