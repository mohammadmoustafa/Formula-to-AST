def postfix(formula):
    output = []
    operands = {'+':1, '*':1, '-':1}
    brackets = ['(', ')']
    stack = []
    index = 0
    while index < len(formula):
        token = formula[index]
        if token.isnumeric():
            output.append(token)
        elif token in operands:
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        index += 1

    while stack != []:
        output.append(stack.pop())

    print(output)


