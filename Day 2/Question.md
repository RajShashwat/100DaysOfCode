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

<br><br>

# Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

```
 I can be placed before V (5) and X (10) to make 4 and 9. 
 X can be placed before L (50) and C (100) to make 40 and 90. 
 C can be placed before D (500) and M (1000) to make 400 and 900.
```

__For an invalid Roman Number the output should be 0__

### Example 1:
``` python
Input: 
"III"
Output: 
3
```
### Example 2:
``` python
Input: 
"IV"
Output: 
4
```
### Example 3:
``` python
Input: 
"IX"
Output: 
9
```
### Example 4:
``` python
Input: 
"LVIIII"
Output: 
0
```
>`Explanation: The numeral for four is not IIII. Character cant be repeated more than 3 time, if it does the Roman Numerical becomes invalid.`
### Example 5:
``` python
Input: 
"MCMXCIV"
Output: 
1994
```
>`Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.`