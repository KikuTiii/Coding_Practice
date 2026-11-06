class Solution:
    def process(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

solution = Solution()

assert solution.process("abc##d") == "ad"
assert solution.process("a##b") == "b"
assert solution.process("abc") == "abc"
assert solution.process("###") == ""
assert solution.process("ab#c") == "ac"
assert solution.process("a#") == ""
assert solution.process("") == ""

print("Todos os testes passaram!")