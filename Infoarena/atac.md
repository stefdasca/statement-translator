## Task

In the country Arboreea, things have gotten out of control. OTPB (Petrica Bomb Organization) has decided to attack two cities in this country because the organization's leader, Petrica, lost the presidential elections in the year $2004$. The country has $N$ cities, numbered from $1$ to $N$, and the network of cities and streets between them form a tree (an undirected connected graph that does not contain cycles). OTPB knows for each street how many bombs are required to dismantle it. The problem now is to determine the smallest number of bombs OTPB needs to use so that there is no longer a path between the two chosen cities (considered of major importance in Arboreea) after the bombing. Since the importance of the cities changes during the evolution of the country, OTPB wants to know the minimum number of bombs for the attack on several pairs of cities, more precisely $M$. However, easy communication of these $M$ pairs between terrorist organizations in the country is desired. Thus, the entire list of the $M$ pairs of cities upon which an attack is desired cannot be transmitted because the connection network between organizations is quite slow at transmitting data. Nevertheless, a solution was found: knowing the first pair of cities $X$ and $Y$ upon which an attack will be carried out and the minimum number of bombs $Z$ that must be used in the case of the attack on the cities $X$ and $Y$, the next pair of cities, the second one, is determined using the relations:

$$X' = (X \cdot A + Y \cdot B) \bmod N + 1$$
$$Y' = (Y \cdot C + Z \cdot D) \bmod N + 1$$

The third pair of cities is determined using the second pair and the minimum number of bombs that must be used to attack it, the fourth pair from the third, and so on. Therefore, it is sufficient to know the first pair of cities and the numbers $A$, $B$, $C$, $D$ to determine all $M$ pairs. Also, for the same reason - slow data transmission - OTPB wants to know the results only for the last $P$ pairs of cities, which are considered sufficient to check the correctness of your program.

Write a program for Petrica's organization that calculates the minimum number of bombs for the attack on the last $P$ pairs of cities from the $M$ pairs if you want to stay alive!

## Input data

The first line of the file `atac.in` contains three numbers representing the number of cities, the number of pairs of cities for which the organization wants to know the minimum number of bombs in case of an attack on them, and the number $P$ of pairs for which your program must display the answer. The next $N-1$ lines contain two natural numbers $U$, $V$ with the meaning: there is a street from city $U$ to city $i$ ($i$ is the line index which will take values from $2$ to $N$) for which OTPB must use $V$ bombs to dismantle it. The next line contains $6$ numbers $X$, $Y$, $A$, $B$, $C$, $D$ with the meaning from the statement.

## Output data

The file `atac.out` will have $P$ lines representing the minimum number of bombs that must be used to attack the last $P$ pairs of cities.

## Constraints and clarifications

$1 \leq N \leq 32000$

$0 < P < M \leq 500000$

$P \leq 10000$

$0 \leq A, B, C, D \leq 10000$

the number of bombs to take a street out of use is a natural number less than $100000$

OTPB will not take any street out of use; the terrain is being probed and nothing more, for now; so for each pair of cities from the $M$ pairs, it is considered that the street network is intact (no street is bombed).

Points on a test will be awarded only if all $P$ numbers in the output file are correctly found.

It is clear that to correctly find the $P$ numbers you have to calculate the minimum number of bombs for all $M$ pairs of cities.

Do not rely on the fact that the pairs of cities will repeat and the set of distinct pairs is small!

OTPB wants to study as many pairs of cities as possible so the numbers $A$, $B$, $C$, $D$ will be intelligently chosen to generate as many distinct pairs as possible among the $M$.

If $X$ coincides with $Y$ then the answer is $0$.

For $40\%$ of the tests $N$ will be less than or equal to $1000$.

## Example

`atac.in`   
$$
7 \\
3 \\
2 \\
1 \\
1 \\
2 \\
2 \\
2 \\
1 \\
3 \\
5 \\
3 \\
5 \\
2 \\
6 \\
7 \\
1 \\
1 \\
1 \\
1 \\
1 \\
1 \\
$$

`atac.out`   
$$
3 \\
5 \\
$$