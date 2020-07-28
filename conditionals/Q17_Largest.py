# IGNORE THIS CODE
# This code allows us to check whether your code
# works on a variety of cases.
import sys
num1, num2, num3 = map(int, sys.argv[1:])

# Enter your solution below

if num1 > num2:
  if num1 > num3:
    print(num1)
  else:
    print(num3)
else:
  # num2 >= num1
  if num2 > num3:
    print(num2)
  else:
    print(num3)