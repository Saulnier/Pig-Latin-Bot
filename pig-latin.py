pyg = 'ay'

original = raw_input('Enter a word:') #WORD

if len(original) > 0 and original.isalpha():
  word = original.lower() #word
  first = word[0] #w
  new_word = word + first + pyg #wordway
  new_word = new_word[1:len(new_word)] #ordway
  print new_word
else:
    print 'empty'