## Iterating Over Lists

Iterating over a list allows you to deal with all of the elements in a list individually. Iterating over the list means to start with the element at index 0, and then progress until you reach the end of the list. A `for` loop is used to iterate over a list.

![Iteration Variable](.guides/images/iterating-list-variable-name.png)

<details><summary>**Number & Numbers**</summary>In the example below, the iteration variable is `number` and the list is named `numbers`. This is a very common practice in Python. The list is always plural, while the iterating variable is the singular of the list name. Python will not throw an error if this convention is not followed. However, `for number in numbers` helps with the readability of your code. You should follow this convention as often as possible.</details>

```python
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)
```

In a few other languages, this pattern is known as "for each". You can think of `for x in s` as "for _each_ element _x_ in list _s_".

|||challenge

**Your Turn:** Make a list of your favorite hobbies, then print each hobby with an exclamation mark (!).

{try it}(python3 code/lists/list-iterate.py 1)

|||

Iterating through a list (also known as **traversing a list**) is the basis for many common computational patterns. For example, you could add up all the numbers in a list.

```python
numbers = [1, 9, 5, 3]
total = 0
for number in numbers:
  total += number
print(total) # the output would be 18
```

|||warning

What if you want to modify the list while iterating through it? Would this work?

```python
numbers = [2, 9, 3]
for num in numbers:
  num += 3
```

**No!** `numbers` is still `[2, 9, 3]`. It is important to remember that the `for ... in` pattern does not allow you to modify the list you are iterating through. To do so, you need to iterate through the valid indexes.

|||

## Iterating Over Indexes

Try the following code segment.

```python
numbers = [9, 8, 4, 5]
for i in range(len(numbers)):
  print(i, numbers[i])
```
{try it}(python3 code/lists/list-iterate.py 2)

This loop uses `range`, a built-in feature that generates arithmetic sequences. In this case, `range(n)` returns a sequence including all integers from 0 (inclusive) to _n_ (exclusive). For example, `range(3)` would be equivalent to `[0, 1, 2]` in iteration.

While the code segment itself doesn't seem very impressive, having the index allows you to **modify** the list being iterated. Try to understand the following example:

```python
words = ['with', 'power', 'comes', 'responsibility']
for i in range(len(words)):
  words[i] += '...'

print(words) # what is the output?
```

## Aborting iteration

If you want to immediately exit the `for` loop, use `break`. For example, try the following:

```python
numbers = [2, 4, 8, 9, 10, 11]
for i in range(len(numbers)):
  if numbers[i] >= 10:
    break
  numbers[i] = -numbers[i]
print(numbers) # what is the output?
```
{try it}(python3 code/lists/list-iterate.py 3)

For each element, this segment checks if the element is greater than or equal to 10. If so, then it immediately exits the loop and reaches the final `print` statement. Otherwise, it negates that element and continues to the next element.

## Check your understanding

You should be able to iterate through a list and modify each element as needed.

{Check It!|assessment}(multiple-choice-1388084939)

{Check It!|assessment}(fill-in-the-blanks-1060157561)

|||challenge

**Think:** Try the following tasks.
* Collect the first letter from each favorite hobby into a string. For example, `["eat", "code", "sleep"]` would result in `"ecs"`.
* Determine the length of your list of favorite hobbies without using `len`.
* Implement the "filter" pattern: populate another list with all favorite hobbies that are shorter than 5 letters.
* Implement the "map" pattern in place: change each favorite hobby to be uppercase and end in an exclamation mark. Check your work with `print`.
* **Challenge:** Implement insertion sort, but not in place. Given `numbers = [9, 3, 2, 7, 1, 5, 6]`, populate another list with the elements from `numbers` sorted smallest to largest. Test your implementation with different inputs. _Hint:_ use `list.insert`. <details><summary>More hints</summary>Insertion sort is based on the idea that the list you are populating is always sorted. Therefore, each step involves finding the right position to insert the next element.</details>

|||

