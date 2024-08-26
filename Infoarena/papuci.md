# Slippers

For some time, Ionel has wanted to visit the museum $X$, and today this opportunity has just presented itself. Like any visitor, he will have to follow the museum's regulations, so the guide explains them to him at the entrance. The boy will visit the $N$ rooms of the museum in order, from room $1$ to room $N$. In the first room, he will put on a pair of slippers (the museum owners want to protect the carpets of inestimable value in this way), and in each of the following rooms, he will take off the current pair of slippers and put on another pair, which he will wear only in that room. The slippers are of $26$ types (labeled with the letters from $'a'$ to $'z'$), and each room in the museum has a pair of one of these types. The time it takes for Ionel to take off slippers of type $i$ and put on slippers of type $j$ is given by the element $A[i][j]$ of a square matrix $A$ provided at the entrance to the museum. The boy desires as long a visit in the museum as possible, which is why the guide presents him with the Special Visitors Rule. Ionel receives a list of $K$ pairs $(a, b)$ of rooms. For each of these, he must decide, before starting his visit to the museum, whether to request the reversal of the slippers in room $a$ with those in room $b$ or not. Then he will enjoy the visit and take advantage of the time while changing slippers between two consecutive rooms, asking the guide as many questions as possible.

## Input data

The first line of the input file `papuci.in` will contain the numbers $N$ and $K$ with the above meanings. The second line will contain a string of $N$ lowercase letters of the English alphabet, such that the $i$-th character represents the initial type of slippers in room $i$. The next $26$ lines will contain $26$ natural numbers each, representing the matrix $A$ ($A[i][j]$ = the time Ionel needs to take off slippers of type $i$ and put on slippers of type $j$). Each of the next $K$ lines will contain $2$ numbers $a$ and $b$, $1 \leq a \leq b \leq N$, representing a slipper reversal that Ionel can make between rooms $a$ and $b$ before starting his visit.

## Output data

The first line of the output file `papuci.out` will contain the maximum time obtained by Ionel just from taking off and putting on slippers when moving from one room to another throughout the entire visit.

## Constraints

$1 \leq N, K \leq 100\,000$

The elements of the matrix $A$ are natural numbers less than or equal to $1000$.

The matrix $A$ will not necessarily be symmetric with respect to the main diagonal.

Any room $i$ appears in at most one of the $K$ reversals.

There are no two reversals $(a,b)$ and $(c,d)$, $a \leq b$, $c \leq d$, such that $c > a$, $c < b$, and $b < d$.

## Example

**papuci.in** 
```
6 3
abccba
1 2 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
4 5 6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
2 3 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 6
4 5
4 5
```

**papuci.out**
```
19
```

## Explanation

The maximum time $19$ is obtained by swapping the slippers in rooms $4$ and $5$. Thus, the string of slippers before starting the visit to the museum is `abcbca`.