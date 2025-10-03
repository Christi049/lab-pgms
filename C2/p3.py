"""Count the number of vowels, consonants, words and question marks in a given string"""

s = input("Enter a string:")

vowels = 0
consot = 0
q = 0

for i in s:
  if i.lower() in "aeiou":
    vowels += 1
  elif i.isalpha():
    consot +=  1
  elif i == '?':
    q +=1 

words = len(s.split())

print(f"No of vowels: {vowels}")
print(f"No of consonants: {consot}")
print(f"No of ?: {q}")
print(f"No of words: {words}")
