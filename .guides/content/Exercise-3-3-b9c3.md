-----------------------------
Note: This exercise should be done using only the statements and other features we have learned so far.

1.  Write a function that draws a grid like the following:

        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +

    Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

        print('+', '-')

    By default, <span>print</span> advances to the next line, but you can override that behavior and put a space at the end, like this:

        print('+', end=' ')
        print('-')

    The output of these statements is `'+ -'` on the same line. The output from the next print statement would begin on the next line.
    
 {Try It}(python3 code/exercise_3-3.py)

2.  Write a function that draws a similar grid with four rows and four columns.

{Try It}(python3 code/exercise_3-3.py)

{Check It!|assessment}(code-output-compare-591127166)

