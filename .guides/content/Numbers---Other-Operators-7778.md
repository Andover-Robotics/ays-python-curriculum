## Modulo
The `%` symbol can be used to perform the **modulo** operation which gives the remainder after integer division. For example, `7 % 3` yields `1`, as the remainder when 7 is divided by 3 is 1. This will be useful when you deal with odd and even numbers.

## Floor Division
The `//` operator performs **floor division**, which yields the result of the division, but with the digits after the decimal point chopped off. For example, `3 // 4` yields `0`, as `0.75` is rounded down to `0`, and `7 // 3` is `2`.

## Working with Variables
When changing the value of an existing variable, the result may be stored back into the same variable.

For example:
```python
x = 1
x = x + 2
print(x)
```

**Try this in your interpreter.**

The output should be 3. In this case, the result of the expression overwrites the previous value of `x`, and that new value is used in all future lines of code. Luckily, Python provides a more concise manner of performing such operations:

```python
x = 1
x += 2
print(x)
```

We no longer have to repeat the name of the variable, which is often longer than just `x`.

* `a += b` is the same as `a = a + b`
* `a *= b` is the same as `a = a * b`
* `a /= b` is the same as `a = a / b`
* `a -= b` is the same as `a = a - b`