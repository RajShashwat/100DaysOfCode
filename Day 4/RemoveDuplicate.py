def removeDuplicates(nums: list) -> int:
        i = len(nums)
        while i > 1:
            i -= 1
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)

nums = list(map(int,input("Enter the array: ").strip().split()))
len = removeDuplicates(nums)
print("length of array: ", len)
print("Array Elements are: ", end="")
for i in nums:
    print(i, end=" ")
