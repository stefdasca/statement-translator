On the island of *Kauai*, located in the village of Hawaii, there are $N$ villages positioned in a straight line, numbered in increasing order starting from $1$: $1, 2, 3, \cdots, N$. In front of each village $i$ ($1 \le i \le N$) there is a signpost which can either be written **R**, meaning that from village $i$ you can reach village $(i+1)$, or **L**, meaning that from village $i$ you can reach village $(i-1)$. It is known that the signpost of village 1 is written with **R**, and the signpost of village $N$ is written with **L**.

Arriving in *Kauai* for $Q$ days, young John and Mary plan to take a trip each day. During each trip, the youths start from different villages, aiming to eventually meet in one of the $N$ villages. Each trip will be represented in the form $(i, j)$ (where $1 \le i, j \le N$ and $i \neq j$).

Interestingly, the two have the ability to replace any number of signposts they encounter along the way and thus follow the new direction; that is, they can replace an encountered **R** signpost with an **L** or an encountered **L** signpost with an **R** and then continue to travel between villages. *Each replacement of a signpost can be carried out if they pay a fee of 1 dollar*. During the trip, due to the heat, the youths can also choose to stay in the villages they find themselves in at any given moment (including the villages they start from), meaning there is no need for them to simultaneously travel between villages throughout the entire route. What is important is that they eventually meet in a village.

# Task

For each of the $Q$ trips, determine the **minimum total cost**, expressed in dollars, that will be paid for the two youths to be able to meet in one of the $N$ villages, possibly after modifying 0 or more signposts in the visited villages.

# Input data

The first line of the input file `excursie.in` contains the non-zero natural number $N$, with the above significance. The next line contains, without any spaces between them, $N$ characters, which can be either '**R**' or '**L**', the $i$-th character representing what is initially written on the signpost at village $i$. The third line contains the non-zero natural number $Q$, representing the number of trips. The next $Q$ lines contain, separated by a space, two natural numbers $i$ and $j$, describing, in order, the trips of the youths, i.e., the villages from which the two start on each of the $Q$ days.

# Output data

The output file `excursie.out` will contain $Q$ lines, with the **minimum total cost** required to perform the trip on day $i$, for each $i$: $1 \le i \le Q$

# Constraints and clarifications
- $2 \le N \le 200\ 000$ and $1 \le Q \le 200\ 000$.
- **The signposts in villages 1 and $N$ cannot be modified**.
- Even if for performing one of the $Q$ trips it is possible to modify the signposts of certain villages, during the night, before the start of the next trip, they will return to their initial state as described in the input file.
- If no signpost needs to be changed for performing a trip, then its (total) cost will be 0 dollars. Also, during a trip, it is allowed that the direction of an encountered signpost be changed multiple times.
- It is possible that for performing a trip there are multiple ways to modify the signposts so that the total cost is minimal.

## Subtask 1 (9 points)
- $|i-j| = 1$, for each of the $Q$ trips

## Subtask 2 (7 points)
- All signposts initially show **R**, except the one for village $N$

## Subtask 3 (6 points)
- All signposts initially show **L**, except the one for village 1

## Subtask 4 (11 points)
- $N \le 200$ and $Q \le 300$

## Subtask 5 (29 points)
- $N,Q \le 3\ 000$

## Subtask 6 (22 points)
- $N,Q \le 70\ 000$

## Subtask 7 (16 points)
- There are no additional restrictions

# Example 1

`excursie.in`
```
7
RRRLLLL
1
2 6
```

`excursie.out`
```
0
```

## Explanation

- On the island there are $N = 7$ villages, and initially, according to the signposts in front of the villages:
    - from village 1 you can reach village 2;
    - from village 2 you can reach village 3;
    - from village 3 you can reach village 4;
    - from village 4 you can reach village 3;
    - from village 5 you can reach village 4;
    - from village 6 you can reach village 5;
    - from village 7 you can reach village 6;
- There will be a single trip ($Q = 1$): John will start from village 2, and Mary from village 6. Without changing any signpost (total cost: 0 dollars), the two can meet, for example, in village 3, following the indications of the encountered signposts. Thus, John will move from village 2 to village 3. Also, Mary will move, starting from village 6, to village 5, then to village 4, and finally to village 3, where she will meet John.

# Example 2

`excursie.in`
```
5
RRLRL
3
1 3
4 1
2 5
```

`excursie.out`
```
0
1
1
```

## Explanation

- For the second trip (4, 1), it is necessary for at least one signpost to be changed, with a cost of 1 dollar. For example, the signpost in front of village 3 can be transformed from **L** to **R**.

# Example 3

`excursie.in`
```
8
RLRRRLRL
4
2 4
1 6
2 8
6 2
```

`excursie.out`
```
1
1
2
1
```

## Explanation

- For the third trip (2, 8), at least two signposts need to be changed, with a total cost of 2 dollars. For example, the signposts in front of villages 2 and 6 can be transformed from **L** to **R**. John and Mary cannot meet if they do not change at least two signposts during this trip.