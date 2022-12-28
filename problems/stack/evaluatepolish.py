class Solution:
    ops = ["+", "/", "*", "-"]

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in self.ops:
                stack.append(int(t))
            elif t in self.ops:
                i2 = stack.pop()
                i1 = stack.pop()

                stack.append(
                    self.calc(i1, i2, t)
                )

        return stack.pop()

    def evalRPNRecursive(self, tokens: List[str]) -> int:
        t = tokens.pop()

        if t in self.ops:
            i2 = self.evalRPNRecursive(tokens)
            i1 = self.evalRPNRecursive(tokens)

            return self.calc(i1, i2, t)
        
        return int(t)
    
    def calc(self, i1, i2, op):
        if op == "+":
            return i1 + i2
        if op == "/":
            return int(i1 / i2)
        if op == "*":
            return i1 * i2
        if op == "-":
            return i1 - i2
        return None