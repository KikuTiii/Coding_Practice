class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in operations:
                right = stack.pop()
                left = stack.pop()

                result = operations[token](left, right)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]

solution = Solution()

assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert solution.evalRPN(["3", "4", "+"]) == 7
assert solution.evalRPN(["5", "2", "-"]) == 3
assert solution.evalRPN(["2", "3", "*"]) == 6

print("Todos os testes passaram!")