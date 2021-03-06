## Reading Numbers From `input()`
As you likely determined from your previous experiments, `input()` always yields a string. So how could you read numbers from the console and then be able to calculate with them? Consider the following code:

```python
user_input = input('What is your favorite whole number? ')
input_number = int(user_input)

print(user_input)
print(input_number)

print(user_input * 5)
print(input_number * 5)
```

What do you think it will do? How do you think `user_input` and `input_number` will act differently?

{Try It | terminal}(python3 code/fundamentals/input_demo_2.py ; read -n 1 -s -r -p "Press any key to exit" ; exit)

Were you right?

## `int()`

The secret to this solution is `int()`, which attempts to interpret the provided string as an **integer**. (that means no decimal points!) This is a process known as **casting**: converting a value of one data type into an equivalent value in another data type. In this case, we are converting from a string to an int. But what if the provided string contains a decimal point or is not a number at all? Try running the code again. What happens when you provide a float, such as `10.5`? What happens when you type a word instead of a number?

{Try It | terminal}(python3 code/fundamentals/input_demo_2.py ; read -n 1 -s -r -p "Press any key to exit" ; exit)

## `float()`
`float()` functions similarly to `int()`, except that it will accept floating-point numbers as well as integers. Let us rewrite the above code to:

```python
user_input = input('What is your favorite number? ')
input_number = float(user_input)

print(user_input)
print(input_number)

print(user_input * 5)
print(input_number * 5)
```

Now, try providing an integer, a decimal number, and a non-numerical string again. Run the program using the button below.

{Try It | terminal}(python3 code/fundamentals/input_demo_3.py ; read -n 1 -s -r -p "Press any key to exit" ; exit)

## `str()`
Now, let us revisit an old problem: adding numbers and strings. With a cast, this has now become possible:

```python
num = 123
text = 'abc'

print(text + str(num))
```

{Try It}(python3 code/fundamentals/input_demo_4.py)

**By passing the number into `str()`, a string form of the number is given**, in this case `'123'`.

## Experiment
Now, try it yourself. Play around in the editor on the left and use the following button to test your code in the console:

{Try It | terminal}(python3 code/fundamentals/input_diy_2.py ; read -n 1 -s -r -p "Press any key to exit" ; exit)

Try to use all the new material from this page.

### Challenges
* Take in two numbers and output their product
* Take in two strings and output them in the opposite order
* Take in a string `s` and a number `num`. Output `s` `num` times (in one line). Can you separate each copy of `s` with a space? (Hint: The concatenation of a space may be required)