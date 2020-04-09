## Modulo
The `%` symbol can be used to perform the **modulo** operation which gives the remainder of a division operation. For example, `7 % 3` yields `1`, as the remainder when 7 is divided by 3 is 1. 

## Floor Division
The `//` operator performs **floor division**, which yields the quotient rounded down to the nearest whole number. For example `3 // 4` yields `0`, as `0.75` is rounded down to `0`, and `7 // 3` yields `2`.

## Working with Variables
When modifying an existing variable, the result may be stored back into the same variable.

For example:
```python
my_number = 1
my_number = my_number + 2
my_number = my_number * 3
my_number = my_number / 2
my_number = my_number - 1
print(my_number)
```

Which yields `3.5` (1 + 2 = 3, 3 * 3 = 9, 9 / 2 = 4.5, 4.5 - 1 = 3.5). In this case, the result of the expression overwrites the previous value of `my_number`, and that new value is used in all future lines of code. Luckily, Python provides a more concise manner of performing such operations:

```python
my_number = 1
my_number += 2
my_number *= 3
my_number /= 2
my_number -= 1
print(my_number)
```

How does this work? Consider these 4 operators:

* `a += b` is the same as `a = a + b`
* `a *= b` is the same as `a = a * b`
* `a /= b` is the same as `a = a / b`
* `a -= b` is the same as `a = a - b`

Although the operators covered on this page are far less common than basic math operators, keep them in mind as they are still quite useful.