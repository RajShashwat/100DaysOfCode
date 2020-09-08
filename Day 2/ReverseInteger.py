def reverse(x: int) -> int:
        sign = -1 if x < 0 else 1
        reverse, x = 0, abs(x)
        while x != 0:
            x, num = divmod(x,10)
            reverse = reverse * 10 + num 
        return sign * reverse if -2 ** 31 <= reverse <= 2 ** 31 - 1 else 0

x = int(input("Enter a number: "))
reverse = reverse(x)
print("Reverse of the Number is: ",reverse)