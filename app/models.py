# word = input("Enter a school-appropriate word: ")

# print("The last letter in '{0}' is '{1}'".format(word, word[-1]))

# first_num = int(input("Enter a whole number: "))
# second_num = int(input("Enter another whole number: "))

# print(f"For {first_num} and {second_num}:")
# print("\tSum = {0}".format(first_num + second_num))
# print("\tDifference = {0}".format(first_num - second_num))
# print("\tProduct = {0}".format(first_num * second_num))
# if second_num != 0:
#   print("\tQuotient = {0}".format(first_num / second_num))
# else:
#   print("\tQuotient = undefined (cannot divide by 0)")



# This program should convert points earned to a percent. Find and fix the logic errors.
points_earned = 23.4
points_possible = 25

percentage = points_earned/points_possible * 100
print(f"The student earned {points_earned} points out of {points_possible}, or {percentage}%.")

# Here are some test cases:
# Earning 8 out of 10 possible points = 80.0%. 
# 11 of of 15 is 73.33333333333333%.
# 23.4 out of 25 93.6%.


# Fix the logic errors in the code to correctly report a student's letter grade!



score_percent = 93.5

if score_percent >= 90:
  letter_grade = 'O'
elif score_percent >= 70:
  letter_grade = 'A'
elif score_percent >= 80:
  letter_grade = 'E'
elif score_percent <= 60:
  letter_grade = 'P'
else:
  letter_grade = 'T'

output = "The student's score of {0}% is a '{1}'."
print(output.format(score_percent, letter_grade))