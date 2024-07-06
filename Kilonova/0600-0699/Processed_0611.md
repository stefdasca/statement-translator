> I have nothing more to say!
> You have sworn an oath with your arms on your shields!
> The power is within you
> and the gods! But think, heroes,
> that the gods are far away, high above,
> and the enemies are close to us!

In the time of the Free Dacians, it was said that an array $A$ is $K$-free if the absolute difference of any two consecutive elements in the array is **not** divisible by $K$.

# Task

The leader of the Free Dacians, Decebal, gives you an array $A$ of $N$ integers and a natural number $K$. For the Free Dacians to win the battle against the army led by Trajan, you need to calculate the number of ways in which we can rearrange the elements of the array $A$ such that the resulting array is $K$-free. Since this number can be very large, the remainder of this number when divided by $10^9 + 7$ is required.

# Input data

The first line contains the numbers $N$ and $K$ as described in the task. The second line contains $N$ numbers, representing the elements of the array $A$.

# Output data

The first line of the output file will contain the remainder when divided by $10^9 + 7$ of the number Decebal asks you to compute.

# Constraints and clarifications
* $1 \leq N \leq 2\ 500$
* $2 \leq K \leq 1\ 000\ 000$
* $0 \leq A_{i} \leq 10^9$.

## Subtask 1 (6 points)
* $1 \leq N \leq 10$
## Subtask 2 (20 points)
* $1 \leq N \leq 50$
## Subtask 3 (25 points)
* $1 \leq N \leq 200$
## Subtask 4 (49 points)
* No other constraints

# Example 1
`stdin`
```
5 5
1 1 6 2 3
```
`stdout`
```
6
```
## Explanation

The $K$-free arrays are: 
1 2 1 3 6
1 2 6 3 1
1 3 1 2 6
1 3 6 2 1
6 2 1 3 1
6 3 1 2 1

# Example 2

`stdin`
```
5 6
1 2 3 4 5
```
`stdout`
```
120
```

## Explanation

Long live Free Dacia!!!