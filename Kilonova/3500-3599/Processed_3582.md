
~[stars.jpg|align=right|width=30em]

We are on Earth. We know from geography classes that our planet consists of water areas and land areas. Being programmers, we will simplify this world to a matrix.

Let matrix $A$ be a binary matrix with $N$ rows and $M$ columns, where:

* $0$ represents a water area,
* $1$ represents a land area.

An **island** is a group of $1$ cells connected through any of the $8$ directions (North, South, East, West, Northwest, Northeast, Southwest, Southeast). We know the total number of islands on Earth, which is $K$ in total. Similarly, a lake, river, sea, or ocean is a group of $0$ cells connected through the same $8$ directions. For simplicity, we will refer to these areas as lakes.

On Earth, there are two lovers, Răzvan and Andreea. They are on different islands, so Răzvan sets out on an expedition to reach his other half. Crossing water is dangerous, so Răzvan will move only during the day. More precisely:

* During the day he can cross lakes.
* During the night he must stop on an island.

Each island has a known number of **stars** visible in the sky **at night**. Andreea adores them, so Răzvan will bring her as many as possible. Every time he arrives on an island, he will collect **all** the visible stars there, and that island will not have stars if Răzvan returns later. Once he reaches Andreea, his journey stops and he gives her all the stars gathered until that moment.

We have $Q$ queries in the form: $R_x, R_y, A_x, A_y$. 

For each query, we need to determine:
What is the maximum number of stars that Răzvan can collect starting from the island where he is located, which includes the coordinates $(R_x, R_y)$, up to Andreea's island, the island that includes the coordinates $(A_x, A_y)$?

# Input data

The first line of the input file `stars.in` contains four integers, $N, M, Q$ and $K$, with the meaning described in the statement.
The next $N$ lines contain $M$ digits each, representing the values of the binary matrix $A$.
On line $N+2$ there are $K$ integers, each indicating the number of stars on one island on Earth.
Starting from line $N+3$, there are $Q$ lines, each containing four integers: $R_x, R_y, A_x$ and $A_y$, representing the coordinates of the lovers.

# Output data

For each query, print on a separate line in the file `stars.out` the maximum number of stars that Răzvan can collect for Andreea.

# Constraints and clarifications

* $3 \leq N \cdot M \leq 1 \ 000 \ 000$
* $1 \leq Q \leq 200 \ 000$
* $2 \leq K \leq 50 \ 000$. It is guaranteed that there are $K$ islands on Earth.
* $3 \leq$ number of islands and lakes $\leq 100 \ 001$
* $1 \leq$ number of stars on an island $\leq 1 \ 000$
* If we have reached Andreea's island, we will collect all the stars from her island and then give her all the stars collected until that moment.
* To identify the islands and determine the number of stars on each of them, we will assign each island its minimum coordinate in lexicographical order. Thus, the first island will be the one with the smallest coordinate in lexicographical order, and the second island will be the one with the second smallest coordinate in lexicographical order, and so on.

|#|Points|Constraints|
|-|-|-|
|1|10|There is only one lake on the entire map|
|2|15|$N=1$ or $M=1$|
|3|30|$2 \leq K \leq 5 \ 000$, $1 \leq Q \leq 1 \ 000$ and $3 \leq$ number of islands and lakes $\leq 10 \ 001$|
|4|45|No additional constraints|

# Example 1

`stars.in`

```
7 9 3 4
0 1 1 0 1 0 0 0 0 
1 1 1 1 0 1 1 0 0 
0 1 0 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 0 
0 1 0 1 0 1 1 0 0 
1 0 0 1 0 1 1 1 0 
1 0 1 0 0 0 0 1 1 
1 5 3 7
2 4 5 2
5 4 3 9
6 1 7 9
```

`stars.out`

```
16
16
16
```

## Explanation

$$
\LARGE{\textcolor{violet}{0} \textcolor{EB5B00}{1 1} \textcolor{blue}{0} \textcolor{EB5B00}{1} \textcolor{blue}{0 0 0 0}} \newline
\textcolor{EB5B00}{1 1 1 1} \textcolor{blue}{0} \textcolor{EB5B00}{1 1} \textcolor{blue}{0 0} \newline
\textcolor{5CB338}{0} \textcolor{EB5B00}{1} \textcolor{5CB338}{0} \textcolor{EB5B00}{1 1 1 1 1 1} \newline
\textcolor{5CB338}{0 0 0 0 0 0 0 0 0} \newline
\textcolor{5CB338}{0} \textcolor{brown}{1} \textcolor{5CB338}{0} \textcolor{red}{1} \textcolor{5CB338}{0} \textcolor{gray}{1 1} \textcolor{5CB338}{0 0} \newline
\textcolor{brown}{1} \textcolor{5CB338}{0 0} \textcolor{red}{1} \textcolor{5CB338}{0} \textcolor{gray}{1 1 1} \textcolor{5CB338}{0} \newline
\textcolor{brown}{1} \textcolor{5CB338}{0} \textcolor{red}{1} \textcolor{5CB338}{0 0 0 0} \textcolor{gray}{1 1} \newline
$$

In the adjacent figure, islands and lakes have been highlighted. There are $4$ islands and $3$ lakes. If we want to solve the last query, a correct answer would be to start from the brown island, which is also Răzvan's island, then go to the red island, then to the orange island, and the last island we should enter will be the gray one, Andreea's island.

# Example 2

`stars.in`

```
9 9 3 3
1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 1
1 0 1 1 1 1 1 0 1 
1 0 1 0 0 0 1 0 1
1 0 1 0 1 0 1 0 1
1 0 1 0 0 0 1 0 1
1 0 1 1 1 1 1 0 1
1 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1
1 2 3
1 1 3 3
5 5 5 3
1 1 5 5
```

`stars.out`

```
3
5
6
```
