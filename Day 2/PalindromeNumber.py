def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        if x<=9:
            return True
        if x%10 == 0 and x!= 0:
            return False
        rev = 0
        cpy = x
        while cpy != 0:
            cpy, num = divmod (cpy, 10)
            rev = rev * 10 + num
        return True if rev == x else False

x = int(input("Enter a Number: "))
result = isPalindrome(x)
print(result)