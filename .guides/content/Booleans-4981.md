# What is a boolean?

Booleans are any value that can only be either `True` or `False`.

Booleans represent a very familiar idea in real life: Yes and No. For example, the statement "I am 15 years old" is either True or False depending on who is talking. This means it's a boolean expression.

|||challenge
# Try This!

Here's another boolean expression: My favorite ice cream flavor is cookie dough. Change the expression so that it is true when you are the one speaking.

(Hint: what's your favorite ice cream flavor?)

|||challenge

#### Applying Booleans to your Programs -- Math Operators

$3 = 4$ is another example of a boolean expression; it is a false statement. 

In programming, when we want to determine whether two numbers are equivalent, we don’t use `=` (because we already use `=` for assigning values to variables.) Instead, we use `==`. This is a very common mistake -- if you find yourself trying to use any kind of equals sign and getting an error, make sure you’re using the right one!

(So the earlier expression, represented in Python, would be `3 == 4`.)

3 > 4 as well as 3 < 4 evaluate to true or false as well. <, >, and `==` are known as **boolean operators.**

You can definitely get more complex with math (`3 + 4 == 7` is a true Boolean expression.)

Equality also applies to strings (`"Hello" == "Hello"` is true, while `"Hello" == "world"` is false.)

In this way, you can start deciding things in your program by comparing the values of variables.

|||challenge
# Try This! - Two Truths and a Lie

Make up two boolean expressions that would evaluate to True, and one that evaluates to False. Print out the values of these three expressions. 

{try it}(python3 code/fundamentals/booleans.py)

|||

{Check It!|assessment}(multiple-choice-4057357606)

