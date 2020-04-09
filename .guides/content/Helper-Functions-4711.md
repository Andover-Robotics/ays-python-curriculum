----------

## Helper Functions

Well written functions are those with a single, specific task. Complex problems will require more than one function for the solution. You don't have to only call functions from your main program -- you can call a function within another function! Helper functions are functions that are called from within other functions. Take, for example, the formula for calculating the area of a circle:
$$A = \pi r^2$$

It would be quite easy to write a Python function to calculate the area of a circle. However, instead of knowing the radius of the circle, you have the X/Y coordinates for a point at the center of the circle and another point on the circle. The distance formula (which is based on the Pythagorean Theorem) can calculate the radius of the circle.
$$\sqrt{(x2 - x1)^2 + (y2 - y1)^2}$$

![Radius](.guides/images/radius.png)

The area function is dependent upon the distance formula. But writing both into one function, while possible, could be a bit confusing and overwhelming. Many programmers would rather split the problem into smaller parts. This is where helper functions come into play. Start by defining a function `radius`. The square root function is included in the `math` module. Be sure to import `math` in your program. Then define a function `area` which calls `radius`. Since `area` requires `radius`, `area` also requires all of the parameters needed for the `radius` function. Finally, print the result of the area of a circle with the points (0, 0) and (4, 4).

```python
import math

def calc_pi():
    """Calculate an approxiate value for pi"""
    return(math.radians(180))

def radius(x1, y1, x2, y2):
    """Distance formula to determine the radius of a circle"""
    return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
  
def area(x1, y1, x2, y2):
    """Area of a circle function"""
    return(calc_pi() * radius(x1, y1, x2, y2)**2)

print(area(0, 0, 4, 4))
```

{try it}(python3 code/functions/helper-functions.py 1)

|||challenge
## Your Turn!

Use the helper functions calc_pi and radius (which are already defined), write a function to find the circumference of a circle given the coordinates for the center and one point on the circle. 

<details><summary>**Solution**</summary>
Here is one possible solution. 
```python
def circumference(x1, y1, x2, y2):
  return radius(x1, y1, x2, y2)*2*calc_pi()
```

</details>

|||

{try it}(python3 code/functions/helper-functions.py 2)

## Inner Functions

Python allows you to declare a function inside another function. Doing this hides the inner function from the main program. In the code below, only the `area` function can call the `radius` function. 

```python
import math
  
def area(x1, y1, x2, y2):
    """Area of a circle function"""
    def radius(x1, y1, x2, y2):
        """Distance formula to determine the radius of a circle"""
        return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    
    return(math.pi * radius(x1, y1, x2, y2)**2)
  
print(area(0, 0, 4, 4))
```

{try it}(python3 code/functions/helper-functions.py 3)

|||challenge
## Inner Function
Make `calc_pi` an inner function of `area` as well.
<details><summary>**Solution**</summary>Here is one possible solution.<img src=".guides/images/pi-inner-function.png" /> </details>

|||

{try it}(python3 code/functions/helper-functions.py 4)

{Check It!|assessment}(multiple-choice-1330281496)
