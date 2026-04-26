import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                a,b = stack.pop(), stack.pop()
                result = operators[char](b,a)
                stack.append(int(result))
        return stack[-1]         