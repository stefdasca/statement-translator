# Noxornolife

After finishing their cake, Mountainman and Middle Islander got bored and decided to play a new game, inspired by their friend Xorrin the Olympian. This time, the game is characterized by three natural numbers $X$, $A$, and $B$. Middle Islander moves first. The turns alternate, and the player who cannot make a move loses. During a move, the player selects a natural number $Y$ such that $A \leq Y \leq B$ and $X \oplus Y < X$, where $\oplus$ represents the xor binary operation. The value of $X$ is then replaced by $X \oplus Y$. Given the values $X$, $A$, and $B$, determine who will win, assuming both players play optimally.

## Input data

The input file `noxornolife.in` contains the first line with a natural number $T$, representing the number of test cases. Each test case consists of exactly one line containing the values of $X$, $A$, and $B$. 

## Output data

In the output file `noxornolife.out`, print the answers for each test in order. For each test, print either `Island` (if Middle Islander wins, assuming both play optimally) or `Mountain` (if Mountainman wins, assuming both play optimally).

## Constraints and clarifications

$T \leq 100000$

$0 \leq X \leq 10^{18}$

$1 \leq A$, $B \leq 10^{18}$

$A \leq B$

## Example

`noxornolife.in`
```
5
1 1 1
6 1 5
7590 1 82335
10050 26357 229376
499543360 32 1243696352
```

`noxornolife.out`
```
Island
Mountain
Island
Mountain
Island
```