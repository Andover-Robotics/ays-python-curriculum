## `len()`
`len()` gives the length of the string inside its parentheses (the number of characters in the string, including whitespace of any kind).

```python
print(len('This message has 30 characters'))
```

{Try It}(python3 code/fundamentals/string_methods_demo_1.py)

## `upper()`
`upper()` capitalizes *every letter* in a string. 

```python
print('This Is My Message'.upper())
```

{Try It}(python3 code/fundamentals/string_methods_demo_2.py)


## `lower()`
`upper()` makes *every letter* in a string lowercase. 

```python
print('This Is My Message'.lower())
```

{Try It}(python3 code/fundamentals/string_methods_demo_3.py)

## `capitalize()`
`capitalize()` capitalizes the *first letter* of the string and makes every other letter lowercase.

```python
print('This Is My Message'.capitalize())
```

{Try It}(python3 code/fundamentals/string_methods_demo_4.py)

## An Important Note
`len()` and `print()` both encompass the strings they affect, but `upper()`, `lower()`, and `capitalize()` come after the string and a `.` character. There may *not* be a space between the end of the string and the `.`, or between the `.` and `upper()`, `lower()`, or `capitalize()`. Although the reasonsing for this is beyond the scope of our knowledge at this point, it is crucial that you keep this in mind.