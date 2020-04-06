## The Length of a List

The **length** of a list refers to the number of elements in it. You can access the length of a list using the built-in `len` function. For example, `len([4, 1, 9, 2])` has a value of 4.

|||challenge

**Your Turn:** Print the length of your list of activities, using `len` as necessary.

{try it}(python3 code/lists/list-basics.py 1)

|||

|||challenge

**Think:** Print the last element in your list of activities without using a negative index. _This technique will be useful if you move onto another programming language in the future._

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

A list in Python has many built-in functionalities. To perform more interesting operations than change the element at an index, we use these built-in functionalities on existing lists. (You will learn later that these functionalities are defined as functions.) To add an element to the end of a list, use `list.append`. For example, to add 3 to the end of a list named `numbers`, you could write `numbers.append(3)`.

|||challenge

**Your Turn:** Add an element `"learn to code"` to the end of your list of activities on a separate line.

{try it}(python3 code/lists/list-basics.py 4)

|||

### Remove elements

There are two ways to remove elements from a list. If you want the value of the removed element, use `list.pop` and supply the index of the element you want to remove. If you do not want the value of the removed element, use `del list[index]`. For example:

```python
numbers = [1, 4, 7, 2, 8, 3]
print(numbers.pop(1))
# this will print "4", and numbers will become [1, 7, 2, 8, 3]
del numbers[0]
# numbers will become [7, 2, 8, 3]
```

|||challenge

**Your Turn:** Remove any element from your list of activities and print it.

{try it}(python3 code/lists/list-basics.py 5)

|||

### Insert elements

You can manually insert an element into any position in an existing list using the techniques covered above, but that is tedious. Fortunately, `list.insert` enables you to add any element to any valid index. To insert an element `x` into a list `k` such that the element at index `i` after insertion is `x`, you could write `k.insert(i, x)`. To add an element to the front of a list, you could write `k.insert(0, x)`. To add an element to the end of a list, you could write `k.insert(len(k), x)`, which is equivalent to `k.append(x)`. For example:

```python
numbers = [2, 9, 1, 5]
numbers.insert(0, 8)
# numbers is now [8, 2, 9, 1, 5]
numbers.insert(3, 4)
# numbers is now [8, 2, 9, 4, 1, 5], as numbers[3] is 4.
```

|||challenge

**Your Turn:** Move the last element in your list of activities to the front of the list on a separate line, and print the list.

{try it}(python3 code/lists/list-basics.py 6)

|||

```python
my_list = [1, 2, 3]
print(my_list)

my_list[0] = 4
my_list[1] = 5
my_list[2] = 6
print(my_list)
```

{try it}(python3 code/lists/list-basics-2.py 3)

|||challenge
## What happens if you:
* Change an assignment to be `my_list[0] = "hello"`?
* Change an assignment to be `my_list[0] = 5 % 2 > 0`?
* Change an assignment to be `my_list[0] = my_list[2]`?

|||

{try it}(python3 code/lists/list-basics-2.py 4)

{Check It!|assessment}(fill-in-the-blanks-2442920593)

