def postfix(formula):
    '''(str) -> list of str
    Given a formula, return the same formula in a list. The formula
    has been re-arranged in Reverse Polish Notation (postfix notation)
    '''
    # use a queue and a stack to represent the output and operators
    output = []
    # declare operators with precedence
    # notes for later, figure out how to build a tree with this/compact
    # the RPN so effeciently organize children
    operands = {'+':0, '*':0, '-':1}
    brackets = ['(', ')']
    stack = []
    index = 0
    while index < len(formula):
        token = formula[index]
        if token in operands:
            while (stack[-1] in operands) and (operands[stack[-1]] > operands[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            output.append(token)
        index += 1

    while stack != []:
        output.append(stack.pop())

    return output


