def isValid(s: str) -> bool:
        stack = []
        mapping = { 
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }
        for i in s:
            if i in mapping:
                top_element = stack.pop() if stack else ""
                if mapping[i] != top_element:
                    return False
            else:
                stack.append(i)
        return not stack

s = input("Enter a Parentheses : ")
result = isValid(s)
print(result)