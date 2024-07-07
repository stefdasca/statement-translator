
A mixture of two substances, whose molecules are noted as $0$ and $1$, respectively, is considered. This mixture is represented as a square matrix with $N$ rows and $N$ columns.

To separate the two substances, a series of $K$ magnetic forces are successively applied to the mixture, characterized by the following three quantities:

- the duration of force application, denoted by $d_i$ ($1 \leq i \leq K$), expressed in seconds
- the position of force application, denoted by $p_i$ **{'N', 'S', 'E', 'W'}**, $1 \leq i \leq K$, representing one of the four cardinal points (**North**, **South**, **East**, **West**)
- the type of molecules ($0$ or $1$) upon which the force acts, denoted by $m_i$, $1 \leq i \leq K$. ~[image.png|align=right]

The displacement of the molecules follows these rules:

- molecules move only horizontally when the force is applied from the East or West, or only vertically when the force is applied from the North or South;
- molecules move towards the location where the force is applied, and in one second, a molecule moves at most one position;
- a molecule moves only if there is a molecule of the opposite type in front of it in the direction of movement; otherwise, it stays in its position;
- a force acts on all molecules of the specific type.

# Task

Write a program that determines the mixture matrix obtained after applying the magnetic forces.

For example, if $N = 3$, the molecule matrix is as shown below and $K = 2$ forces, characterized by **1N1** and **2E0**, are applied. The mixture will go through the following stages:

~[image2.png|align=center]

# Input data

The input file `amestec.in` contains on the first line two natural numbers, $N$ and $K$, separated by a space, as described above. Each of the next $N$ lines contains a string of $N$ characters $0$ or $1$. Each of the next $K$ lines contains $3$ values as follows: a natural number $d_i$, a character $p_i$ **('N','S','E','W')**, and a natural number $m_i$, $1 \leq i \leq K$, as described above, without spaces in between.

# Output data

The output file `amestec.out` will contain the final mixture matrix. Each of the $N$ lines of the output file will contain a string of $N$ characters, $0$ or $1$, without spaces in between.

# Constraints and clarifications

* $2 \leq N \leq 100$
* $1 \leq K \leq 100$
* $1 \leq d_i \leq 10^9, 1 \leq i \leq K$

# Example

`amestec.in`
```
3 2
011
101
110
1N1
2E0
```

`amestec.out`
```
111
110
100
```

## Explanation

The molecule matrix has $3$ rows and $3$ columns.
A number of $K=2$ forces are applied, the first with a duration of $1$ second, towards the north, which attracts molecules of type $1$, and the second with a duration of $2$ seconds, towards the east, which attracts molecules of type $0$. After applying the $2$ forces, the molecules rearrange according to the adjacent matrix.
