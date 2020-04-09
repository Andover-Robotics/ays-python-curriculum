## Introducing Numbers
To store a **number** in a variable, simply assign the variable to the number (not as a string).

Some examples:
```python
whole_number = 123
decimal_number = 0.456
big_number = 789.0123
print(whole_number)
print(decimal_number)
print(big_number)
```

{try_it}(python3 code/fundamentals/numbers_demo_1.py)

<details><summary>If these are not strings, why does `print()` work?</summary>When something is passed into `print()`, it is *converted* into a string if it is not already a string. For example, calling `print(1)` will have the same result as calling `print('1')`, although `1` and `'1'` are very different (one is a number, one is a string).</details>

## Number Operations 
When dealing with numbers, there are a multitude of mathematical operations that can be used.

### Addition
To add two numbers, simply insert a `+` between them. 

For example:

```python
num_one = 3
num_two = 4
print(num_one + num_two)
```

Yields `7`.
### Subtraction
To subtract two numbers, simply insert a `-` between them. 

For example:

```python
num_one = 3
num_two = 4
print(num_one - num_two)
```

Yields `-1`.

### Multiplication
To multiply two numbers, simply insert a `*` between them. 

For example,

```python
num_one = 3
num_two = 4
print(num_one * num_two)
```

Yields `12`.

### Division
To divide two numbers, simply insert a `/` between them. 

For example:

```python
num_one = 3
num_two = 4
print(num_one / num_two)
```

Yields `0.75`.

### Order of Operations
In Python, math is interpreted in the same order as it is in algebra. Remember PEMDAS: Parentheses, Exponents, Multiplication / Division, Addition / Subtraction (from left to right).

This is important to remember because in Python you can easily **string together operations**, thus:

```python
print(2 + 3 * 4 - 5)
```

Yields `9`, but

```python
print((2 + 3) * 4 - 5)
```

Yields `15`.
