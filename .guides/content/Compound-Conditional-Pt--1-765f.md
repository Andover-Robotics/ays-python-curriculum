----------

## Compound Conditional

A compound conditional is a conditional (an if statement) that has more than one boolean expression. You need to use the `and` or the `or` keywords to link these boolean expressions together. You can use the `not` keyword, but only in combination with `and` or `or`.

```python
if True and True:
    print("True")
```

[Code Visualizer](open_tutor code/selection/compound-conditional-syntax.py)
{try it}(python3 code/selection/compound-conditional-syntax.py 1)

|||challenge
## What happens if you:
* Have an if statement that says `if True or False:`?
* Have an if statement that says `if not True or False:`?
* Have an if statement that says `if True not False:`?
* Have an if statement that says `if 5 < 10 and 5 > 0`?

[Code Visualizer](open_tutor code/selection/compound-conditional-syntax.py)
{try it}(python3 code/selection/compound-conditional-syntax.py 2)

|||

<details><summary>**Compound Less Than or Greater Than**</summary>This is Python specific syntax, but it is possible to combine a compound conditional to look like something from a math class. Imagine you have a variable `a` with the value of `5`. You can rewrite `a < 10 and a > 0` to be `0 < a < 10`.</details>

{Check It!|assessment}(multiple-choice-2216399909)

-----
## Why Use Compound Conditionals

Both code snippets below do the same thing: Ask if `my_var` is greater than 15 and if `my_var` is less than 20. If both of these are true, then Python will print the value of `my_var`.

![compound conditional](.guides/images/compound-conditional.png)

The code with the compound conditional (on the right) has fewer lines of code, and is easier for a human to read. In fact, it almost reads like a sentence.

{Check It!|assessment}(multiple-choice-3946834266)

