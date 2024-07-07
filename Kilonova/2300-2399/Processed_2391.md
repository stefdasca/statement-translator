
The pharmaceutical company AB produces substances that fall into two categories: Acids and Bases. It produces $M$ acids and $N$ bases. The acids are numbered from $1$ to $M$, and the bases are numbered from $1$ to $N$. Some acids have an affinity for some bases. If an acid is placed together with a base for which it has an affinity, a very dangerous chemical reaction occurs. Two acids placed together do not cause any reaction, nor do two bases placed together. Each acid $X \\ (1 \\leq X \\leq M)$ has an affinity for each of the bases numbered from $1$ to $B_X$. Acids have an interesting property due to the fact that acid $X \\ (2 \\leq X \\leq M)$ is produced as a result of refining the composition of acid $X-1$. Thus, if acid $X-1$ has an affinity for each base in a set $Q$, then acid $X$ also has an affinity for each of the bases in the set $Q$. In other words, the bases for which acid $X-1$ has an affinity represent a subset of the bases for which acid $X$ has an affinity. This implies the inequality $B_X \\geq B_{X-1}$.

The company has $K$ containers at its disposal, and each of the $M+N$ substances must be stored in one of these containers. Two substances can be stored in the same container provided that they do not react with each other. Storing one of the $M+N$ substances in the $P$-th container involves paying a sum $S_P$. Therefore, for each substance, the corresponding sum for the container in which it is stored must be paid. The total sum paid is equal to the sum of the sums paid for each substance.

# Task
Determine the minimum total sum that AB company must pay to store all the substances, respecting the specified constraints.

# Input data
The first line of the input file `ab.in` contains the integer $T$, representing the number of data sets described below. The first line of each data set contains $3$ integers, separated by a space: $M, N$, and $K$. The next line contains $K$ integers, separated by spaces. The $P$-th of these numbers represents the sum that must be paid if a substance is stored in the $P$-th container. The next line contains the integer $B_1$. The following $M-1$ lines contain, for each acid $X$ from $2$ to $M$, the values $B_X - B_{X-1}$ (the number of "additional" bases for which acid $X$ has an affinity but acid $X-1$ does not).

# Output data
In the output file `ab.out` you will print $T$ lines. The $i$-th of these lines will contain the minimum sum that AB company must pay, considering the information from the $i$-th data set in the input file.

# Constraints and clarifications
* $1 \\leq T \\leq 10$
* $1 \\leq M,N \\leq 30 \\ 000$
* $2 \\leq K \\leq 1 \\ 000$
* $1 \\leq S_P \\leq 1 \\ 000$
* It is possible that no substances are stored in some containers.
* $50 \\%$ of the test files will have all values $M$ and $N$ less than or equal to $2 \\ 500$.

# Example

`ab.in`
```
2
4 5 5
4 3 2 1 97
1
0
0
4
1 30000 2
999 1000
0
```

`ab.out`
```
12
29970999
```

## Explanation

In the case of the first data set, acids $1, 2$ and $3$ have an affinity for base $1$, while acid $4$ has an affinity for all $5$ bases. One way to achieve the total sum of $12$ is the following: acids $1, 2$ and $3$, as well as bases $2, 3, 4$, and $5$ are stored in container $4$, base $1$ is stored in container $3$, and acid $4$ in container $2$. 

In the case of the second data set, acid $1$ has no affinity for any base. All $30 \ 001$ substances are stored in container $1$.
