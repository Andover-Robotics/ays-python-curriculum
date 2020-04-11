----------
## Testing Multiple Cases

You will find yourself needing to test the same variable multiple times. Be sure that you set up your conditionals to test **all** possible values of the variable.

```python
grade = 90

if grade > 70:
    print("Congrats, you passed the class")
    
if grade < 70:
    print("Condolences, you did not pass the class")
```

[Code Visualizer](open_tutor code/selection/if-statement-pt2.py)
{try it}(python3 code/selection/if-statement-pt2.py 1)

|||challenge
## What happens if you:
* Change `grade` to `60`?
* Change `grade` to `70`?
* Change `grade > 70` to `grade >= 70`?

[Code Visualizer](open_tutor code/selection/if-statement.py)
{try it}(python3 code/selection/if-statement-pt2.py 2)

|||

