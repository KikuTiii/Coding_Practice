class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
                if stack and char == stack[-1]:
                     stack.pop()
                else:
                     stack.append(char)
            
        return "".join(stack)


solution = Solution()

assert solution.removeDuplicates("abbaca") == "ca"
assert solution.removeDuplicates("azxxzy") == "ay"
assert solution.removeDuplicates("abc") == "abc"
assert solution.removeDuplicates("aaaa") == ""
assert solution.removeDuplicates("a") == "a"
assert solution.removeDuplicates("") == ""

print("Todos os testes passaram!")