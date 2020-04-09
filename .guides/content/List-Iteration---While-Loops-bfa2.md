## Iteration with While Loops

As opposed to a `for` loop, a `while` loop executes its body repeatedly until a certain condition is no longer true. Consider the following example, which prints all integers from 1 to 10 (inclusive):

```python
number = 1
while number < 11:
  print(number)
  number += 1
```

This example repetitively prints the value of `number` and increments it by one until the number reaches 11, in which case the loop is no longer executed. More formally, the `while` loop above can be understood as the following:

```text
set number to 1
section "loop" begins
if number is less than 11:
  print the number
  increase the number by one
  go to the beginning of section "loop"
```

This segment shows that you can think of a `while` loop as an `if` statement that repeats itself until its condition is no longer true. (In fact, code starts to read like this as you strip away the nice features found in structured programming.)

For loops are almost exclusively used to iterate over lists. It is possible to use a while loop with an index counter. The index is initially set to zero and incremented at the end of each loop iteration. The loop ends when the index reaches the length of the list.

```python
numbers = [1, 2, 3, 4]
length = len(numbers)

i = 0
while i < length:
    print(numbers[i])
    i += 1
```

|||challenge

**Your Turn:** Make a list of four of your favorite foods (or any other category). Then, use a `while` loop to print each element in the list from the last to the first, i.e. in reverse order. Make sure that all elements are printed.

{try it}(python3 code/lists/list-while-loop.py 2)

|||

## Check your understanding

{Check It!|assessment}(multiple-choice-4064533170)

{Check It!|assessment}(multiple-choice-2355929832)
