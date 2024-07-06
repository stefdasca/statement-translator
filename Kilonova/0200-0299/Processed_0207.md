We have $n$ planks with heights $1$, $2$, $3$, ..., $n$. We want to build a fence by placing the planks side by side in a random order. For example, if $n=3$, we can build the fence in $6$ ways:
~[urat.png]

For any type of fence, the absolute differences between the heights of any two neighboring planks in the fence are calculated. The sum of these differences is called the *ugliness degree of the fence*. In the previous example, for $n=3$, it can be observed that fences have an ugliness degree equal to $3$ in $4$ cases and an ugliness degree equal to $2$ in $2$ cases.

# Task
Given the number $n$ of planks, write a program that:
* calculates the maximum ugliness degree that a fence of $n$ planks can have;
* calculates the modulo $543\\ 217$ remainder of the number of fences with the maximum ugliness degree that can be built with the $n$ planks;
* determines a fence with the maximum ugliness degree formed by $n$ planks, in the form of a permutation of order $n$.

# Input data
The file `urat.in` contains on the first line the natural number $n$ representing the number of planks.

# Output data
The file `urat.out` will contain three lines:
* the first line will contain a natural number representing the maximum ugliness degree of a fence formed by $n$ planks;
* the second line will contain a natural number representing the modulo $543\\ 217$ remainder of the number of fences with the maximum ugliness degree that can be built using the $n$ planks;
* the third line will contain $n$ natural numbers, any two consecutive numbers separated by a space, representing, from left to right, the heights of the planks in a fence with the maximum ugliness degree formed with the $n$ planks.

# Constraints and clarifications
* $1 \\lt n \\le 500\\ 000$
* For the first task $20\\%$ of the score is allocated, for the second $60\\%$, and for the third $20\\%$.

# Example

`urat.in`
```
3
```

`urat.out`
```
3
4
1 3 2
```

## Explanation

The maximum ugliness degree is $3$. 
There are $4$ types of fences with the maximum ugliness degree among the $6$ possible cases — see the figure above.
One of the fences with maximum ugliness uses, from left to right, the planks with heights $1$, $3$, $2$ — see the second fence in the figure.