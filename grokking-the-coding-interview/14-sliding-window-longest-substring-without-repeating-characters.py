def find_longest_substring(input_str):

   # Replace this placeholder return statement with your code
   str_set = set()
   start = 0 
   end = 0
   max_length = -1
   length = 0
   for i  in range(len(input_str)):
      if input_str[i] not in str_set:
         str_set.add(input_str[i])
         length +=1 
         if length > max_length:
            max_length = length
      else:
         while input_str[i] != input_str[start]:
            str_set.remove(input_str[start])
            start +=1
            length -=1 
         start+=1
         





   return max_length