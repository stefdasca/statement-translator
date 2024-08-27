TVShow

In a television show, $N$ contestants participate in a life-and-death competition from which only one of them can emerge as the winner. Each contestant has accumulated a certain number of points, $S_i$, throughout the show and now faces the final round. Each of them must choose one of the two gates before them. Only one of these gates hides the grand prize behind it. Additionally, each contestant bets a number of points $P_i$ $(0 \leq P_i \leq S_i)$. If the gate they chose is the one hiding the prize, their score will be $S_i + P_i$, but if they did not choose correctly, their score will be $S_i - P_i$. The contestant with the highest score after this round will win the grand prize. If there are multiple highest scores, no one will win. The last contestant, none other than Petrica, faces a very difficult decision: he knows the scores of the other contestants and the number of points each has wagered, but he does not know which gates they chose. However, he knows that every contestant—including himself—has a $50\%$ chance of guessing the winning gate and a $50\%$ chance of not guessing it. He must decide the number of points to bet in order to maximize his probability of winning (even if for two ways of betting the probabilities are very close, practically negligible, Petrica will choose the way with the higher winning probability).

## Task

Calculate the number of points Petrica should bet to have the maximum chances of winning. If there are multiple solutions, choose the smallest one. Also, calculate the maximum probability of winning that Petrica can have.

## Input data

The input file `tvshow.in` will contain on the first line the integer $N$ representing the number of contestants in the competition. Each of the next $N - 1$ lines will contain two integers separated by a space representing the score and the number of points bet by each of the first $N - 1$ contestants. The last line contains a single integer representing Petrica's score.

## Output data

The first line of the output file `tvshow.out` will contain the number of points bet by Petrica. On the next two lines, there will be two integers $A$ and $B$ that represent Petrica's maximum winning probability in the form of an irreducible fraction (the probability is equal to $A/B$).

## Constraints and clarifications

$1 < N < 301$  
The score values are integers in the interval $[0, 30000]$  
For $40\%$ of the tests $N \leq 17$  

## Examples

`tvshow.in`

```
3
100 25
100 75
100
```

`tvshow.out`

```
76
1
2
```

`tvshow.in`

```
10
3 2
0 0
1 3
5 0
31 60
41 10
10 1
8
```

## Explanations

For the first example, the probability that Petrica will win is $50\%$ if he chooses to bet $76$ points, regardless of whether the first two contestants guessed correctly or not the winning gate. If Petrica guessed the winning gate, he will win the contest (accumulating $176$ points), and if he did not guess, he will certainly lose (accumulating $24$ points). If he bets less than $76$ points, the probability of winning will be lower, and if he bets more, the probability will remain the same. For the second example, Petrica loses no matter what amount he bets. In the third example, if Petrica bets $10$ points, he has a $12.5\%$ chance to win (he wins only if the first two contestants do not guess the gate and he does; in all other cases, Petrica will lose). If he bets less, Petrica will have $0\%$ chances of winning.