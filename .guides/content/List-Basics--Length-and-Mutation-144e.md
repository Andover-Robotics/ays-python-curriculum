## The Length of a List

The **length** of a list refers to the number of elements in it. You can access the length of a list using the built-in `len` function. For example, `len([4, 1, 9, 2])` has a value of 4.

|||challenge

**Your Turn:** Print the length of your list of activities, using `len` as necessary.

{try it}(python3 code/lists/list-basics.py 1)

|||

|||challenge

**Think:** Print the last element in your list of activities without using a negative index. _This skill will be useful if you move onto another programming language in the future._

{try it}(python3 code/lists/list-basics.py 2)

|||

## Manipulating a List

What might you want to do to a list? You might want to add elements to the end, insert elements at the front, remove an element at an index, merge two lists, and check if an item exists in the list. All of these operations are easy to achieve with Python.

### Change elements


### Add elements


You can use the assignment operator (`=`) to change the value of an element. Be sure the reference the element with the appropriate index.

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

