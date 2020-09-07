def twoSum(nums, target: int) :
    hashMap = {}
    for index,num in enumerate(nums):
        val = target-num
        if val in hashMap:
            return [hashMap[val], index]
        else:
            hashMap[num] = index        
    return []


List = list(map(int,input("Enter the array: ").strip().split()))
target = int(input("Enter the target Number: "))

result = twoSum(List,target)

print("index of the numbers are: ", result)