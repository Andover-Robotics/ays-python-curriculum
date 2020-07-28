![Decision based on the password](.guides/img/decisions.png)

Consider your usual sign-in page, where you have to enter a username and a password. If the password you entered was correct, the computer should let you in. If the password you entered was incorrect, it should tell you so and not let you in. How do we code this form of decision making based on a condition?

## If Statement 

Conditionals are pieces of code that make a decision about what the program is going to do next. The most common conditional is the if statement.

**If statements** check if a certain condition is true. If it is true, then the piece of code inside the statement will run. If it is false, then that code is skipped, and the program continues with whatever code comes after the statement.

## Syntax

![If Statement Syntax](.guides/images/if-statement-syntax.png)

If statements in Python must contain the following items:
* the keyword `if`
* a boolean expression
* a colon
* spaces of indentation for all lines of code that will run if the boolean expression is true.

What do you predict will print out from the code below? **Copy the code into your code editor on the left and run it.**

```python
if True:
  print("The above statement is true")
print("This is not related to the if statement")
```


|||challenge
## What happens if you:
* Change `True` to `False`?
* Remove the indentation on line 2?

[Code Visualizer](open_tutor code/selection/if-statement-pt1.py)
{try it}(python3 code/selection/if-statement-pt1.py 2)

|||

----
## The Whitespace
You may have noticed in the diagram above that there is an indent of exactly two spaces in front of the first two print statements. If those indents were not there, the program would run totally differently. Why is that?

Python uses line breaks and indents, i.e. "whitespace" to express code blocks. The indents in front of those two print statements tell the computer that they belong to the if statement and will only run when a condition is met.

When you write code with any code-aware editor (like the one here on Codio), the editor will automatically start the indent for you and keep the indent when you press `enter`. If you have to manually press `space` to indent, there's a good chance that you are missing a colon at the end of the line with `if`.

If you ever need to indent many lines at once, you can select the lines with your mouse and press `tab`. To remove a level of indent, press `shift+tab`. Feel free to try this out.

## Check your understanding

{Check It!|assessment}(multiple-choice-2553315478)
