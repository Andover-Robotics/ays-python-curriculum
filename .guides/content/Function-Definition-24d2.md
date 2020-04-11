----------

## Function Syntax

In several of your past projects, you may have found yourself needing the same bits of code over and over again at different points in your program. In the past, you would have typed out the piece you needed each time that you used it -- but programmers use something called a function to avoid that redundancy. A function is a piece of code that, once you define what it does somewhere in your code, you can use (call) as many times as you want without retyping it. You can even input values into your functions (parameters) so that they perform differently based on your input! 

You have already seen and used built-in functions like the length function (`len(my_list)`). The len function takes in a list as input and outputs its length based on its preset instructions, or definition. This unit deals with user-defined functions -- functions you write yourself that are specific to what your code needs. Functions are composed of two parts, the header (the specifications of the function) and the body (the actual code that the function performs).

![Function Header & Body](.guides/images/function-header-body.png)

Before you can use your function, you must define it so that the computer knows the name of your function, the parameters or input it is looking for, and what it does. When you define a function, you must start with a header. The function header contains the `def` keyword which signals the definition of a function. Next is the name of the function. Function names follow the same rules as variable names; letters, numbers, and underscores. Function names cannot start with a number. Parentheses are required, and any parameters (your input) go between them. Finally, the header ends with a colon to signal the start of the body.


![Function Header](.guides/images/function-header.png)

The function body is the list of actions the function performs. All of the code for the function body must be indented (four spaces is the Python standard) from the function header. The function ends when the code is no longer indented.

![Function Body](.guides/images/function-body.png)

## Calling a Function

If you only define a function, you never tell the computer when to use it! For an example, enter the code below into the editor and click the `TRY IT` button. Nothing is printed. You have only alerted you program to the existence of your function: you have not specified how to use it.

```python
def greet_twice():
    print("Hello")
    print("Hello")
```

{try it}(python3 code/functions/call-function.py 1)

You have to explicitly call the function if you want it to run. Add `greet_twice()` after the function definition. This call does exactly what you would expect: it just tells Python to perform the code inside the function. Remember: **do not** indent the function call (because anything indented is still part of the function!). Run the code again.

```python
def greet_twice():
    print("Hello")
    print("Hello")
    
greet_twice()
```

{try it}(python3 code/functions/call-function.py 2)

|||challenge
## Your Turn!
* Instead of greeting the user twice, greet them four times without changing the function definition.

{try it}(python3 code/functions/call-function.py 3)
|||



|||challenge
## Your Turn!
* Customize the function definition to use your name when it greets you!

{try it}(python3 code/functions/call-function.py 4)
|||



{Check It!|assessment}(multiple-choice-1896286432)
