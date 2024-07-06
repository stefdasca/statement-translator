~~Mo și Fo sunt mari chimiști. În laboratorul lor există șase substanțe chimice, numite mofocarburi, care sunt alcătuite pe baza a trei elemente chimice:

* oxygen denoted by $M$
* hydrogen denoted by $F$
* carbon denoted by $C$.

A molecule of mofocarbură is made up of $2$ atoms of one element and one atom of another element. It is observed that there are exactly $6$ such molecules, namely: $M_2F$, $M_2C$, $F_2M$, $F_2C$, $C_2M$, $C_2F$. A chemical reaction will combine a number of molecules from the $6$ mofocarburi and will result in a number of atoms of each element. Here are two examples of correct reactions:

$2M_2F + M_2C + 3F_2M + F_2C + 5C_2M + C_2F \rightarrow 14M + 11F + 14C$
$3M_2F + 5C_2F \rightarrow 6M + 8F + 10C$

So in general a reaction will have the following form:

$x \cdot F_2M + y \cdot C_2M + z \cdot M_2F + u \cdot C_2F + v \cdot M_2C + w \cdot F_2C \rightarrow m \cdot M + f \cdot F + c \cdot C$

where $m=x+y+2z+2v$, $f=2x+z+u+2w$ and $c=2y+2u+v+w$.
Two reactions are considered distinct if they differ by at least one coefficient in the first member, meaning if at least one mofocarbură is used a different number of times in the two reactions.

# Task

Given three natural numbers $m$, $f$, and $c$, calculate the number of distinct reactions that result in $m \cdot M + f \cdot F + c \cdot C$. Since this number can be very large, the result will be displayed modulo $13 \ 131$.

# Input data

The input file `mofocarburi.in` contains on the first line the three natural numbers $m$, $f$, and $c$ separated by a space.

# Output data

The output file `mofocarburi.out` will contain a single number $R$ representing the remainder of the division by $13 \ 131$ of the number of distinct reactions that result in $m$ atoms of oxygen, $f$ atoms of hydrogen, and $c$ atoms of carbon.

# Constraints and clarifications

* $0 \leq m,f,c \leq 100 \ 000$
* The number $m+f+c$ is, for all tests, divisible by $3$.

# Example

`mofocarburi.in`
``` 
2 2 2
```

`mofocarburi.out`
```
3
```

## Explanation

We have $3$ reactions with the result $2M+2F+2C$:

* $M_2F + C_2F \rightarrow 2M + 2F + 2C$
* $C_2M + F_2M \rightarrow 2M + 2F + 2C$
* $M_2C + F_2C \rightarrow 2M + 2F + 2C$

~~