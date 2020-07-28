## What is a Data Type?
So far, we have worked with strings and numbers. But why distinct them? After all, both may be saved in a variable! The difference, however, is their **Data Type**, or the kind of the data they each represent. There are many different types of data types in Python, but the 4 main data types in Python:

* **Strings**
* There are two different types of numbers:
  * **ints** - integers (numbers without decimal points), such as `2`
  * **floats** - numbers that have a decimal point, such as `2.1`
* **Booleans** - A value that is either **`True`** or **`False`** (the capitalization is important!)

## Why are Data Types Important?
**Different operations may be performed on different data types**. For example, addition with strings may work one way (concatenation), but what happens if we try to perform the same operations on numbers? **Try the following two lines in your interpreter.**

```python
10 + 20
'10' + '20'
```

As you can see, the operation was very different across the different data types. The computer thinks the first sum is 30, but it thinks the second sum is 1020.

But what if we try to add two different data types together?

```python
print('10' + 10)
```

{try it}(python3 code/fundamentals/data_type_demo_2.py)

The computer sees `'10'` as a piece of text (like `'ten'`), and it doesn't make sense to add a number to a piece of text.

There is an exception to this string-integer operation incompatibility, however: multiplication. What do you think the following represents?

```python
'no' * 3
```

<!-- {try it}(python3 code/fundamentals/data_type_demo_3.py) -->
**Try it in your interpreter.**

Were you right?