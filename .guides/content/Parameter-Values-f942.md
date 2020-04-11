----------

## Named Parameters

Typically, parameter values are assigned based on their position in the function call. However, Python allows you to specify which parameter is which if you want them in a different order. This technique also helps readability if you are dealing with complex functions that take in lots of hard-to-remember parameters.

```python
def subtract(num1, num2):
    # Subtracts the second parameter from the first
    print(num1 - num2)
    
subtract(5, 2) # returns 5 - 2 = 3
subtract(2, 5) # returns 2 - 5 = -3
subtract(num2=2, num1=5) # can you predict what this returns?
```

{try it}(python3 code/functions/parameter-values.py 1)

## Parameter Values

If parameters can be thought of as variables, then you can pass in any type of variable as a parameter: ints, floats, strings, boolean, lists, etc.

```python
def parameter_types(param1, param2, param3, param4):
    """Takes four parameters
    Print the type of each element"""
    print("The type of {} is {}".format(param1, type(param1)))
    print("The type of {} is {}".format(param2, type(param2)))
    print("The type of {} is {}".format(param3, type(param3)))
    print("The type of {} is {}".format(param4, type(param4)))
        
parameter_types(1, 5.9, "Beatles", False)
```

{try it}(python3 code/functions/parameter-values.py 2)

|||challenge
## Your Turn!
- Write a function that passes in a list as a parameter and prints out each item. Test the outputs you get when you input lists with different types of elements.

|||

{try it}(python3 code/functions/parameter-values.py 4)

{Check It!|assessment}(multiple-choice-1415019255)
