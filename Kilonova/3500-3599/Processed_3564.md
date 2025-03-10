
~[faleza4.png|align=right|width=20%]

# Task

Little Ion has just graduated from the *Faculty of Geology and Geophysics* and got a job as a cartographer for an important businessman.  

This businessman wishes to develop a beach on the seaside, but he has a limited area of land available to do this.  

Specifically, he has a rectangle with corners $(xStart, yStart), (xFinal, yFinal)$ on the Cartesian plane xOy. $(xStart, yStart)$ represents the bottom-left corner of the rectangle, and $(xFinal, yFinal)$ the top-right corner.

In this rectangle, the sea is determined by a known mathematical equation.

For illustration, consider the polynomial equation $f(x) = k_n \cdot x^n + k_{n-1} \cdot x^{n-1} + \ldots + k_1 \cdot x^1 + k_0$ which describes the sea and which we will particularize below. 

Everything that is ***above*** or on the graph of the function will be on land, and everything that is ***below*** is in the sea. In this context, $x$ represents the ***abscissa*** of a point in these coordinates.

For example, for $f(x) = x^2 - 10 \cdot x + 1$ and the point $(1, 0)$ we have $1 - 10 + 1 = -8 < 0 \Rightarrow$ the point $(1, 0)$ is on land.
Another example, for the point $(10, -2)$ and the same sea we have $100 - 100 + 1 = 1 > -2 \Rightarrow$ the point is in the sea.

~[faleza1.png|align=center|width=40%]

The functions that will describe the sea function are:
* x (for polynomial of degree I);
* x^nr (for x to a specific power);
* sin(...) (for the sine function);
* cos(..) (for the cosine function);
* exp(...) (for the exponential function);
* ln(...) (for the logarithm function);

Each function can be combined with standard mathematical operations (+,-,*,/) and some constants and the syntax will be correct.
For example, 5x, 5*x, x*5*10 will all be valid polynomial functions. Only x5 will not be a valid function.
These constants can also have parentheses, for example (1/2)*x. Also, we can have the '-' sign in case we multiply by a negative number, for example -1*x.
Furthermore, functions can also be combined with standard mathematical operations (+,-,*,/) and with other functions or can be placed as arguments (in parentheses).
There are no spaces in the sea function.

The businessman wants to determine the best possible approximation of the land/sea ratio to develop a beach that will attract as many tourists as possible. Thus, he handed this difficult mission to Little Ion. As poor Ion is not sure where to start solving it, he asks you to help him solve this problem.

However, the businessman is an impatient person, so he also provides a code skeleton. Thus, in the file `help.cpp` you will find a function to calculate the value of a mathematical function at a particular point x, plus other functions that might be useful. Also, in this file, you will find an example of how to use the code skeleton. ***You are NOT*** required to use them, but he thought it might be helpful.

You have to solve the following task: Approximate the land/sea ratio for the entire rectangle. In the constraints and clarifications section, you will find how the sea function can be described.

# Input data

The file `faleza.in` contains on the first line the equation of the sea. The next line contains the coordinates $(xStart, yStart)$ respectively $(xFinal, yFinal)$ marking the large rectangle.  
$(xStart, yStart)$ represents the bottom-left corner, and $(xFinal, yFinal)$ the top-right corner.

# Output data

The file `faleza.out` will contain the approximation of the land/sea ratio of the rectangle.

# Constraints and clarifications

* $xStart$, $xFinal$, $yStart$, $yFinal$ are ***integer*** numbers.  
* $yStart, yFinal \geq 0$;
* $|yFinal - yStart| \cdot |xFinal - xStart| \leq 50$   
* If there is **no land or sea** within a rectangle, the ratio will be equal to $0.00$.  
* The sea function will have at most $300$ characters.
* The sea function will contain only ***integer*** numbers. 
* For $21$ points, the sea function is described by a polynomial of degree I.
* For another $17$ points, the sea function is described by any strict polynomial function;
* For $33$ points, the sea function may contain the $\\sin$, $\\cos$ functions and other combinations with these functions ($\\sin$ of a polynomial, $\\cos$ of a polynomial, $\\sin$ of $\\cos$ etc.)  
* For $29$ points, the sea function may also contain the exponential function $e^x$, the logarithm function, and other combinations of functions ($\\sin$, $\\cos$, polynomials).
* Your approximation must have a relative error less than $0.05$. This error is calculated as follows: 
$$
\\frac{|\\text{your ratio value} - \\text{the theoretical ratio value}|}{|\\text{the theoretical ratio value}|}
$$

* If the response has an error up to $0.1$, you will receive $50\\%$ of the test value.

# Example 1

`faleza.in`
```
x 
0 0 1 1
```

`faleza.out`
```
1.0  
```

## Explanation

The function $f(x) = x$ has the following form in the rectangle $(0, 0)(1, 1)$:

~[faleza2.png|align=center|width=40%]

# Example 2

`faleza.in`
```
sin(x) 
-2 1 -1 2
```

`faleza.out`
```
0.0
```

## Explanation

The function $f(x) = \\sin(x)$ is entirely below the desired rectangle. 

# Example 3

`faleza.in`
```
ln(x) 
1 0 4 2
```

`faleza.out`
```
1.35856
```

## Explanation

The function  $f(x) = \\ln(x)$ looks like this:

~[faleza3.png|align=center|width=40%]
```
