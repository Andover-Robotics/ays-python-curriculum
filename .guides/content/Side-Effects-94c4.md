----------

## Side Effects

Side effects are any changes that a function produces that modify things outside of the function's scope. Examples of side effects are printing to the screen, changing a global variable, writing to a file, etc. Sometimes side effects are the desired outcome, but there are many programmers who believe that functions should not have side effects (these are called pure functions). 

This belief is due to the idea that functions you write in one program can and should be applied to others to avoid repeating work. If your functions depend on global variables or otherwise change things outside of their scope, it not only makes it more difficult to catch an error, but it makes them impossible to reuse without significant modification.

The examples below demonstrate how to incorporate pure functions into programs that have side effects.

### Modify a Global Variable

Global variables can be modified by a function without using the `global` keyword (using the global keyword is a side effect). This is accomplished by simply assigning the return value of the desired function into the global variable. In the for loop, the new value of `my_num` is calculated by calling the function `add_5`. You can see the value of `my_num` change each time the loop runs.

```python
my_num = 0

def add_5(num):
    """Receive a number, add 5 tot the number, and
    return the new number"""
    return(num + 5)
  
for i in range(10):
    my_num = add_5(my_num)
    print(my_num)
```

{try it}(python3 code/functions/side-effects.py 1)

|||challenge
## Your Turn! 
- You are given a program that looks like this: 
```python
my_num = 0

def subtract_5():
    """Subtract 5 from my_num and return the new number"""
    return(my_num + 5)
  
for i in range(10):
    my_num = subtract_5()
    print(my_num)
```
- In this program, we never call the function until my_num is defined. However, that may not be the case in other programs, leading to errors. Your task is to fix it so that you can reuse the function in other programs. 

<details><summary>**Solution**</summary>
```python
  def subtract_5(my_num):
    """Subtract 5 from my_num and return the new number"""
    return(my_num + 5)
  
my_num = 0
for i in range(10):
    my_num = subtract_5(my_num)
    print(my_num)
```
</details>

|||

{try it}(python3 code/functions/side-effects.py 2)

### Printing

The code below prints if a number is odd or even. The first function determines if a number is odd or even. The second function constructs the appropriate string. Neither function has a side effect. The act of printing is left to the main program.

```python
def is_even(num):
    """Return True if num is even
    return False if num is odd"""
    return num % 2 == 0
  
def output(num):
    """Return a string with a number,
    and states if that number is even or odd"""
    if is_even(num):
        return "{} is an even number.".format(num)
    else:
        return "{} is an odd number.".format(num)
  
print(output(2))
```

{try it}(python3 code/functions/side-effects.py 3)

|||challenge
## What happens if you:
* Change the print statement to `print(output(3))`?

|||

{try it}(python3 code/functions/side-effects.py 4)

### Are Side Effects Bad?

No, side effects are not bad. In fact, they may be the desired result. However, the more side effects a function produces, the greater the risk of introducing a bug, because it's more difficult to see where your variables are being edited if that's happening from inside a function. On the other hand, if your function only returns a value and doesn’t change anything outside of that, it is much easier to track the function to which a bug belongs. Additionally, functions you write in one program can and should be applied to others to avoid repeating work. If your functions depend on global variables or otherwise change things outside of their scope, it not only makes it more difficult to catch an error, but it makes them impossible to reuse without significant modification.

Think about the functions you are writing. If possible, break up your code into several smaller functions, and only introduce side effects when necessary. This may mean you have to write more code, but if this keeps you from having to spend a lot of time debugging, then it is time well spent.

{Check It!|assessment}(multiple-choice-511526029)
