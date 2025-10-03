""" Read a number in decimal and convert it into different bases."""
num = int(input("Enter a decimal:"))

binary = bin(num)
octal = oct(num)
hexadecimal = hex(num)

print(f"{binary[2:]}")
print(f"{octal[2:]}")
print(f"{hexadecimal[2:]}")
