## Introducing Numbers
You've already seen `pi` in action. You can remove the quotes surrounding a number, and the number's value will be saved numerically, so you can calculate with them later.

Some examples:
```python
a = 123
b = 0.456
c = 789.0123
print(a)
print(b)
print(c)
print(a + b)
```

**Try typing this into your interpreter.**

<details><summary>If these are not strings, why does `print()` work?</summary>When something is passed into `print()`, it is *converted* into a string if it is not already a string. For example, calling `print(1)` will have the same result as calling `print('1')`, although `1` and `'1'` are very different (one is a number, one is a piece of text).</details>

## Number Operations 
When dealing with numbers, there are a multitude of mathematical operations that can be used.

### Addition
To add two numbers, simply insert a `+` between them. 

For example:

```python
a = 3
b = 4
print(a + b)
```

**Try this in your interpreter.** The output should be `7`.

### Subtraction
To subtract two numbers, simply insert a `-` between them. 

For example:

```python
a = 3
b = 4
print(a - b)
```

Yields `-1`.

### Multiplication
To multiply two numbers, simply insert a `*` between them. 

For example,

```python
a = 3
b = 4
print(a * b)
```

Yields `12`.

### Division
To divide two numbers, simply insert a `/` between them. 

For example:

```python
a = 3
b = 4
print(a / b)
```

Yields `0.75`.

### Order of Operations
In Python, math is interpreted in the same order as it is in algebra. Remember PEMDAS: Parentheses, Exponents, Multiplication / Division, Addition / Subtraction (from left to right).

This is important to remember because in Python you can easily **chain different operations**, thus:

```python
print(2 + 3 * 4 - 5)
```

Yields `9`, but

```python
print((2 + 3) * 4 - 5)
```

Yields `15`.
