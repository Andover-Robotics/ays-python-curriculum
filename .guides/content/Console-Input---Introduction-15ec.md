## `input()`
`input()` is used to take in data from the user through the **console**. The console is a tool in which you may run your code and communicate with your programs using the keyboard. You will often seen referred to as the *terminal*. For `input()`, you may supply a string inside the parentheses as a prompt, and then the user will be able to type a response in the console. When the user presses enter, their typed message is sent back as the result of the `input()`, and may be stored in a variable, as seen below:

```python
message = input('Leave me a message: ')
print(message)
```

The panel on the right is currently blank. Upon running this code, a new window will appear there with a console. This is where your `print()` statements are sent to and where the user will be able to provide an input. Press the following button to execute the above code in the terminal:

{Try It | terminal}(python3 code/fundamentals/input_demo.py ; read -n 1 -s -r -p "Press any key to exit" ; exit)

Once the command is done, you will see a prompt that says `Press any key to exit`. This is **not a part of the Python itself**, but rather an element of the Codio environment. To open the console again, simply press the button above again.