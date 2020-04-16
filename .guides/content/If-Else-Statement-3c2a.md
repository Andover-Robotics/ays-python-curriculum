----------

## If Else Statement

So, what if you want something to happen is a condition is true, but something else to happen when the condition is false? That's where the **else statement** comes in.

## Syntax

An else statement always has to be paired with an if statement. The code within the else statement only runs when the if statement turns out to be false. Otherwise, it is skipped.

Notice, `else` is aligned with the `if` keyword (no indentation) and has a `:`. You do not write another boolean expression with `else`.

![If Else Syntax](.guides/images/if-else-statement-syntax.png)

Copy the code below into your code editor and run it:
```python
if 5 > 4:
    print("The boolean expression is true")
else:
    print("The boolean expression is false")
```

[Code Visualizer](open_tutor code/selection/if-else-statement.py 1)
{try it}(python3 code/selection/if-else-statement.py 1)

|||challenge
## What happens if you:
* Change `4` to `6`?
* Indent the `else` statement four spaces?

[Code Visualizer](open_tutor code/selection/if-else-statement.py 2)
{try it}(python3 code/selection/if-else-statement.py 2)

|||

{Check It!|assessment}(multiple-choice-3776588336)
