## The Length of a List

The **length** of a list refers to the number of elements in it. You can access the length of a list using the built-in `len` function. For example, `len([4, 1, 9, 2])` has a value of 4.

```python
acts = ['write', 'read', 'listen', 'speak']
print(len(acts)) # output is 4, as there are four elements
```

|||challenge

**Your Turn:** Print the length of your list of activities using `len`.

{try it}(python3 code/lists/list-basics.py 1)

|||

|||challenge

**Think:** Print the last element in your list of activities without using a negative index. _This technique will be useful if you move onto another programming language in the future._

<details><summary>Hint</summary>Use the `len` function to get the index of the last element. Remember that indexes start at 0!</details>

{try it}(python3 code/lists/list-basics.py 2)

|||

## Manipulating a List

<!-- What might you want to do to a list? You might want to add elements to the end, insert elements at the front, remove an element at an index, merge two lists, and check if an item exists in the list. All of these operations are easy to achieve with Python. -->

### Change elements

You can use the assignment operator (`=`) to change the value of an element. Be sure to reference the element with the appropriate index. For example, to change the first element of `numbers` to 0, you could write `numbers[0] = 0`.

|||challenge

**Your Turn:** Change the last element of your list of activities on a separate line.

{try it}(python3 code/lists/list-basics.py 3)

|||

### Add elements

A list in Python has many built-in functionalities. To perform more interesting operations than change the element at an index, we use these built-in functionalities on existing lists. (You will learn later that these functionalities are defined as functions.) To add an element to the end of a list, use `.append`. For example, to add 3 to the end of a list named `numbers`, you could write `numbers.append(3)`.

|||challenge

**Your Turn:** Add an element `"learn to code"` to the end of your list of activities on a separate line.

{try it}(python3 code/lists/list-basics.py 4)

|||

### Remove elements

If you want the value of the removed element, use `list.pop` and supply the index of the element you want to remove. For example:

```python
numbers = [1, 4, 7, 2, 8, 3]
print(numbers.pop(1))
# this will print "4", and numbers will become [1, 7, 2, 8, 3]
```

|||challenge

**Your Turn:** Remove any element from your list of activities and print it.

{try it}(python3 code/lists/list-basics.py 5)

|||

### Insert elements

You can manually insert an element into any position in an existing list using the techniques covered above, but that is tedious. Fortunately, `.insert` enables you to add any element to any valid index. To insert an element `x` into a list `k` such that the element at index `i` after insertion is `x`, you could write `k.insert(i, x)`. To add an element to the front of a list, you could write `k.insert(0, x)`. To add an element to the end of a list, you could write `k.insert(len(k), x)`, which is equivalent to `k.append(x)`. For example:

```python
daft = ['faster', 'stronger']
daft.insert(0, 'harder')
# daft is now ['harder', 'faster', 'stronger']
daft.insert(1, 'better')
# daft is now ['harder', 'better', 'faster', 'stronger'], and is thus perfect :P
```

|||challenge

**Your Turn:** Move the last element in your list of activities to the front of the list on a separate line, and print the list.

<details><summary>Hint</summary>This requires two operations: (1) removing the last element, and (2) inserting that element to the front of the list. Use `pop` and `insert`.</details>

{try it}(python3 code/lists/list-basics.py 6)

|||

### Combine lists

In Python, you can use the addition operator (`+`) between two lists in order to combine them. For example, `[1, 9, 3] + [8, 2, 4]` is equal to `[1, 9, 3, 8, 2, 4]`. 

## _How do I do this_?

If it is generic enough, Python probably has you covered with their many list functionalities, which are officially documented [here](https://docs.python.org/3/tutorial/datastructures.html). Feel free to browse through the documentation to find built-in solutions. If you want to find the index of a given element in a list, for example, Python has you covered with `.index(...)`.

## Check your understanding

By now, you should know how to get the length of a list, add elements, remove elements, change elements, and combine lists.

{Check It!|assessment}(fill-in-the-blanks-1796257491)

{Check It!|assessment}(fill-in-the-blanks-2837205768)