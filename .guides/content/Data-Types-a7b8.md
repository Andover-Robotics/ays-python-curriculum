## What is a Data Type?
So far, we have worked with strings and numbers. But why distinct them? After all, both may be saved in a variable! The difference, however, is their **Data Type**, or the classification of the data they each represent. There are many different types of data types in Python, but the 4 main data types in Python:

* **Strings**
* There are two different types of numbers:
  * **ints** - integers (numbers without decimal points), such as `2`
  * **floats** - numbers that have a decimal point, such as `2.1`
* **Booleans** - A value that is either **`True`** or **`False`** (the capitalization is important!)

## Why are Data Types Important?
**Different operations may be performed on different data types**. For example, addition with strings may work one way (concatenation), but what happens if we try to perform the same operations on numbers?

```python
my_num_one = 10
my_num_two = 20
my_string_one = '10'
my_string_two = '20'
print(my_num_one + my_num_two)
print(my_string_one + my_string_two)
```

{try it}(python3 code/fundamentals/data_type_demo_1.py)

As you can see, the operation functioned very differently across the different data types.

But what if we try to add two different data types together?

```python
print('10' + 10)
```

{try it}(python3 code/fundamentals/data_type_demo_2.py)

Once again, another error is thrown!

There is an exception to this string-integer operation incompatibility, however: multiplicaton. What do you think the following code does?

```python
print('123' * 2)
```

{try it}(python3 code/fundamentals/data_type_demo_3.py)

Were you right?