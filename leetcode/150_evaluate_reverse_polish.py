def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    ops = {"+","-","*","/"}
    for i in tokens:
        if i in ops:
            b = stack.pop()
            a = stack.pop()
            if i == "+":
                stack.append(a+b)
            elif i == "-":
                stack.append(a-b)
            elif i == "*":
                stack.append(a*b)
            elif i == "/":
                stack.append(int(float(a)/float(b)))
        else:
            stack.append(int(i))
    return stack[-1]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))