
A tango is made up of musical phrases, each of them having $8$ musical beats. The musical beats have the same duration. Just as important as the melody of a tango is the dance associated with it. The movements performed during the dance are called figures. The sequence of figures performed during the dance forms a choreography. Two choreographies are considered different if the sequence of figures that compose them is different. A beautiful choreography associated with a tango has the following characteristic: when a musical phrase ends, a figure must end as well.

$D$ and $S$ are preparing for their first dance competition and they are currently working on the tango choreography. Even though it will be their first competition, they already know $n$ figures and have calculated for each of these figures the number of musical beats it lasts. Because they enjoy dancing together, they want to prepare a beautiful choreography for a piece that lasts exactly $k$ musical beats.

# Task

Determine the number of beautiful choreographies $\\text{mod } 999 \\ 983$ for a piece that: lasts exactly $k$ musical beats, respects the conditions above, and is formed only from the $n$ known figures of $D$ and $S$ (there is very little time left until the competition, so they cannot learn new figures).

# Input data

The first line of the input file `tango.in` contains the natural numbers $n$ and $k$, separated by a single space. The second line contains exactly $n$ numbers separated by a space, representing the lengths of the figures.

# Output data

The output file `tango.out` will contain the number of possible choreographies $\\text{mod } 999 \\ 983$.

# Constraints and clarifications

* $n \\leq 100 \\ 000$
* $k \\leq 2 \\ 000 \\ 000 \\ 000$
* $k$ will always be divisible by $8$
* $1 \\leq$ length of a figure $\\leq 8$
* for $30\\%$ of the tests, there will be a single figure of a certain length
* for $50\\%$ of the tests $n \\leq 30$
* for $70\\%$ of the tests, the lengths of the figures will only be values from the set $\\{2, 4, 6, 8\\}$
* By $a \\text{ mod } b$, we mean the remainder of the division of $a$ by $b$.

# Example

`tango.in`
```
3 16
1 1 8
```

`tango.out`
```
66049
```

## Explanation

There are $16$ musical beats, so a beautiful choreography will be danced to $16 / 8 = 2$ musical phrases.
If we denote the figures with letters, we have figure $A$ of length $1$, figure $B$ of length $1$, and figure $C$ of length $8$. The first musical phrase can be made up of any sequence consisting of eight pieces of $A$ or $B$, hence a total of $2^8 = 256$ possibilities. Another possibility for the first phrase is through a single $C$. Thus, a total of $257$ possibilities. For the second phrase, we have just as many possibilities, so in total, there are $257 \\cdot 257 = 66 \\ 049$ possible beautiful choreographies.
Since $66 \\ 049 \\text{ mod } 999 \\ 983 = 66 \\ 049$, the result is $66 \\ 049$.
