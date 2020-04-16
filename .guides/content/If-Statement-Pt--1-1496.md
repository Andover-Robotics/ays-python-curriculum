----------

## If Statement 

Conditionals are pieces of code that make a decision about what the program is going to do next. The most common conditional is the if statement.

**If statements** test to see if a certain condition is true. If it is true, then a certain set of code will run. If it is false, then that code is skipped and the program continues with whatever code comes after.

## Syntax

![If Statement Syntax](.guides/images/if-statement-syntax.png)


If statements in Python must contain the following items:
* the keyword `if`
* a boolean expression
* a colon
* 4 spaces of indentation for all lines of code that will run if the boolean expression is true.

What do you predict will print out from the code below? Copy the code into your code editor on the left and run it. You can use the code visualizer to see a step-by-step breakdown.

```python
if True:
    print("The above statement is true")
print("This is not related to the if statement")
```

[Code Visualizer](open_tutor code/selection/if-statement-pt1.py)
{try it}(python3 code/selection/if-statement-pt1.py 1)

|||challenge
## What happens if you:
* Change `True` to `False`?
* Remove the indentation on line 2?

[Code Visualizer](open_tutor code/selection/if-statement-pt1.py)
{try it}(python3 code/selection/if-statement-pt1.py 2)

|||

----
## The Whitespace
You may have noticed in the diagram above that there is an indent of exactly four spaces in front of the first two print statements. If those indents were not there, the program would run totally differently. Why is that?

In many other programming languages, there are specific characters that tell the computer where statements start and end. For example, in Java, you put a semicolon `;` at the end of each statement. Think of it as punctuation, but for code.

However, in Python, we do not have any set characters that tell the computer where to start and stop reading. Instead, it uses line breaks and indents, aka "whitespace" to do this. The indents in front of those two print statements tell the computer that they belong to the if statement, and will only run if the if statement is true.

As for the four spaces, that's just what the Python community has agreed to be the size of an indent. Hitting the `tab` key on your keyboard will work as well.
