----------
## Boolean Operators
When you write an if statement, you will usually use it to compare the values of two different variables. These variables can be compared using **boolean operators**. As a quick review, a **boolean** can only take on two values: yes (`True`) or no (`False`). Below is a list of some very useful boolean operators:

* `==`: is equal to (not to be confused with `=`, which is used to assign variables)
* `!=`: is **not** equal to (the `!` means not)
* `<`: less than
* `<=`: greater than or equal to
* `>`: greater than
* `>=`: greater than or equal to

Some of these symbols may seem familiar to you from math class. These boolean operators are the same for pretty much every programming language, which is nice.

|||challenge
## Try it yourself:

Write one true boolean expression and one false boolean expression. Then, print out their results.

{try it}(python3 code/selection/if-statement-pt2.py 1)

|||

## Testing Multiple Cases

You will find yourself needing to test the same variable multiple times. Be sure that you set up your conditionals to test **all** possible values of the variable.

Copy the following code into the code editor and run it:
```python
grade = 90

if grade > 70:
    print("Congrats, you passed the class")
    
if grade < 70:
    print("Condolences, you did not pass the class")
```

[Code Visualizer](open_tutor code/selection/if-statement-pt2.py)
{try it}(python3 code/selection/if-statement-pt2.py 2)

|||challenge
## What happens if you:
* Change `grade` to `60`?
* Change `grade` to `70`?
* Change `grade > 70` to `grade >= 70`?

[Code Visualizer](open_tutor code/selection/if-statement.py)
{try it}(python3 code/selection/if-statement-pt2.py 3)

|||

{Check It!|assessment}(free-text-auto-1037488722)
