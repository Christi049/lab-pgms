def charCount(file_path):
  numWords = 0
  numSentences= 0
  numUpper = 0
  numLower = 0
  numSpecial = 0
  try:
    with open(file_path,'r',encoding = "utf-8") as file:
      text = file.read()
      words = text.split()
      numWords = len(words)
      
      numSentences = text.count('.')+text.count('!')+text.count('?')

      for i in text:
        if i.isupper():
          numUpper += 1
        elif i.islower():
          numLower += 1
        elif not i.isalnum() and not i.isspace():
          numSpecial += 1
      
      print(f"No of sentences: {numSentences}")
      print(f"No of words: {numWords}")
      print(f"No of lower case: {numLower}")
      print(f"No of upper case: {numUpper}")
      print(f"No of special chars: {numSpecial}")

  except FileNotFoundError:
    print(f"File {file_path} not found")
    
  except Exception as e:
    print(f"An error occured: {e}")

file_path = 'sample_text.txt'
charCount(file_path)

        


