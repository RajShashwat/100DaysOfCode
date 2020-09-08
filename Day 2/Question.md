# Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

### Example 1:
``` python
Input: 
123
Output: 
321
```
### Example 2:
``` python
Input: 
-123
Output: 
-321
```
### Example 3:
``` python

Input: 
120
Output: 
21
```
__Note:__

Assume we are dealing with an environment which could only store integers within the __32-bit signed integer__ range: 
**[−2<sup>31</sup>,  2<sup>31</sup> − 1]** 
. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

<br><br>

# Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

### Example 1:
``` python
Input: 
121
Output: 
True
```
### Example 2:
``` python
Input: 
-121
Output: 
False
```
>`Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.`
### Example 3:
``` python
Input: 
10
Output: 
False
```
>`Explanation: Reads 01 from right to left. Therefore it is not a palindrome.`

__Follow up:__

__```Coud you solve it without converting the integer to a string?```__