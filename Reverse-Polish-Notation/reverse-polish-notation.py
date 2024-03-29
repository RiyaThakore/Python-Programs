class Solution:
  def isnum(s):
    try:
      int(s)
      return True
    except:
      return False
  
  def reversePolishNotation(tokens):
    for t in tokens:
      if isnum(t):
        stack.append(t)
      else:
        a=int(stack.pop())
        b=int(stack.pop())
        if t == '+':
          c = b+a
        elif t == '-':
          c = b-a
        elif t == '*':
          c = b*a
        elif t == '/':
          c = int(b/a)
        stack.append(str(c))
  return(stack[-1])
  
  
