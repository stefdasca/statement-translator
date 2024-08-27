## Task

"Maxim I said!" At the casino on the corner, new machines have been brought in. The subject of the problem is a machine that is continuously frequented by a certain master, $Hapsan$, whom his friends know as a true hero. Few people want to admit that $Hapsan$ is actually on an extraordinary mission to bankrupt the casino industry with as many colossal wins as possible. The machine in question is not much different from a classic slot machine. The machine offers a reward to the player when certain configurations of fruits appear on the video display panel after the circular reels spin independently at random speeds. For simplicity, we will assume that the slot machine has $N$ reels, and the fruits are of $N$ types, indexed by numbers from $1$ to $N$ in the order of their associated value. What is special about this slot machine is that the same $N$ images always appear in a random order. Since no fruit repeats on the screen of the machine regardless of the number of games played, the casino has been compelled over time to modify the way it rewards players. Therefore, the player is rewarded only if they manage to guess the number of local maxima that will appear. A position $i$ is considered a local maximum if the value of the fruit at position $i$ is greater than that of its neighbors. Since master $Hapsan$ has most likely already filled his pockets with money from this machine, he obviously wouldn't ask for your help, but he wants to help you using his vast experience with machines. He dictates a sequence of numbers representing the configuration that will appear, and the optimal winning strategy is to determine the average number of local maxima that could appear.

## Input data

The input file `maxim2.in` will contain on the first line the number $N$, followed by $N$ numbers on the second line representing the values of the fruits dictated by the master. Elements for which we have no information are marked with $0$.

## Output data

The output file `maxim2.out` will contain the average number of local maxima that could appear after the spin.

## Constraints and clarifications

$1 \leq N \leq 100000$

The answer will be considered correct only if $\mid committee\_result - participant\_result \mid \leq 0.0000001$

It is assumed that any final configuration can appear equally likely.

## Example

`maxim2.in`
```
5
4 0 0 0 1
```

`maxim2.out`
```
1.83333333
```

## Explanation

The possible final configurations are:

$4 \ 2 \ 3 \ 5 \ 1$: $2$ maxima $(4$ and $5)$

$4 \ 2 \ 5 \ 3 \ 1$: $2$ maxima $(4$ and $5)$

$4 \ 3 \ 2 \ 5 \ 1$: $2$ maxima $(4$ and $5)$

$4 \ 3 \ 5 \ 2 \ 1$: $2$ maxima $(4$ and $5)$

$4 \ 5 \ 2 \ 3 \ 1$: $2$ maxima $(3$ and $5)$

$4 \ 5 \ 3 \ 2 \ 1$: $1$ maximum $(5)$

Answer: $(2+2+2+2+2+1)/6 = 11/6$