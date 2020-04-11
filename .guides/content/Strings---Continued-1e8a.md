## `'` or `"`?
In Python, you can write a string using both single quotes (`'`) and double quotes ('"'), but you cannot mix and match. Thus, in the following code:

```python
print("Hello World")
print('Hello World')
```

both are these lines are valid and would function exactly the same. The line `print('Hello World")`, however, is not valid.

## What if I need an apostrophe?

If you are using double quotes, you don't have to do anything! Single quotes will not be interpreted as the end of the string in a double-quote-enclosed string. Thus, the line `print("It's a miracle!")` is perfectly valid.

If you are using single quotes, your apostrophe would be interpreted as the end of the string and your code would not function properly (a syntax error would likely be thrown). Thus, the line `print('It's a miracle!')` would not be valid, as the interpreter would see two strings: `'It'` and an unclosed string, `')`. This would result in a syntax error and your code would not run. To fix this, you must **escape the character** by placing a `\` before the `'`. Thus, `print('It\'s a miracle')` is perfectly valid and would output `It's a miracle!`. This is because the preceding `\` tells the interpreter that the following `'` is not a part of your code, but is a part of the string itself. 

## What if I need a quote?

The opposite of the apostrophe case occurs: 

If you are using single quotes, you don't have to do anything! Thus, the line `print('He had me at "Hello World"')` is perfectly valid.

If you are using double quotes, you would have to **escape the character** for the same reason that you must escape the apostrophe in a single-quote-enclosed string. The `"` is escaped in the same way as the `'`, by adding a preceding `\`. Thus, the line `print("He had me at "Hello World"")` is invalid, but the line `print("He had me at \"Hello World\"")` works properly and outputs `He had me at "Hello World"`.


## So which should you use?

It all comes down to personal preference, but it is recommended that you **stay consistent** throughout your Python code. Although it is not technically incorrect, switching between single-quote-enclosed strings and double-quote-enclosed strings can make things confusing for you and your collaborators.