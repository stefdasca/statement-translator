## Task

Santa Claus wanted to conduct an experiment this year, so he gathered $n$ people and lined them up. It is known that during this time of the year, three types of strange events happen.
1 $i$ - person $i$ miraculously befriends person $i + 1$
2 $i$ - person $i$ breaks the friendship with person $i + 1$ (an unexplained behavior)
3 $a$ $b$ - Santa Claus wonders what is the longest chain of friends in the interval $[a, b]$
Santa Claus tried to answer these questions himself but old age has caught up with him. In the end, he is asking you for help.

## Input data

The input file `prieteni2.in` will contain on the first line the number $n$, and on the second line the number $q$. The following $q$ lines will each describe one event.

## Output data

The output file `prieteni2.out` will contain the answers to the type 3 events, each on a separate line.

## Constraints

for 40% of the score
$1 \leq n, q \leq 3000$

for another 30% of the score
$1 \leq n, q \leq 30000$

for another 30% of the score
$1 \leq n, q \leq 200000$

for type 1 events it is guaranteed that 
$1 \leq i < n$
and that $i$ is not friends with $i + 1$

for type 2 events it is guaranteed that 
$1 \leq i < n$
and that $i$ is friends with $i + 1$

for type 3 events it is guaranteed that 
$1 \leq a, b \leq n$

## Example

`prieteni2.in`

```
3 
11 
3 1 3 
1 1 
3 1 3 
3 2 3 
1 2 
3 1 2 
3 1 3 
3 2 3 
2 1 
3 1 3 
2 2 
3 1 2
```

`prieteni2.out`

```
2 
2 
1 
2 
2 
2 
3 
1 
2 
1 
1
```

## Explanation for example 2

2 befriends 3 the longest chain between 1 and 3 is 2-3, with length 2

2 breaks up with 3 the longest chain between 2 and 3 is of length 1 (just 2, or just 3).