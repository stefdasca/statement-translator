## Task

Georgel is playing Hearthstone, a game with minions. Each minion is characterized by a pair $(A_i, D_i)$, which means the minion has $A_i$ attack points and $D_i$ defensive points. If two minions $(A_i, D_i)$ and $(A_j, D_j)$ fight, after the fight they will become $(A_i, D_i - A_j)$ and $(A_j, D_j - A_i)$. In other words, each minion reduces the other's defensive points by its own attack value. A minion dies if its defensive points become less than or equal to $0$. Georgel has one minion with points $(ga, gd)$ and the computer has $N$ minions. It is Georgel's turn to attack. His minion can attack multiple times, even attacking the same opposing minion. Furthermore, after killing an opposing minion, both its attack and defensive points increase by $1$. Help Georgel by telling him the maximum number of opposing minions he can kill without his minion dying.

## Input data

The input file `hsattack.in` will contain on the first line an integer $T$ representing the number of tests. Each test has the following format:
- the first line contains two integers $ga$ and $gd$, representing the attack and defensive points of Georgel's minion;
- the second line contains $N$, the number of opposing minions;
- each of the following $N$ lines contains two integers $A_i$ and $D_i$, representing the attack and defensive points of the $i$-th opposing minion.

## Output data

The output file `hsattack.out` will contain the answers for the $T$ tests. The answer for a test consists of a single line which contains the maximum number of opposing minions that Georgel's minion can kill without dying.

## Constraints and clarifications

$1 \leq T \leq 20$ 

$1 \leq N \leq 500$ 

$1 \leq A_i, D_i \leq 10^4$ 

$1 \leq ga, gd \leq 10^4$ 

There will be at most $4000$ minions in total.

## Example

`hsattack.in`
```
3
3 4
2
1 4
3 2
3 4
2
1 7
3 3
1000 1000
1
1000 1000
```

`hsattack.out`
```
2
1
0
```

## Explanation

Test 1 

Georgel's minion will attack the minion $(3, 2)$, killing it immediately, and then it becomes $(3, 1)$. Since it killed an opposing minion, it receives $(+1, +1)$ and becomes $(4, 2)$. Now it can kill the other opposing minion immediately without dying. If the minions were taken in a different order, it would not have been able to kill both.

Test 2 

Regardless of the order in which Georgel's minion attacks the opposing minions, it can only kill one of them.

Test 3 

Even if it could kill the opposing minion, Georgel's minion would also die.