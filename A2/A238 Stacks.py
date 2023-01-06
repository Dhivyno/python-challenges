def postfix_eval(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            stack.append(result)
    return stack[0]
  
expression = "1 2 + 3 *"
result = postfix_eval(expression)
print(result)
