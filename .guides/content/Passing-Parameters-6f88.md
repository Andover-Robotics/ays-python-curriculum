----------

|||guidance

Time estimation: 13 minutes.

|||

## Parameters

Parameters are the inputs that a function works with. (The name of a parameter is defined inside the parentheses in a function definition, while its value is passed in when the function is called.) Just as the plus sign on a calculator yields a different result based on the numbers you input, functions that make good use of parameters are capable of tailoring the result to your input. In the example below, the function adds the parameters together. If I write 3 and 4 in my function call, the function will print 7, but if I write 5 and 6, it will print 11. If you need more than one parameter, as in the example, they will be separated by commas within the parentheses.

```python
def addition(num1, num2):
    """Prints the sum of two numbers"""
    print(num1 + num2)

addition(3, 4)
```

{try it}(python3 code/functions/parameters.py 1)

|||challenge
## Your Turn!
* Modify the function to add three numbers. (Hint: you'll need another parameter!)

{try it}(python3 code/functions/parameters.py 2)

|||


## Parameters as Variables

Parameters are a specific type of variable. They are declared in a certain order in the function definition, and their values are determined by the inputs in that order in the function call. Because of this, the order of parameters is important. The first parameter in the function call will be the first parameter in the definition, the second parameter from the function call will be the second parameter in the definition, etc.

```python
def add_sub(num1, num2, num3):
    """add_sub does the following:
    Add the first two parameters
    Subtract the third paramter
    Print the result"""
    print(num1 + num2 - num3)

add_sub(5, 10, 15)
```

{try it}(python3 code/functions/parameters.py 3)

|||challenge
## Your Turn!
What if you wanted to add 5 and 15 and subtract 10? What would you have to change in your function call?

{try it}(python3 code/functions/parameters.py 4)
|||



