Dominic is a renowned alchemist known for his experiments with precious stones. Throughout his career, he has managed to collect $N$ gemstones, which he has numbered from $1$ to $N$. According to his studies, the appearance of each gemstone is characterized by three integers $X$, $Y$, and $Z$ representing its color, clarity, and brightness.

Dominic has discovered a secret method to make a gemstone from his collection acquire the appearance of another gemstone in the collection. However, the method has a weakness, succeeding only if at least one of the values of the first gemstone is equal to at least one of the values of the other gemstone, but it is irrelevant if the property that the two values represent coincides. For example, the gemstone $(1, 3, 4)$ can be transformed into the gemstone $(3, 2, 2)$ because both have one property equal to $3$.

Curious to test his alchemy skills, the Queen chose two stones from the collection numbered $A$ and $B$ and ordered Dominic to make stone $A$ acquire the appearance of stone $B$. Dominic must complete the task by applying successive transformations to stone $A$, changing its properties each time. Since the queen seems a bit impatient, he hopes to succeed using as few transformations as possible. Dominic asks you to find out whether the queen's order can be carried out, and if so, what is the minimum number of transformations required for this.

**Attention!** If the process is possible, the intermediate aspects of stone $A$ until it looks like $B$ will correspond to other stones in the collection.

# Task

The number of tests $T$ is given, and for each test, $N$, $A$, and $B$, and the properties of the $N$ gemstones in Dominic's collection. The task is to determine the minimum number of necessary transformations (if possible).

# Input data

The first line of the input file `nestemate.in` contains $T$, the number of tests. For each test, the first line contains the integer $N$, the second line contains the integers $A$ and $B$, and the next $N$ lines contain three integers $X$, $Y$, and $Z$ describing the gemstones.

# Output data

The output file `nestemate.out` must contain $T$ lines, one for each given test, containing the minimum number of necessary transformations or `−1` if the process cannot be achieved.

# Constraints and clarifications

* $1 \leq T \leq 5$;
* $2 \leq N \leq 100\ 000$;
* $1 \leq A, B \leq N$ and $A \neq B$;
* $1 \leq X, Y, Z \leq 500\ 000$;
* $1 \leq$ The sum of values $N$ from all $T$ tests $\leq 300\ 000$;
* It is guaranteed that at least one transformation is necessary (stones $A$ and $B$ do not have the same appearance).

|# | Points | Constraints |
| - | - | ------------ |
| 1 | 11 | It is guaranteed that if there is a solution, the result can be achieved with exactly one transformation and $N \leq 10$. |
| 2 | 13 | It is guaranteed that if there is a solution, the result can be achieved with a maximum of two transformations and $N \leq 10$. |
| 3 | 16 | It is guaranteed that if there is a solution, the result can be achieved with a maximum of three transformations and $N \leq 10$. |
| 4 | 10 | $N \leq 10$ |
| 5 | 10 | $N \leq 1\ 000$ |
| 6 | 13 | It is guaranteed that a value appears in the configuration of at most $3$ distinct gemstones. |
| 7 | 27 | No additional constraints. |

# Example

`nestemate.in`
```
2
4
1 2
2 1 1
5 3 6
4 3 5
3 2 7
4
1 3
2 1 1
2 2 2
4 3 5
2 2 7
```

`nestemate.out`
```
2
-1
```

## Explanation

For the first test, the gemstone $4$ is used as illustrated in the drawing below to transform stone $1$ into stone $2$.

For the second test, the transformation process cannot be accomplished, so `−1` is printed.

~[nestemate_ex.png|width=45em]

The transformation $(2, 1, 1) \rightarrow (3, 2, 7)$ is valid because $2 \in \{2, 1, 1\} \cap \{3, 2, 7\}$.
The transformation $(3, 2, 7) \rightarrow (5, 3, 6)$ is valid because $3 \in \{3, 2, 7\} \cap \{5, 3, 6\}$.