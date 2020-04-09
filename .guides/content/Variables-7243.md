## Introduction
Consider the following code:

```python
print('Hello '.upper() + 'World! '.lower() + 'I am learning Python!'.capitalize())
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

The same methods we applied to strings (`len()`, `upper()`, `lower()`, `capitalize()`) can be applied to variables that **contain strings**, in the same format. For example, all of the following is valid:

```python
my_variable = 'Hello World'
print(len(my_variable))
print(my_variable.upper())
print(my_variable.lower())
print(my_variable.capitalize())
```

{Try It}(python3 code/fundamentals/variables_demo_4.py)


## Challenge: Revisiting the First Example
Remember this code from the beginning of the page?

```python
print('Hello '.upper() + 'World! '.lower() + 'I am learning Python!'.capitalize())
```
{Try It}(python3 code/fundamentals/variables_demo_1.py)

Can you achieve the same result using a separate variable for each string? Write your code on the left and use the button below to test your code. Remember that **no two variables can share the same name** - assigning a different value to a variable that has already been declared will simply overwrite the previous value of the variable.

{Try It}(python3 code/fundamentals/variables_diy.py)

<details><summary>Need help?</summary>Here is a possible solution:
<code class="language-python"><!-- react-text: 117 -->my_variable = <!-- /react-text --><span class="hljs-string">'Hello World'</span><!-- react-text: 119 -->
print(len(my_variable))
print(my_variable.upper())
print(my_variable.lower())
print(my_variable.capitalize())
<!-- /react-text --></code>
</details>

## Variable Naming Rules
Here are the rules for declaring a variable.

|Rule|Correct|Incorrect|
|----|-------|---------|
|Start with a letter or underscore|`variable`, `_variable`|`1variable`|
|Remainder of variable name is letters, numbers, or underscores|`var_i_able`, `var1able`|`var-i-able`, `var!able`|
|Cannot use a Python keyword|`my_class`|`class`|
|Variables are case sensitive|`variable`, `Variable`, and `VARIABLE` are all different variables|

<details><summary><b>What are the Python key words?</b></summary><table><tr><th></th><th></th><th></th><th></th></tr><tr><td>False</td><td>class</td><td>finally</td><td>is</td></tr><tr><td>return</td><td>None</td><td>continue</td><td>for</td></tr><tr><td>lambda</td><td>try</td><td>True</td><td>def</td></tr><tr><td>from</td><td>nonlocal</td><td>while</td><td>and</td></tr><tr><td>del</td><td>global</td><td>nont</td><td>with</td></tr><tr><td>as</td><td>elif</td><td>if</td><td>or</td></tr><tr><td>yield</td><td>assert</td><td>else</td><td>import</td></tr><tr><td>pass</td><td>break</td><td>except</td><td>in</td></tr><tr><td>raise</td></tr></table></details>