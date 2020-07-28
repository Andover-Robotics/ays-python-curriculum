Not all code is immediately understandable by all programmers. To help others (and future you) understand what everything is doing, **comments** can be employed. 

To make a single-line comment, simply insert a `#`. The computer will ignore everything from the `#` to the end of the line.

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

When maintaining a piece of code for a long time, comments become very useful. When people can't figure out what your code is trying to do at a high level, you need to add comments that explain what you're trying to do and why you're doing it a particular way. As Martin Fowler puts it,

<blockquote>
  Any fool can write code that a computer can understand. Good programmers write code that humans can understand.
</blockquote>