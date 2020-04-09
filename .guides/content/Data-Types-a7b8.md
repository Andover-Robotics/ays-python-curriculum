## What is a Data Type?
So far, we have worked with strings and numbers. But why distinct them? After all, both may be saved in a variable! The difference, however, is their **Data Type**, or the classification of the data they each represent. There are many different types of data types in Python, but the 4 main data types in Python:

* **Strings**
* There are two different types of numbers:
  * **ints** - integers (numbers without decimal points), such as `2`
  * **floats** - numbers that have a decimal point, such as `2.1`
* **Booleans** - A value that is either **`True`** or **`False`** (the capitalization is important!)

## Why are Data Types Important?
**Different operations may be performed on different data types**. Strings may be affected by `upper()`, `lower()`, `capitalize()`, and more, for example, but but what happens if we try to call them on a number?

```python
my_variable = 10
print(my_variable.upper())
```

{try it}(python3 code/fundamentals/data_type_demo_1.py)

As you can see, an error is thrown. This is because the number is not the right data type for the operation we are trying to perform. The same is true for many other operators, such as mathematical operators. For example, attempting to add a number to a string will result in an error, as you may only add two strings together or two numbers together.

```python
print('10' + 10)
```

{try it}(python3 code/fundamentals/data_type_demo_2.py)

There is an exception to this string-integer operation incompatibility, however: multiplicaton. What do you think the following code does?

```python
print('123' * 2)
```

{try it}(python3 code/fundamentals/data_type_demo_3.py)

Were you right?

## Your Turn
Experiment with different data types in the editor on the left. Use this button to execute your code:

{try it}(python3 code/fundamentals/data_type_diy.py)