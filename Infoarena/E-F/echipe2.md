# Teams2

Julieta is the coach of a rather unusual sport. In this sport, there are $N$ functions that a player can perform. Each player is an expert in a specific function and can only occupy that function. Julieta has $2$ players for each function and wants to form two teams that are as balanced as possible. She knows the value of each of the $2 * N$ players (a natural number). The imbalance of a team is defined as the difference between the highest value player in the team and the lowest value player. Julieta also defines the total imbalance as the maximum between the imbalance of the first team and the imbalance of the second team. Because there are so many players on the field, Julieta asks you to find out the minimum total imbalance that can be achieved.

## Input data

The input file `echipe2.in` will contain on the first line the number $N$. The following $N$ lines will each contain two natural numbers representing the values of the players who can occupy the respective function.

## Output data

In the output file `echipe2.out` you will print the minimum total imbalance that can be achieved.

## Constraints and clarifications

$1 \leq N \leq 10^5$

The player values will not exceed $10^9$

## Example

`echipe2.in`

```
5
1 3
5 4
3 4
6 5
4 2
```

`echipe2.out`

```
4
```

## Explanation

One possible solution is (the bold values represent one team and the non-bolded ones the other team):
`1 3`
`5 4`
`3 4`
`6 5`
`4 2`
The imbalance of the bolded team is $4$, and the imbalance of the other team is $3$. The total imbalance is $4$. There may be multiple solutions for forming the teams.