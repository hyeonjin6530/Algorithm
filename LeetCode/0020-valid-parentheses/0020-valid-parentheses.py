class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # 해결법 1 : 모든 경우를 나눠서 체크 해보기 (겹치는 부분이 많아서 뭔가 비효율적으로 보임)
        # for i in s:
        #     if i == '(' or i == '{' or i == '[':
        #         stack.append(i)
        #     elif i == ')':
        #         if len(stack) > 0 and stack[-1] == '(':
        #             stack.pop()
        #         else:
        #             return False
        #     elif i == '}':
        #         if len(stack) > 0 and stack[-1] == '{':
        #             stack.pop()
        #         else:
        #             return False
        #     elif i == ']':
        #         if len(stack) > 0 and stack[-1] == '[':
        #             stack.pop()
        #         else:
        #             return False

        # 해결법 2 : 딕셔너리를 이용한 방법
        dict = { ')' : '(', '}' : '{', ']' : '['}

        for i in s:
            # 여는 괄호
            if i in dict.values():
                stack.append(i)
            
            # 닫는 괄호
            else:
                if not stack or stack[-1] != dict[i]:
                    return False
                stack.pop()
        
        if len(stack) > 0:
            return False
        
        return True

        