
In a more or less near future, humans will populate $n$ galaxies, numbered from $1$ to $n$. Due to the development of space transport technology, it is possible to reach any other galaxy from any galaxy through a flight. Each pair of galaxies thus defines a flight that can be traversed in any direction.

At some point, it was decided that $\\frac{n+1}{2}$ transport companies will ensure the free movement of people between existing galaxies. The companies are numbered from $1$ to $\\frac{n+1}{2}$. Each company $x$ will be assigned a set of flights $Z_x$. We denote by $G_x$ the set of galaxies served by company $x$ through the flights in the set $Z_x$. 

The flights will be distributed according to the following rules:
1) through the flights in $Z_x$, company $x$ can transport people between any two galaxies in $G_x$ (either directly, or passing through other galaxies in $G_x$);
2) for any two galaxies in $G_x$, the way company $x$ transports travelers from one galaxy to another is unique;
3) each flight must be assigned to exactly one company.

# Task

Write a program that determines a way to assign the flights to the $\\frac{n+1}{2}$ companies in accordance with the rules stated above.

# Input data

The input file `galax.in` contains a single line that will contain a natural number $n$, representing the number of galaxies.

# Output data

The output file `galax.out` will contain a line for each pair of galaxies. On this line, there will be written $3$ natural numbers $a \ b \ c$, meaning "the flight between galaxies $a$ and $b$ is assigned to company $c$".

# Constraints and clarifications

* $3 < n < 1\ 001$
* $a \ div \ b$ is the integer division of $a$ by $b$.

# Example 1

`galax.in`
```
4
```

`galax.out`
```
1 4 1
1 2 2
4 3 1
3 1 2
3 2 1
2 4 2
```

## Explanation

~[galax.png]

# Example 2

`galax.in`
```
5
```

`galax.out`
```
1 2 1
1 5 3
2 4 1
4 3 1
5 3 1
1 3 2
2 3 2
1 4 3
5 2 2
5 4 2
```

## Explanation

~[galax2.png]
```

I have translated the provided code and also corrected grammar and syntax errors according to the rules of the English language.
