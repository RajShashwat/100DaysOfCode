# Stack

Design a stack that supports the following operation

- ___push(x) -- Push element x onto stack.___
- ___pop() -- Removes the element on top of the stack.___
- ___top() -- Get the top element.___
- ___is_empty() -- Checks if stack is empty or not___
- ___get_stack() -- Get all the elements of stack___
- ___length() -- Get the length of the stack___

<br><br>

# Integer to Binary

Given a positive integer number `num` has to be converted into binary. The output will be a string.

### Example 1
``` python
Input: 
10
Output:
1010
```
### Example 1
``` python
Input: 
246
Output:
11110110
```
### Example 1
``` python
Input: 
131
Output:
10000011
```

<br><br>

 




# MinStack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- ___push(x) -- Push element x onto stack.___
- ___pop() -- Removes the element on top of the stack.___
- ___top() -- Get the top element.___
- ___getMin() -- Retrieve the minimum element in the stack.___
 

### Example 1:
``` python
Output
1
7
1
5
```

>`Explanation`
>
> `obj = MinStack()`
>
>`obj.push(5)`
>
>`obj.push(4)`
>
>`obj.pop()`
>
>`obj.push(1)`
>
>`print("Top: ",obj.top())`
>
>`obj.push(7)`
>
>`print("Top: ",obj.top())`
>
>`obj.pop()`
>
>`print("Top: ",obj.top())`
>
>`obj.pop()`
>
>`print("MIN: ",obj.getMin())`
 

__Constraints:__

Methods pop, top and getMin operations will always be called on non-empty stacks.

<br><br>

# Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
 

### Example 1:
``` python
Input: 
s = "()"
Output: 
True
```
Example 2:
``` python
Input: 
s = "()[]{}"
Output: 
True
```
### Example 3:
``` python
Input: 
s = "(]"
Output: 
False
```
### Example 4:
``` python
Input: 
s = "([)]"
Output: 
False
```
### Example 5:
``` python
Input: 
s = "{[]}"
Output: 
True
```
 

Constraints:

- `1 <= s.length <= 104`
- `s` consists of parentheses only '()[]{}'.

