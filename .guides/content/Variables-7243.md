Consider a program that performs basic geometric operations with circles. As you know from math class, most geometric calculations involving circles (like circumference, area, etc.) involve the constant $\pi$, which is about $3.14$. You may simply use this approximated value in your calculations, but computers are used for much more precise situations where this is not enough.

So what, repeat $3.141592653589793$ every time we use it? There has to be a better way!

Your familiar interpreter is open on the left. Try this:
```python
pi = 3.141592653
```
And then:
```python
pi
```

You told the computer what `pi` refers to, and it remembered! You have just made a **variable**, a name that refers to a value.

## Variables
A **variable** is a place to store something, and each variable has a name. To **declare a variable**, use the following code:

`my_variable_name = 'value'`

Notice that there are **no spaces in the variable's name**; this would cause a syntax error! Let us show some demos:

```python
message = 'Hello world'
print(message)
```

{Try It}(python3 code/fundamentals/variables_demo_2.py)

But what happens if we put quotation marks around `message` in the `print()` statement?

```python
message = 'Hello world'
print('message')
```

{Try It}(python3 code/fundamentals/variables_demo_3.py)

These are very different results. Why? When the `'`s are added, `'message'` becomes a string, not as the variable `message`.

Once you have specified that `message = 'Hello world'`, you can refer to it later on with `message`:

```python
my_variable = 'Hello World'
print(my_variable)
print(my_variable + ' I am learning Python!')
```

Try running these statements in your interpreter.

## Variable Naming Rules
Here are the rules for declaring a variable.

|Rule|Correct|Incorrect|
|----|-------|---------|
|Start with a letter or underscore|`variable`, `_variable`|`1variable`|
|Remainder of variable name is letters, numbers, or underscores|`var_i_able`, `var1able`|`var-i-able`, `var!able`|
|Cannot use a Python keyword|`my_class`|`class`|
|**Variables are case sensitive**|`variable`, `Variable`, and `VARIABLE` are all different variables|

### Conventions

To promote consistency, Python has a set of official _conventions_ for variable names. Unlike the rules above, _conventions_ are not enforced by the computer, but by the programmer through discipline. Following naming conventions can also save you troubleshooting time later on, since you never have to check if you decided to capitalize a variable name and forgot about it later, for example.

Essentially, Python recommends that you name variables all lowercase, with spaces replaced with underscores. So, the User ID's variable would be called `user_id`, for instance. In a game, the high score would be called `high_score`.

<details><summary>What is a keyword?</summary>A keyword is a word that has been reserved by Python because it serves a purpose in the program's compilation and execution. Keywords are case sensitive and are used too define the syntax and structure of Python.</details>
<details><summary><b>What are the Python keywords?</b></summary><table><tr><th></th><th></th><th></th><th></th></tr><tr><td>False</td><td>class</td><td>finally</td><td>is</td></tr><tr><td>return</td><td>None</td><td>continue</td><td>for</td></tr><tr><td>lambda</td><td>try</td><td>True</td><td>def</td></tr><tr><td>from</td><td>nonlocal</td><td>while</td><td>and</td></tr><tr><td>del</td><td>global</td><td>nont</td><td>with</td></tr><tr><td>as</td><td>elif</td><td>if</td><td>or</td></tr><tr><td>yield</td><td>assert</td><td>else</td><td>import</td></tr><tr><td>pass</td><td>break</td><td>except</td><td>in</td></tr><tr><td>raise</td></tr></table></details>

{Check It!|assessment}(multiple-choice-259764082)