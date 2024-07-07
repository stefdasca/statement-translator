# Task

> “Walking through the city […] I just have to find my way�

MIron, bored with everyday life, decided to go for a walk in his hometown, Deva. It has a tree structure (an undirected, cycle-free, connected graph), consisting of $N$ squares and $N-1$ streets that connect them. MIron wants to choose a square to start his walk from and traverse the longest possible path in the city, without passing through the same square twice (to avoid getting even more bored).

Since MIron is a good friend of the city's mayor, he can ask him to move a street, by removing it from between the squares it currently connects, and adding it between two other squares, in such a way that the tree property of Deva city is maintained.

Knowing that MIron can ask the mayor to move **only one** street, you need to determine the maximum length his path can have.

Since MIron does not know which street to ask to be moved, he wants to find out the maximum length of the path that can be formed for **each** of the $N-1$ possible requests.

# Input data

The input file `plimbare.in` contains:

* The first line contains an integer $N$, representing the number of squares in Deva city.
* The next $N-1$ lines contain the descriptions of the city's streets, each of these lines being formed of two numbers $x$ and $y$ representing that there is a street between squares $x$ and $y$.

# Output data

The output file `plimbare.out` will contain $N-1$ lines. The $i$-th of these lines will contain the length of the maximum path if the $i$-th street from the input file is moved.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq x, y \leq N$
* The length of the path between two squares represents the number of streets that need to be traversed to get from one square to another, without passing through a square multiple times.

# Example

`plimbare.in`
```
5
1 2
1 3
4 3
5 3
```

`plimbare.out`
```
3
4
4
4
```

## Explanation

We can leave the street $(1,2)$ in place, obtaining the path $(2,1,3,4)$.
The street $(1,3)$ can be moved between squares $2$ and $4$, obtaining the path $(1,2,4,3,5)$.
The street $(4,3)$ can be moved between squares $5$ and $4$, obtaining the path $(2,1,3,5,4)$.
The street $(5,3)$ can be moved between squares $4$ and $5$, obtaining the path $(2,1,3,4,5)$.