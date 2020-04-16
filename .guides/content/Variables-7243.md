## Introduction
Consider the following code:

```python
print('Hello ' + 'World! ' + 'I am learning Python!')
```

{Try It}(python3 code/fundamentals/variables_demo_1.py)

With all these strings, things are getting pretty messy and confusing in our code. How could we fix this?

## Variables
This is where variables come in. A **variable** is a named value that can later be read and modified. To **declare a vaiable**, use the following code:

`my_variable_name = 'value'`

Notice that there are **no spaces in the variable's name**; this would cause a Syntax Error! Let us example some demos:

```python
my_variable = 'Hello world'
print(my_variable)
```

{Try It}(python3 code/fundamentals/variables_demo_2.py)

But what happens if we put quotation marks around `my_variable` in the `print()` statement?

```python
my_variable = 'Hello world'
print('my_variable')
```

{Try It}(python3 code/fundamentals/variables_demo_3.py)

These are very different results. Why? When the `'`s are added, `'my_variable'` is interpreted as a string, not as the variable `my_variable`. 

The properties of strings are applied to any variable that **contains strings**.

```python
my_variable = 'Hello World'
print(my_variable)
print(my_variable + ' I am learning Python!')
```

{Try It}(python3 code/fundamentals/variables_demo_4.py)

## Variable Naming Rules
Here are the rules for declaring a variable.

|Rule|Correct|Incorrect|
|----|-------|---------|
|Start with a letter or underscore|`variable`, `_variable`|`1variable`|
|Remainder of variable name is letters, numbers, or underscores|`var_i_able`, `var1able`|`var-i-able`, `var!able`|
|Cannot use a Python keyword|`my_class`|`class`|
|Variables are case sensitive|`variable`, `Variable`, and `VARIABLE` are all different variables|

<details><summary>What is a keyword?</summary>A keyword is a word that has been reserved by Python because it serves a purpose in the program's compilation and execution. Keywords are case sensitive and are used too define the syntax and structure of Python.</details>
<details><summary><b>What are the Python keywords?</b></summary><table><tr><th></th><th></th><th></th><th></th></tr><tr><td>False</td><td>class</td><td>finally</td><td>is</td></tr><tr><td>return</td><td>None</td><td>continue</td><td>for</td></tr><tr><td>lambda</td><td>try</td><td>True</td><td>def</td></tr><tr><td>from</td><td>nonlocal</td><td>while</td><td>and</td></tr><tr><td>del</td><td>global</td><td>nont</td><td>with</td></tr><tr><td>as</td><td>elif</td><td>if</td><td>or</td></tr><tr><td>yield</td><td>assert</td><td>else</td><td>import</td></tr><tr><td>pass</td><td>break</td><td>except</td><td>in</td></tr><tr><td>raise</td></tr></table></details>