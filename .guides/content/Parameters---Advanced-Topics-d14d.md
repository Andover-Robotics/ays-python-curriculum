----------

## Optional Parameters

Python allows you to create functions with optional parameters. They are considered to be optional because when you call the function, you can either include the parameter or choose not to However, the function declaration will name this parameter and give it a default value.

```python
def add_if_true(num1, num2, bool = True):
    """Prints the sum of two numbers
    if the variable bool is true"""
    if bool:
        print(num1 + num2)
    else:
        print("No addition, bool is false")

add_if_true(5, 7)
add_if_true(5, 7, False)
```

{try it}(python3 code/functions/advanced-parameters.py 1)

|||challenge
## Your Turn!
- Write a function that takes in a student's name and age as well as an optional parameter of their pet's name, and then prints them out. If the pet's name is not included in the call, print out "No Pet" Try different calls to your function and see if it works as desired!

|||

{try it}(python3 code/functions/advanced-parameters.py 2)

## Variable Parameter Lists

It is possible to declare a function with a list of variables of an undetermined length. The function below will find the sum for any number passed as a parameter. There can be two parameters or twenty, but it is not necessary to write out each parameter. Instead, you can create a list of parameters that has unknown length. Use a `*` before the name you want to assign the list of parameters. 

Example below:
```python
def calc_sum(*nums):
    """Calculate the sum of all of the parameters"""
    total = 0
    for num in nums:
        total += num
    print(total)
    
calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

{try it}(python3 code/functions/advanced-parameters.py 3)

|||challenge
## Your Turn!
- Write a function that takes in an unknown number of strings and concatenates all of them together.

|||

{try it}(python3 code/functions/advanced-parameters.py 4)

{Check It!|assessment}(fill-in-the-blanks-3645586010)
