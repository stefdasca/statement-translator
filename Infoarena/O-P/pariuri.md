# Bets

Since the start time of the game is approaching quickly, PalanRit has started betting because he wants to be an experienced bettor by the time the match between Greece and Romania begins. To gain experience quickly, he has joined a dangerous gang of $N$ people. Each of the $N$ people has a list that contains pairs of the form $(time, money)$ which signify that at time unit $time$ he or she has bet and won or lost an amount of money equivalent to $money$. PalanRit wants to create statistics, namely, he wants to create a list of pairs of the form $(time, sum_money)$ in which to count how much the gang has won or lost at each moment in time when a bet was placed.

## Input data

The input file `pariuri.in` contains on the first line a natural number $N$, representing the number of people in the gang. On the next $N$ lines, the $N$ lists will be described as follows. Each line contains a number $M$, representing the number of elements in the respective list, followed by $M$ pairs of two numbers, $time$ and $money$, with the meaning from the ## Task section. All numbers on a line are separated by a space.

## Output data

In the output file `pariuri.out` you will print on the first line a number $P$ representing the number of elements in PalanRit's list, and on the second line, you will print $P$ pairs of two numbers $time$, $sum_money$, with the meaning that at the time unit $time$, the whole gang has won or lost an amount of money equivalent to $sum_money$.

## Constraints and clarifications

$1 \leq N \leq 100$

$1 \leq M \leq 20 \, 000$

$1 \leq time \leq 10^9$

For $80\%$ of tests $1 \leq time \leq 10^6$

$-10^6 \leq money \leq 10^6$

If $money \geq 0$, then it is considered a win; otherwise, it is considered a loss.

**WARNING!** The order of pairs in the output file does not matter.

## Example

`pariuri.in`

```
3
2 1 10 3 -60
1 3 50
3 1 -5 3 15 2 -5
```

`pariuri.out`

```
3
1 5 2 -5 3 5
```

## Explanation

The first person in the gang bet at times $1$ and $3$, the second person only at time $3$, and the last person at times $1, 2$, and $3$. In conclusion, at time unit $1$ the gang wins $10 - 5 = 5$, at time unit $2$ loses $5$, and at time unit $3$ the gang has a profit of $-60 + 50 + 15 = 5$.