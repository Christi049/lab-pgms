"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: 
a. Open brackets must be closed by the same type of brackets.,
b. Open brackets must be closed in the correct order. 
c. Every close bracket has a corresponding open bracket of the same type.
"""
def isvalid(s):
  bracket_map = {')':'(', ']':'[', '}':'{'}
  stack = []
  for i in s:
    if i in bracket_map.values():
      stack.append(i)
    elif i in bracket_map:
      if not stack or stack.pop() != bracket_map[i]:
        return False
    else:
      return False
  return not stack

str = input("Enter a string of brackets:")
if isvalid(str):
  print("is valid")
else:
  print("Not valid")

