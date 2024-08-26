# Piese3

hceToglA is expanding into the automotive industry, specifically as a parts distributor. Initially, they purchased a warehouse containing a stock of $N$ parts, each part having exactly $C$ assigned codes. Lerogla, the warehouse manager, wants to put things in order right from the start, so she began reorganizing the parts in the warehouse. Reorganization consists of grouping duplicate parts. Two parts $A$ and $B$ are considered duplicates if any of the codes assigned to part $A$ is equal to at least one of the codes assigned to part $B$. Furthermore, if $A$ and $B$ are duplicates, and $B$ and $C$ are duplicates, then implicitly $A$ and $C$ are considered duplicates. All is well, however, after a week of hard work, Lerogla realized that the task is impossible for her, so she needs to turn to her colleagues in the programming department. And something else... Meanwhile, some more warehouses have been bought, so now there are a total of $T$ warehouses, each with the same need for reorganization. We are given $T$ - the number of warehouses. For each warehouse, we are given $N$ - the number of parts, $C$ - the number of codes assigned to each part in that warehouse, then $X_{ij}$ - the codes assigned to part $i$, $1 \leq i \leq N$, $1 \leq j \leq C$. The task is to find the groups of parts sorted in ascending order of part indices ($1 \leq i \leq N$), both within the groups and between the groups (Lerogla is very detail-oriented). For example, if we have the groups (2), (1, 3), (5, 4, 6) they will be displayed in the order: (1, 3), (2), (4, 5, 6). Note: a group is formed from the indices of the parts that compose it, indices with values between $1$ and $N$.

## Input data

The input file `piese3.in` contains on the first line $T$ - the number of warehouses, then the following lines describe the $T$ warehouses as follows: The first line contains $N$ - the number of parts, and $C$ - the number of codes assigned to each part, separated by a space. Each of the following $N$ lines contains $C$ values representing the codes of part $i$, $X_{ij}$, $1 \leq i \leq N$, $1 \leq j \leq C$.

## Output data

In the output file `piese3.out` you need to display for each warehouse, the groups of parts after reorganization, each group on a separate line, in the defined order above. Note: the order is applied within a warehouse, not globally.

## Constraints and clarifications

$1 \leq T \leq 20$

$1 \leq N \leq 50\ 000$

$1 \leq C \leq 10$

$1 \leq X_{ij} \leq 1\ 000\ 000$

In the set of codes of a part, there can be equal values.

## Example

piese3.in               | piese3.out
------------------------|------------------------
`3                      | 
3 3                     | 
1 2 9                   | 
3 4 9                   | 
5 6 7                   | 
4 2                     | 
10 10 11 20 10          | 
5 17 5 5                | 
4 101 102 103 44        | 
4 2                     | 
3 1 6 10 13             | 
21 2 17 20 23           | 
8 7 4 3 1 2             | 
3 1 3 4                 | 
2 1 2 4 5 3`            |