Revolve

"All roads lead to the park." (Chirescu, 2016) Ionica and Chirescu are very good friends. In their youth, every day they would set out in Bucharest, looking for something to do. Each of them would choose a random starting point and, of course, eventually end up in the park at Piata Unirii, where they would have a glass of warm milk. Their routes were always very specific: each time they chose the shortest path to the park from where they were. Fortunately for them, this was always very simple because the map of Bucharest was connected and had no cycles! (in other words, it was a tree) Since the two are very good friends, whenever one of them arrived at a place where the other was also supposed to arrive, he would wait eagerly, after which they would continue both calmly towards the park. That place could be either the park itself or an intermediary place. Now Ionica and Chirescu are responsible adults. Even today they met at Ionica's residential house in Silicon Valley and reminisce about their memories. They remember $M$ days (out of the many they spent together). They no longer remember the exact location of the park, but for each of those $M$ days, they know the two starting points $a$, $b$, and the point where they meet, noted in our problem as $c$.

## Task

Given the number of intermediary places $N$, the number of days $M$, along with the starting points and meeting place, reconstruct the map of Bucharest from the youth of the two friends. The two know that the solution is not necessarily unique, so they accept the one you like best :). If they recall the days incorrectly (which is very likely), print $-1$. 

## Input data

The input file `revolve.in` will contain on the first line $T$, the number of tests. There will follow $T$ configurations of the type:

$N$ $M$ (number of intermediary locations, respectively the number of days)

$M$ lines, each containing a triplet in the form $a$ $b$ $c$, with the meanings described in the statement

## Output data

For each test, print in the file `revolve.out` (on separate lines, as in the example):

$B$, a natural number indicating the location of the Unirii park $(1 \leq B \leq N)$

$N-1$ lines, each line containing a pair $a$ $b$ with the meaning that there is a direct path from node $a$ to node $b$ $(1 \leq a, b \leq N)$.

If no possible map exists, then print $-1$.

## Constraints and clarifications

$T \leq 25$

$N$, $M \leq 100\ 000$

The sum of all $M$ is less than or equal to $500\ 000$

The sum of all $N$ is less than or equal to $500\ 000$

The displayed construction must respect the conditions in the statement!

In all intermediary locations, there are shops stocked with fresh milk, in case one of the two is impatient and drinks their milk on the way!

## Example

`revolve.in`

```
2 
4 3 
1 2 1 
2 3 1 
3 4 3 
2 2 
1 2 1 
1 2 1 
```

`revolve.out`

```
1 
1 2 
1 3 
3 4 
-1 
```

## Explanation

There are 2 tests. In the first test, a possible solution is that the park is located at node 1, and the other locations as in the output. Even Ionica realizes that in the second test, there is no possible map with the properties described in the statement.