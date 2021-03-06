|||guidance
This page should take around 15 minutes.
|||
## What is a List?

A list is a built-in data structure that groups pieces of data in a sequence. Think of your typical grocery list--a sequence of items. Lists are declared with the `[]` brackets, and a comma separates each item in a list. Lists are mutable, which means you can change them after you make them. The values in a list are called **elements** or sometimes **items**.

## Declaring a List
```python
[1, 4, 7, 10]
numbers = [1, 2, 3, 4, 5]
truths = [False, True, True, 2020]
covid_prevention = ["wash hands", "social distance", "avoid touching face", "wear masks"]
```

To create an empty list, the most idiomatic syntax would be `[]`.

|||challenge
**Your Turn:** Make a list of your activities during quarantine and print it. Make sure it has at least four elements.

{try it}(python3 code/lists/list-basics.py 1)
|||

## Accessing Elements

Each element in a list has its own **index**, which corresponds to the element's position in the list. The first element in a list has an index of 0, the second element in a list has an index of 1, and so forth.

For example, to retrieve the third element from a list named `names`, the syntax would be `names[2]`.

![List Indices](.guides/images/list-and-index.png)

|||challenge
**Your Turn:** Print the second element of your list of activities during quarantine.

{try it}(python3 code/lists/list-basics.py 2)
|||

### Exotic Indexes

What happens when I have a list of 4 elements and try to access the fifth? Try it.

|||challenge
**Your Turn:** Try to print the 1000th element of your list of activities during quarantine.

{try it}(python3 code/lists/list-basics.py 3)
|||

|||info
What you might have just seen was a **runtime error**. Runtime errors indicate that something has gone wrong while the program is running. You asked the computer to get the 1000th element, but there aren't 1000 elements to begin with! The computer cannot fulfill your request, so it raises an error.
|||

#### Negative Indexes

A specialty of Python lists is that you can use negative indexes to count from the last element to the front. For example, `numbers[-1]` refers to the **last** element in `numbers`. Following this, `numbers[-2]` refers to the second-to-last element. Notice how we start counting from 1 instead of 0 when the indexes are negative, as `-0` is the same as `0` and would refer to the first element instead.

|||challenge
**Your Turn:** Print the third-to-last element of your list of activities during quarantine.

{try it}(python3 code/lists/list-basics.py 4)
|||

## Check Your Understanding

{Check It!|assessment}(multiple-choice-3821345628)

{Check It!|assessment}(multiple-choice-759972809)