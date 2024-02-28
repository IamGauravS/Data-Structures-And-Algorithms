def is_palindrome(s):
  
  # Replace this placeholder return statement with your code
  start= 0
  end = len(s) -1 
  while end>start:
    if s[start] != s[end]:
      return False 
    start +=1
    end -= 1

  return True