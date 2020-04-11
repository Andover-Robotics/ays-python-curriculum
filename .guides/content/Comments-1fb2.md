Not all code is immediately understandable. To help others (and yourself) understand what everything is doing, **comments** should be employed. 

There are two kinds of comments:
  * **Single-line** comments
  * **Multi-line** comments
  
## Single-line Comments
To make a single-line comment, simply insert a `#`. Everything from the `#` to the end of the line will then be interpreted as a comment (that is to say, it will not be interpreted at all as code)

For example:
```python
# This is a comment
print('Hello World') # This comment comes after code
# print('My second message')

number = 10
# number += 20
number = number #+ 30

# Output the final result
print(number)
```

{try it}(python3 code/fundamentals/comments_demo_1.py)

Notice what parts of the code have been executed and what has been commented out.

## Multi-line Comments
To make a multi-line comment you have two options:
* Add a `#` at the beginning of every line that is a part of your comment
* Add `"""`s at the beginning and ends of your comments, like so:

```python
"""
This is a "block comment" in Python.
Pay attention to the format.
Any code written here will not be executed
print('Hello')
"""
print('World')
```

{try it}(python3 code/fundamentals/comments_demo_2.py)

Using comments will result in better, clearer code and easier collaboration.