## Reexamining `print()`

Why did our printed messages have to be surrounded by single quotes (`'`)? Well, what happens if we try to print without the quotes?

```python
print(Hello World!)
```

{Try It}(python3 code/fundamentals/string_basics_demo.py)

Do you see the line `SyntaxError: invalid syntax`? This is called a **Syntax Error**, an error in the source code of a program. Think of a Syntax Error like a grammatical error, but for code. They are most often caused by missing or extra symbols (such as `'` and `)`), and will prevent your code from running.

So why did this code have a Syntax Error?

Well, consider the point of view of the compiler, the program that reads through your code and converts it into language that your computer. When the compiler sees `print`, `Hello`, and `World!`, how does it know what is your message and what is not? This is the role of syntax. When you surround `Hello World!` with single quotes, you form what is called a **string**, data stored in the form of text. When a set of characters are surrounded by `'`s, the compiler knows that everything between the `'`s is a part of the string and not code that must be interpreted and executed.