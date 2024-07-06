Given a data structure called [Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree), you need to find the expression and the value of the expression defined in the AST. The tree consists of $N$ nodes.

# Input data

The first line contains $26$ numbers representing the values of the variables (the first number represents the value of the variable $a$, the second $b$, $\\dots$).  
The second line contains a natural number $N$.  
The following $N$ lines contain the description of each node. If line $i$ contains a natural number or a letter of the Latin alphabet, then node $i$ contains a constant or a variable, respectively. Otherwise, line $i$ will contain a string of characters from the set $\\{\\texttt{+}, \\texttt{-}, \\texttt{*}, \\texttt{()}, \\texttt{/}\\}$, followed by a number $k_i$ representing the number of children node $i$ has, followed by a sequence of $k_i$ natural numbers representing the children of node $i$.

# Output data

The first line will contain a string of characters representing the expression defined by the AST, and the second line will contain an integer representing the value of the expression on the line above.

# Constraints and clarifications

* $1 \\leq N \\leq 10^5$;
* It is guaranteed that the result fits in the $\\texttt{long long}$ data type in C++

# Example 1

`stdin`
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
3
+ 2 2 3
1
2
```

`stdout`
```
1+2
3
```

## Explanation

As we know, $1 + 2 = 3$.

~[exemplu1.png|width=250px]

# Example 2


`stdin`
```
3 1 5 6 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
7
() 1 2
+ 2 3 4
a
() 1 5
+ 2 6 7
c
d
```

`stdout`
```
(a+(c+d))
14
```

## Explanation

$(a + (c + d)) \\Leftrightarrow (3 + (5 + 6)) = 14$

~[exemplu2.png|width=350px]

# Example 3

`stdin`
```
1 2 3 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
15
- 2 2 3
250
* 2 4 5
() 1 11
* 2 7 8
* 2 10 9
() 1 6
4
10
d
+ 2 12 13
* 2 14 15
c
a
b
```

`stdout`
```
250-(a*b+c)*(d*10)*4
50
```

## Explanation

$250-(a*b+c)*(d*10)*4 \\Leftrightarrow 250-(1*2+3)*(1*10)*4 = 50 $  
**Note**, node $1$ in the picture below contains the `-` sign, not `+`! It is a mistake.  
~[exemplu3.png|width=500px]