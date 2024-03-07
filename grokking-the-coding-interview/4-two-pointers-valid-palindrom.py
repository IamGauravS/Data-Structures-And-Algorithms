def check_palindrome(s):
  start = 0
  end = len(s) -1
  while start < end:
    if s[start] != s[end]:
      return False
    start +=1
    end -=1 
  return True 

def is_palindrome(s):
  
  # Replace this placeholder return statement with your code
  start = 0
  end = len(s) -1
  while start < end:
    if s[start] == s[end]:
      start +=1
      end -=1
    else:
      return check_palindrome(s[:start] + s[start+1:]) or check_palindrome(s[:end]+ s[end+1:])


  
  return True