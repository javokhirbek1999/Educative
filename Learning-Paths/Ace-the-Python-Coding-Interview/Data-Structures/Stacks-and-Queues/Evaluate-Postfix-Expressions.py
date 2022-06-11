from Stack import MyStack

def evaluate_post_fix(exp):

    operators = []
    digits = []

    for i in exp:
        if i in {'+':'+', '-':'-', '*':'*', '/':'/'}:
            operators.append(i)
        
        elif i in {i:i for i in "09876544321"}:
            digits.append(i)
    
    print(operators)
    print(digits)

    exp = ""
    if len(operators)>1 and len(digits) >= 3:
        exp = str(digits.pop(1)) + str(operators.pop(0)) + str(digits.pop(1))
        exp = str(digits.pop(0)) + str(operators.pop(0)) + exp
    
    while digits and operators:
        exp += str(operators.pop(0))+str(digits.pop(0))

    return eval(exp)
