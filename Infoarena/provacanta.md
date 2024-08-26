Provacanta

Doru Muncitoru has started working at a new dishwashing company in Cluj. As the business is doing very well, he has $N$ projects available. For each project, the required time $t_i$ (in days) and the payment $c_i$ for completing the project are known. Additionally, everyone loves Doru Muncitoru, so he has also received $M$ vacation offers, each with a known duration $t_i$ in days and payment $c_i$. As his name suggests, Doru is a hardworking guy who is not very interested in vacations. Instead, Doru is desperate to earn as much money as possible. Unfortunately, he knows that each time he starts a new project, his efficiency decreases, meaning any subsequent project will take one more day to complete. This fatigue accumulates, so after completing $X$ projects, the $(X + 1)$-th project, which would normally take $Y$ days, will now take $X + Y$ days. However, each time he goes on vacation, his efficiency returns to normal. Doru realizes that although vacations might be paid less, it may be worthwhile to rest to regain his efficiency. Doru Muncitoru does not have much time to waste. As he often changes his workplace, he only has $K$ days to earn as much money as possible. Knowing the $N$ projects, $M$ vacation offers, and $K$ days (the number of days available to him), he asks you to determine the maximum amount he can earn.

## Task

## Input data

The input file `provacanta.in` will contain on the first line a natural number $T$, representing the number of tests. The structure of a test is as follows: the first line contains 3 natural numbers $N$, $M$, and $K$. The next $N$ lines contain 2 natural numbers $t_i$, $c_i$ representing the $N$ projects. The next $M$ lines contain 2 natural numbers $t_i$, $c_i$ representing the $M$ vacation offers.

## Output data

The output file `provacanta.out` will contain a single natural number representing the maximum amount of money Doru Muncitoru can earn in the $K$ days available to him.

## Constraints and clarifications

$1 \leq T \leq 5$

$1 \leq N, M \leq 100$

$1 \leq K \leq 1\ 000$ 

$1 \leq t_i \leq K$ 

$1 \leq c_i \leq 1\ 000\ 000$

## Example

`provacanta.in`
```
1
6 4 14
4 18
2 10
1 8
4 18
2 10
1 18
6 18
5 21
6 14
3 9
```

`provacanta.out`
```
74
```