import string
alphabet = string.ascii_uppercase
# The code below contains 3 syntax errors. Run the code as-is to generate the first error message.
# Use the message to find and fix the bug. Repeat for the other bugs.

value = int(input("Enter an index value: "))
index = value%26

if value >= len(alphabet):
  print("The letter at index {0} ({1}) is '{2}'.".format(value, index, alphabet[index]))
else:
  print(("The letter at index {0} is '{1}'".format(index, alphabet[index])))



word = input("Enter a school-appropriate word: ")
print("The last letter in '{0}' is '{1}'".format(word, word[len(word)]))

first_num = int(input("Enter a whole number: "))
second_num = input("Enter another whole number: ")

print(f"For {first_num} and {second_num}:")
print("\tSum = {0}".format(first_num + second_num))
print("\tDifference = {0}".format(first_num - second_num))
print("\tProduct = {0}".format(first_num * secnod_num))
if second_num != 0:
  print("\tQuotient = {0}".format(first_num / second_num))
else:
  print("\tQuotient = undefined (cannot divide by 0)")