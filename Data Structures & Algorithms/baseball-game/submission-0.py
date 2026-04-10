class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for op in operations:
            match op:
                case "C":
                    sum -= stack.pop()
                case "D":
                    res = stack[-1] * 2
                    stack.append(res)
                    sum += res
                case "+":
                    res = int(stack[-1]) + int(stack[-2])
                    stack.append(res)
                    sum += res
                case _:
                    stack.append(int(op))
                    sum += int(op)                    
        return sum