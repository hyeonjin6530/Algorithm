class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # 해결법 1 : 모든 경우를 나눠서 체크 해보기 (겹치는 부분이 많아서 뭔가 비효율적으로 보임)
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True

        