#imported the Stack.py 
from Stack import Stack


def intToBinary(num: int) -> str :
    stack = Stack()

    while num > 0:
        remender = num % 2
        stack.push(remender)
        num = num // 2

    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
        print(stack)
    return binary

num = int(input("Enter a Number: "))
if num < 0:
    print("Enter a Positive Number")
    quit()
result = intToBinary(num)
print("Binary: ",result)
