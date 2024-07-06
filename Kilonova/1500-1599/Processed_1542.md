In the school where Andrei and Bogdan learn, they know another $N$ students, labeled with numbers $1, 2, \dots , N$. Among these $N$ students, some are friends of Andrei. Some of these $N$ students are enemies of Bogdan. We know both the labels of Andrei's friends and the labels of Bogdan's enemies. The school principal wants to organize a trip that includes Andrei, Bogdan, and $S$ of their acquaintances, such that the group of $S$ students includes at least $K_1$ of Andrei's friends and at most $K_2$ of Bogdan's enemies. To avoid unpleasant events, the principal will choose the $S$ students so that the total number of absences accumulated by them, denoted $Sm$, is minimized.

# Task

Given the values $N, S, K_1, K_2$, the labels of Andrei's friends, the labels of Bogdan's enemies, as well as the number of absences accumulated by each of the $N$ students, determine the value of $Sm$ obtained for a group that meets the above conditions.

# Input data

The input data is read from the text file `grup.in`, with the following structure:
- The first line contains the natural values $N$, $S$, $K_1$, $K_2$, separated by a space, with the meanings from the statement;
- The second line contains the values $a_1, a_2, \dots ,a_N$, separated by a space, representing the number of absences accumulated by each of the $N$ students;
- The third line contains a sequence of $N$ characters from the set $\\{$`0`$,$ `1`$\\}$, **not separated by spaces**. If the $i$-th character in the sequence is the character `1`, then the student with label $i$ is a friend of Andrei;
- The fourth line contains a sequence of $N$ characters from the set $\\{$`0`$,$ `1`$\\}$, **not separated by spaces**. If the $i$-th character in the sequence is the character `1`, then the student with label $i$ is an enemy of Bogdan.

# Output data

The first line of the text file `grup.out` will contain the value $Sm$.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* $1 \leq a_i \leq 1\ 000\ 000\ 000,  \forall i \in \{ 1, 2, \dots, N \}$
* Andrei and Bogdan **are not** part of the group of $S$ selected students.

# Example

`grup.in`
```
7 4 3 2
1 2 3 4 5 6 7
0010110
0011010
```

`grup.out`
```
15
```

## Explanation

The students selected in the group are those with labels $1$, $3$, $5$, $6$.
The total number of absences $Sm = 1+3+5+6 = 15$.
The friends of Andrei selected in the group are $3$, $5$ and $6$.
The enemies of Bogdan selected in the group are $3$ and $6$.