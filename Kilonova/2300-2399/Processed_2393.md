Here's the translated text, following the provided guidelines:

---

A group of $N$ business people met on the occasion of a conference. Some of them are enemies, others are not (friendship is rarely a consideration when it comes to business). Each of them has a bank account with a certain amount of money expressed in euros. Whenever they meet, they think about how to initiate a new business. This time they decided to establish a company, in which a part of them will be shareholders, such that any two business people who are shareholders in the company are not enemies, and the company's capital (equal to the total amounts in the shareholders' accounts) is maximized. To determine the shareholders of this company, they have hired you, and if you provide the answer in due time, you will be rewarded with a handsome sum.

Before you start working, the $N$ business people have provided you with information about their bank accounts and the enmity relationships between them. Analyzing the problem, you concluded that the enmity relationships can be represented as an undirected graph with $N$ vertices (corresponding to the $N$ business people); there is an edge between two different vertices if the corresponding business people are enemies (enmity is mutual). The graph has a special structure, more precisely it is a **chordal graph**. A graph is called a **chordal graph** if it meets one of the following $2$ conditions:
1. It is a graph with a single node.
2. It is obtained by inserting a new node $X$ into a chordal graph $G$, as follows: a subset of nodes from $G$ is chosen, with the property that there is an edge between any two nodes in the subset (the subset can contain just a single node), and an edge is introduced between the new node $X$ and each node in the subset.
~[img1.png]

An equivalent definition of chordal graphs is the following: a graph is called a **chordal graph** if it is connected and any elementary cycle (which contains each node of the graph at most once) having at least $4$ nodes contains at least one “chord” (an edge between two nodes that are part of the cycle but are not adjacent on the cycle). Here are some examples of chordal and non-chordal graphs:
~[img2.png]

# Input data
The first line of the input file `soc.in` contains the integers: $N$ and $M$, separated by a space. The next line contains the integers $E_i,i=1,2,..,N$, separated by a space, representing the amounts in the accounts of the $N$ business people. The number EK represents the amount in the account of the business person numbered $K$. The next $M$ lines contain two integers $a$ and $b$ from the interval $[1,N]$, with the meaning that the business people numbered with $a$ and respectively $b$ are enemies.

# Output data
In the file `soc.out` you will display, on the first line, the maximum capital of the company. On the next line, display the number $A$, representing the number of shareholders of the company. On the third line, display the numbers of the business people who will be shareholders, separated by a space. If there are multiple ways to choose the shareholders of the company such that its capital is maximized, you can display any of them. The numbers of the business people can be displayed in any order (not necessarily in increasing order).

# Constraints and clarifications

* $2 \leq N \leq 256$
* $1 \leq M \leq \frac{N \cdot (N-1)}{2}$
* $1 \leq E_i \leq 1 \ 000 \ 000$, for $i=1,2,..,N$
* If you determine only the maximum capital of the company but not its shareholders, you will receive $60 \%$ of the points corresponding to the respective test.
* For $20 \%$ of the test files, $M=N-1$
* For $60 \%$ of the test files, each biconnected component of the given graph will contain at most $15$ nodes

# Example

`soc.in`
```
16 31
4 4 4 3 1 5 5 3 2 3 1 1 3 5 4 4
1 3
1 8
1 9
1 10
2 4
2 7
2 13
3 4
3 7
3 8
3 9
3 10
3 13
3 16
4 7
4 13
5 6
5 7
5 15
6 7
6 15
7 11
7 13
7 15
8 9
9 10
10 12
10 14
10 16
11 15
12 14
```
`soc.out`
```
23
6 
1 2 6 11 14 16
```

