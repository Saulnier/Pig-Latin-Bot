pyg = ' fourwinds'

original = input('Enter a word:') #WORD

if len(original) > 0 and original.isalpha():  # adding alpha char
  word = original.lower() #word
  first = word[0] #w
  new_word = word  + pyg #wordway + first
  #new_word = new_word[1:len(new_word)] #ordway
  print (new_word)
else:
    print ('please type one word')