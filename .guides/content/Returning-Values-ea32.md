----------

## The Return Keyword

So far, all the functions you have defined yourself have just printed things out. If you set a variable equal to a call of one of your functions, there would be nothing inside the variable. But what if you wanted to define a function such that the result it produces wasn't just printed, but saved so that it could be placed into any variable you want, and more? 

Think of the `len` function. This function returns the length (an int) of either a string or list. If you were to say: x = len(my_list), x would be an integer representing the length of the list you used as a parameter. So the return value of `len` is of type int. `len` does not print anything to the screen, it just returns a number. (Functions that don't return anything do exist -- they are known as NoneType, or void, functions.)

Example of a function that uses return:

```python
def add_five(num):
    """Add five to the parameter num"""
    return(num + 5)
  
add_five(10)
```

{try it}(python3 code/functions/returning-values.py 1)

The program no longer prints anything to the screen. That is because the function only adds 5 to whatever parameter is passed to the function, and back the function returns this value to the program. Explicitly tell Python to print the return value of the function.

```python
def add_five(num):
    """Add five to the parameter num and RETURN the function"""
    return(num + 5)
  
new_number = add_five(10)
print(new_number)
```

{try it}(python3 code/functions/returning-values.py 2)

|||challenge
## Your Turn!
- Can you reduce the two lines of code after the function definition into one line?

|||

{try it}(python3 code/functions/returning-values.py 3)

<details><summary>**What is the return value for functions that use `print`?**</summary>If every function in Python has a return value, what is the return value for functions that use `print`? The keyword `return` is not used, so you cannot see if it returns a string, a float, a list, etc. Functions that use `print` instead of `return` have a special return value called `NoneType`. Enter the code below to see the return type of the print statement as compared to the return value of the `len` function.<img src=".guides/images/none-type.png" /></details>

## Returning Values

Functions can return any value in Python — ints, floats, strings, lists, etc.

```python
def return_int(num1, num2):
    """Return the floor division of num1 divided by num2"""
    return(num1 // num2)
  
def return_float(num1, num2):
    """Return num1 divided by num2"""
    return(num1 / num2)
  
def return_string(string):
    """Return the value of string appended to 'Hello` """
    return("Hello".append(string))
  
print(return_int(10, 3))
print(return_float(10, 3))
print(return_string(" friend"))
```

{try it}(python3 code/functions/returning-values.py 4)

|||challenge
## Your Turn!
Can you return a list? Write a function that will take in a list of numbers as a parameter, multiply each value in the list by 5, and then return the resulting list. 
<details><summary>**Solution**</summary>The code below takes a list of numbers as a parameter. Each element of the list is multiplied by 5, and the new list is returned. <img src=".guides/images/return-list.png" /></details>

|||

{try it}(python3 code/path/to_file.py 4)

{Check It!|assessment}(multiple-choice-1906116983)
