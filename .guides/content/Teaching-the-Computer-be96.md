# Computer Programming in a Nutshell
**In essence, computer programming is all about telling a computer what to do and how to do it.** The instructions you write for computers is expressed in **code**, which both you and the computer understand. In this course, you will express this code in a programming language called **Python**.

All human and programming languages have a set of **grammar rules**. However, unlike human languages, these grammar rules are much more strict in programming languages. **Syntax** refers to the arrangement of words, symbols and punctuation in a language, and each language has its own way of expressing something. We will come back to syntax later.

In this course, we teach both **programming concepts** and **how to write them in Python**, so that you can interact with your computer as we move along and be productive after this course. **Our highest priority is to ensure that you understand the concepts**—whether you can memorize how to write them in Python is less important.

In fact, here is our homemade cheat sheet for this course (literally). We recommend that you print out this cheatsheet so that you are free to reference it as we move along. Rest assured that after enough practice and application, you will gradually stop having to rely on this cheatsheet to write programs.

[Download Cheatsheet (.pdf)](https://drive.google.com/file/d/1EEFtUBSWycHq-Qv2kwkuzBDZU9v5h-B_/view?usp=sharing)

## Computers as Calculators

Simply said: **Your computer is a glorified calculator.** Both accept inputs from you and show the result of their calculations on a screen. **The underlying principles are the same—both operate on numbers, which can represent anything from cute pet photos to English prose.** They turn inputs from you and the Internet into useful output, and your programs will do the same.

Stanford University's CS101 course (Introduction to Computing Principles) presents the **Fundamental Equation of Computers**:

> # $\text{Computer} = \text{Powerful} + \text{Stupid}$

* $\text{Powerful}$ in that computers can process big data sets with billions of operations per second
* $\text{Stupid}$ in that their instructions are simple and mechanical, as you will soon find out

## Computer Pedagogy

As a programmer, your job is to describe what you want the computer to do in a simple, unambiguous, and technical way. Like teaching someone to tie their shoes and writing a recipe, **writing a program involves breaking the procedure down into step-by-step instructions.** Consider the following procedure for a calculator:

1. Accept user input on the numpad.
2. If the user presses a digit, add that digit to the end of the current number.
3. If the user presses an operator (like $+$), keep track of that operator, store the current number in memory, and then reset the current number to 0.
4. If the user presses the equal sign ($=$), apply the operator that we are keeping track of to the stored number and the current number, then set the current number to the result.
5. Go back to step 1.

Semantically, the programs you write in Python will sound a lot like this procedure. It is mechanical and detail-oriented, but **when we combine many operations like these and build on top of them, we can start making computers _seem_ "smart".** That is your challenge, and this course will walk you through the steps necessary to conquer it.

_Are you ready?_