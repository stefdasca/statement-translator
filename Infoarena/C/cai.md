# Horse Races

Gigel and Ionel each have $N$ horses. They have decided to compete in $N$ races, one by one, between their horses. Each horse will participate in exactly one race, and each race will put face to face 2 horses with different owners. Each horse has a certain speed, and a race is won by the horse with the higher speed. For each victory, Gigel will receive $200$ lei, for each defeat he will have to pay the same amount, and in case of a tie, he will neither pay nor receive anything.

## Task

Knowing that Gigel can decide for each of his horses against which of Ionel's horses they will compete (respecting the competition conditions), help him to obtain as much money as possible from Ionel.

## Input data

The first line of the input file `cai.in` contains $T$, the number of tests. The following lines contain the description of the $T$ tests. Each test begins with a line containing $N$, the number of horses in a camp. The second line contains $N$ integers representing the speeds of Gigel's horses. The third line contains $N$ integers representing the speeds of Ionel's horses.

## Output data

For each test, print in the output file `cai.out` a line that contains a single number, the maximum sum Gigel can obtain, in lei.

## Constraints and clarifications

$$N \leq 1\ 000$$

$$T \leq 20$$

## Example

`cai.in`

```
4
3
92 83 71
95 87 74
2
20 20
20 20
2
20 19
22 18
1
13
20
```

`cai.out`

```
200
0
0
-200
```