"""Define a tuple containing the names of different fruits. Write a Python program that prompts the user to enter a fruit name. If the entered fruit exists in the tuple, display a message confirming its presence; otherwise, display a message indicating its absence.
"""

fruits = ("apple","mango","banana",)
user_fruit = input("Enter a fruit:")
if user_fruit.lower() in fruits:
  print("Fruit present in tuple")
else:
  print("not present in tuple")