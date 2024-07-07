
On Mars, $N$ Martians have been discovered, identified by scientists from Earth with numbers ranging from $1$ to $N$. Research has shown that the DNA of any Martian $X$ is formed from the set of prime factors in the decomposition of $X$. For example, $\\text{DNA}(6)=\\{2,3\\}$.

It is known that the Martian with the order number $Y$ inherits from the Martian with the order number $X$ if $\\text{DNA}(X)$ is included in $\\text{DNA}(Y)$, meaning the set of prime factors of $X$ is included in the set of prime factors of $Y$. For example, the Martian $6$ inherits from the Martian $3$ because $\\text{DNA}(3)=\\{3\\}$ is included in $\\text{DNA}(6)=\\{2,3\\}$.

We need to specify that extreme situations can arise where $X$ inherits from $Y$ and $Y$ inherits from $X$, when the two Martians have equal DNAs. This is the case of the Martian $12$ who inherits from $6$ but also $6$ inherits from $12$.

# Task

Create a program that, considering the set of $N$ Martians, determines the number of pairs of Martians $(X, Y)$ for which $Y$ inherits from $X$, where $1 \\leq X \\leq N$ and $1 \\leq Y \\leq N$.

# Input data

The input file `adn.in` contains on the first line the natural number $N$, representing the number of Martians.

# Output data

The output file `adn.out` will contain on the first line the determined number of pairs.

# Constraints and clarifications

* $1 \\leq N \\leq 5 \\cdot 10^6$.
* On the planet Mars, any Martian $X$ inherits from $X$.
* Any Martian inherits from the Martian $1$ because $\\text{DNA}(1)=\\{\\}$, i.e., the empty set, which is considered included in any non-empty set.
* It is guaranteed that the number of determined pairs has at most nine digits.

# Example 1

`adn.in`
```
6
```

`adn.out`
```
16
```

## Explanation

$\\text{DNA}(1)=\\{\\}$, $\\text{DNA}(2)=\\{2\\}$, $\\text{DNA}(3)=\\{3\\}$, $\\text{DNA}(4)=\\{2\\}$, $\\text{DNA}(5)=\\{5\\}$, $\\text{DNA}(6)=\\{2,3\\}$
The determined pairs of Martians are $(1,1)$; $(2,2)$; $(3,3)$; $(4,4)$; $(5,5)$; $(6,6)$; $(4,2)$; $(2,4)$; $(6,2)$; $(6,3)$; $(6,4)$; $(2,1)$; $(3,1)$; $(4,1)$; $(5,1)$; $(6,1)$.

# Example 2

`adn.in`
```
19
```

`adn.out`
```
88
```

# Example 3

`adn.in`
```
38
```

`adn.out`
```
251
```

# Example 4

`adn.in`
```
99
```

`adn.out`
```
961
```
```
