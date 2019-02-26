import copy as cp

def compare(a, b):
  if len(a) > len(b):
    return a
  else:
    return b

def isSubsequencePalindrome(s):
    n=len(s)
    isPalindrome=True
    j =n
    for i in range(n+1):
        j=j-1
        if s[i]==s[j]:
            isPalindrome = True
            if ((n-1)//2)== j:
              break
        else:
            isPalindrome=False
            break
    return isPalindrome            
   
def longestPalSubsB(s):
  word_list =[]
  for i in s:
    word_list.append(i)
  if len(word_list)<3:
    print('TOO SHORT! Cannot be a Palindrome! Try word with atleast 3 characters!')
    return
  if isSubsequencePalindrome(s) == True:
    return s
  else:
    flag2 =True
    flag3 =True
    flag4 =True
    flag5 =True    
    
    next0 = 0
    next1 = 0
    
    front = cp.deepcopy(word_list)
    end = cp.deepcopy(word_list)
    frontNend = cp.deepcopy(word_list)
    endNfront = cp.deepcopy(word_list)
    length = len(word_list)

# Takes one at a time on the left and then all from the right        
    for i in range(len(word_list)):
      frontNend = cp.deepcopy(front)
      for j in range(len(front)):
          del frontNend[-1]
          if isSubsequencePalindrome(frontNend)==True:
            next0 = 1
            flag2 = True
            flag3 = True
            break
          if len(frontNend)==3:
            flag2 = False
            flag3 =False
            break
      if next0 == 1:
        break
      else:
        del front[0]
        if isSubsequencePalindrome(front)==True:
          flag2 = True
          flag3 = False
          break
        if len(front)==3:
          flag2 = False
          flag3 = False
          break 
#Take one at a time on the right(end) and then all from the left(front)    
    for i in range(len(word_list)):
      endNfront = cp.deepcopy(end)
      for j in range(len(end)):
          del endNfront[0]
          if isSubsequencePalindrome(endNfront)==True:
            next1 = 1
            flag4 = True
            flag5 = True
            break 
          if len(endNfront)==3:
            flag4 = False
            flag5 = False
            break
      if next1 == 1:
        break
      else: 
        del end[-1]
        if isSubsequencePalindrome(end)==True:
          flag4 = True
          flag5 = False
          break
        if len(end)==3:
          flag4 = False
          flag5 = False
          break      
    
#Getting out of loop and catching all the outcomes in the container:    
    container = []
    if flag2 == flag3 == flag4 == flag5 == False:
      print('No Palindrome in the word! Try another word!')
      return
    else:
      if flag2 == True and flag3 == False:
        container.append(str(front))
      if flag2 == True and flag3 == True:
        container.append(str(frontNend))
      if flag4 == True and flag5 == False:
        container.append(str(end))
      if flag4 == True and flag5 == True:
        container.append(str(endNfront))    
      j=0
      for i in range(len(container)):
        j =+ 1  
      if j == 1:
        return container[0]
      if j == 2 and (len(container[0]) == len(container[1])):
        return container[0] + ' ' + container[1]
      else:
        return compare(container[0], container[1])

word = raw_input('Enter a word: ')
catch = longestPalSubsB(word)
if catch == None:
  print('NO Palindrome!')
else:
  print('The longest palindrome/s in the given word: ')          
  print(catch)       


'''
print(longestPalSubsB("aceexcivicgrfdds"))
print(longestPalSubsB("civicgrfdds"))
print(longestPalSubsB("aceexcivic"))
print(longestPalSubsB("civic"))
print(longestPalSubsB("123abba1"))
print(longestPalSubsB("abba1"))
print(longestPalSubsB("123abba"))
print(longestPalSubsB("12345"))
print(longestPalSubsB(""))      
                                
  '''                                  
            