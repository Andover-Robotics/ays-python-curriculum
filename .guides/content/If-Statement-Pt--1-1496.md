----------

## If Statement 

Conditionals are pieces of code that make a decision about what the program is going to do next. The most common conditional is the if statement.

**If statements** test to see if a certain condition is true. If yes, then a specific commands are run. If not, it doesn't do anything.

## Syntax

![If Statement Syntax](.guides/images/if-statement-syntax.png)


If statements in Python must contain the following items:
* the keyword `if`
* a boolean expression
* a colon
* 4 spaces of indentation for all lines of code that will run if the boolean expression is true.

Try out the code below. Remember that you can use the code visualizer to see how the code works step by step.

```python
if 7 != 10:
    print("The above statement is true")
print("This is not related to the if statement")
```

[Code Visualizer](open_tutor code/selection/if-statement-pt1.py)
{try it}(python3 code/selection/if-statement-pt1.py 1)

|||challenge
## What happens if you:
* Change `!=` to `==`?
* Change `7 == 10` to `True`?
* Change `True` to `False`?
* Remove the indentation on line 2?

[Code Visualizer](open_tutor code/selection/if-statement-pt1.py)
{try it}(python3 code/selection/if-statement-pt1.py 2)

|||

----
## The Whitespace
You may have noticed in the diagram above that there is an indent of exactly four spaces in front of the first two print statements. If those indents were not there, the program would run differently. Why is this indent so important?

In many other programming languages, there are specific characters that tells the computer where statements start and end. For example, in Java, you put a semicolon `;` at the end of each statement. Think of it as punctuation, but for code.

However, in Python, we do not have any set characters that tell the computer where to start and stop reading. Instead, it uses line breaks and indents, aka "whitespace." The indents in front of those two print statements tell the computer that they belong to the if statement, and will only run if the if statement is true.

As for the four spaces, that's just what the Python community has agreed to be the size of an indent. Hitting the `tab` key on your keyboard will work as well.
