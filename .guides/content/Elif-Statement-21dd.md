----------
## Elif Statement

Check out this piece of code:

```python
if grade > 90:
  print('you get A')
else:
  if grade > 80:
    print('you get B')
  else:
    if grade > 70:
      print('you get C')
```

It seems that the more cases you add to this pattern, the more indented your last lines of code become!

What if you wanted to check for a situation that isn't just "this" or "that," but had multiple cases in between? That's where the `elif` statement comes in!

The **elif statement**, short for "else if," is used after an if statement and before an else statement. You can think of it as "otherwise, if ...". Elif statements allow you to specify more than two possible branches of execution in one `if` statement. For example, these two code segments are equivalent:

```python
answer = input('pick a topping for your pizza: pepperoni, mushrooms, or pineapple')
if answer == 'pepperoni':
  print('solid choice')
else:
  if answer == 'mushrooms':
    print('interesting')
  else:
    if answer == 'pineapple':
      print('some people hate this')
```

```python
answer = input('pick a topping for your pizza: pepperoni, mushrooms, or pineapple')
if answer == 'pepperoni':
  print('solid choice')
elif answer == 'mushrooms':
  print('interesting')
elif answer == 'pineapple':
  print('some people hate this')
```

The latter is much easier to read and reason about than the former segment.

## Syntax

The elif statement is written similarly to the if statement. There are few differences as well. Here are the rules for writing an elif statement:

* An if statement must come before the first elif statement
* `elif` is followed by a boolean expression and a `:`
* Indent and write the code for when the elif statement's condition is True
* You can write as many elif statements as you want

![elif Statement](.guides/images/elif-statement.png)

Try out the code below:
```python
a = 20

if a < 10:
    print(str(a) + " is less than 10")
elif a < 20:
    print(str(a) + " is less than 20")
elif a < 30:
    print(str(a) + " less than 30")
else:
    print(str(a) + " is greater than 30")
```

[Code Visualizer](open_tutor code/selection/elif-syntax.py)
{try it}(python3 code/selection/elif-syntax.py 1)

|||challenge
## What happens if you:
* Change `a` to `0`?
* Change `a` to `100`?
* Change `a` to `30`? (How can you fix this?)

[Code Visualizer](open_tutor code/selection/elif-syntax.py)
{try it}(python3 code/selection/elif-syntax.py 2)

|||

{Check It!|assessment}(multiple-choice-1573332278)

----

The picture below shows how the elif statement can be more precise than just an if or an if else statement

![elif Statement](.guides/images/if-vs-else-vs-elif.png)

|||challenge
## Can you...
Copy the code from above, but add the letter grade D which is any grade from 60 to 69?

**Testing Your Code**
Change `grade` to `65`. You should see `You got a D.` as the output of your program.

<details><summary>**Hint**</summary>You need to change the if statement and add another elif statement.</details>

[Code Visualizer](open_tutor code/selection/elif-syntax.py)
{try it}(python3 code/selection/elif-syntax.py 3)

|||
