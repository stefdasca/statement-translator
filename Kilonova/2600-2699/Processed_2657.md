# Task

The computer science teacher needs to correct the papers of $m$ students. The students had to solve $n$ problems in the paper, numbered from $1$ to $n$. Each student solved all the problems, so the teacher has a total of $m \times n$ problems to correct. He notices that taking the papers sequentially and correcting all the problems from the first paper, then all the problems from the second paper, and so on, does not always result in the minimum total correction time. The teacher has the following correction method:
   * All papers will be corrected in $f$ phases ($1 \leq f \leq n$);
   * In each phase $i$, a subset of problems that have not already been corrected, $S_i$, will be chosen. These problems will be corrected in all papers before returning to the first paper;
   * Formally, we choose $S_i \subseteq \lbrace 1, \ldots, n \rbrace$ such that:
     - $S_i \cap S_j = \emptyset, \forall\ i, \ j \in \lbrace 1, \ldots, f \rbrace , \ i \neq j$;
     - $S_1 \cup \ldots \cup S_f = \lbrace1, \ldots, \ n \rbrace$.

At the beginning of correcting each paper, the student's name must be identified, a process that takes exactly $p$ seconds each time, even if the same paper is returned to multiple times.

After beginning the correction of a paper, finding each problem takes $k$ seconds. Correcting the first problem in the chosen subset takes $t_1$ seconds, correcting the second problem takes $t_2$ seconds, and so forth. It is guaranteed that $t_1 < t_2 < \ldots < t_n$. Each time a paper is returned to and correction is resumed with a different subset of problems, the first problem in the subset will again take $t_1$ seconds to correct.

The value of $t_1$ will be given in the input file along with the values $d_0, \ldots , d_{q-1}$, from which the other values in the sequence $t$ will be obtained using the formula: $t_i = t_{i-1} + d_{i \text{ mod } q}, \forall\ i \in \lbrace 2, \ldots , n \rbrace$, where $x \text{ mod } y$ signifies the remainder of the division of $x$ by $y$.

# Task

Determine the minimum time in which the $m$ papers can be corrected.

# Input data

The input file `teze.in` will contain on the first line the numbers $n$, $m$, $p$, and $k$, separated by spaces. The second line contains two values $t_1$ and $q$, separated by a space. The next $q$ lines contain the values $d_0, \ldots, d_{q-1}$.

# Output data

The output file `teze.out` will contain a single number, representing the number of seconds in which the papers can be corrected, modulo $10^9 + 7$.

# Constraints and clarifications

* $1 \leq n \leq 1\ 500\ 000\ 000$
* $1 \leq m, q, k \leq 1\ 000$
* $1 \leq p \leq 10^{10}$
* $1 \leq t_1, d_i \leq 10$

|#| Points |        Constraints                  | 
|-|---------|------------------------------------|
|1|    5    | $n \leq 25$                        |
|2|   10    | $n \leq 50$                        |
|3|   20    | $n \leq 10\ 000$                  |
|4|   30    | $n \leq 10^7$                      |
|5|    7    | $q = 1$                            |
|6|    8    | $q = 2$                            |
|7|   20    | No additional constraints          |

# Example

`teze.in`
```
2 10 5 2
1 1
2
```

`teze.out`
```
130
```

## Explanation

We have two problems in the paper, and $t_1 = 1, t_2 = t_1 + d_0 = 1 + 2 = 3$. If we correct them together, the correction time for each paper will be: $5$ seconds for finding the student's name, $2$ seconds for finding the first problem, $1$ second for correcting the first problem, $2$ seconds for finding the second problem, and $3$ seconds for correcting the second problem, so in total $5 + 2 + 1 + 2 + 3 = 13$ seconds for each of the $10$ papers, meaning $130$ seconds in total.

Another possibility is to correct the first problem in all papers first, then correct the second problem in all papers. For correcting the first problem we have: $5$ seconds starting the correction, $2$ seconds finding the problem, and $1$ second correcting the problem, in total $5 + 2 + 1 = 8$ per paper, meaning $80$ seconds for all papers.

For correcting the second problem, we have exactly the same calculation, resulting in a total of $160$ seconds, hence the first method was more efficient and no better possibility exists.