## `input()`
`input()` is used to take in data from the user through the **console**. The console is a textual interface that displays outputs from your program and accepts inputs from the keyboard into your program. You will often see the console referred to as the *terminal* for historical reasons _(maybe your parents know more about them ;))_. For `input()`, you may supply a string inside the parentheses that asks the user for something, and then the user will be able to type a response in the console. When the user presses <kbd>Enter</kbd>, their typed message is sent back as the result of the `input()`, and may be stored in a variable, as seen below:

```python
message = input('Leave me a message: ')
print(message)
```

The panel on the right is currently blank. Upon running this code, a new window will appear there with a console. This is where your `print()` statements are sent to and where the user will be able to provide an input. Press the following button to execute the above code in the terminal:

{Try It | terminal}(python3 code/fundamentals/input_demo.py ; read -n 1 -s -r -p "Press any key to exit" ; exit)

Once the command is done, you will see a prompt that says `Press any key to exit`. This is **not a part of the Python itself**, but rather an element of the Codio environment. To open the console again, simply press the button above again.