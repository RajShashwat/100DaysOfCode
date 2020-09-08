def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        if x<=9:
            return True
        if x%10 == 0 and x!= 0:
            return False
        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[-(i+1)]:
                return False
        return True

x = int(input("Enter a Number: "))
result = isPalindrome(x)
print(result)