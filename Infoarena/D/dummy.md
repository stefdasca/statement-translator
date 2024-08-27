# Training Dummy

"Training Dummies are mechanical NPCs that enable you to test your dps out on different level mobs. Training dummies are located in all capital cities." In the center of Orgrimmar city, there are so-called "Training Dummies". As their name suggests, these dummies are used by Horde warriors to train in battles. The goal of a warrior is to destroy this dummy. Only then will he be considered worthy to participate in the battle against Alliance soldiers. A dummy has a natural number $X$ of health points. A dummy is considered destroyed when the number of its health points becomes equal to or less than $0$ (zero). Warriors have axes available with which they can hit the dummies. Each axe has a power equal to a natural number between $A$ and $B$. There are exactly $B - A + 1$ axes. Among them, no two axes have the same power. A Horde warrior equips an axe randomly. The warrior hits the dummy every second with the axe, causing damage equal to the power of the equipped axe. More precisely, let's assume that at this moment the dummy has $X$ health points, and the warrior's equipped axe has power $P$. When the warrior hits the dummy, it will be left with exactly $X - P$ health points. Impatient, the warriors want to know the average number of seconds in which the dummy can be destroyed. Therefore, we ask you to display this number!

## Input Data

The input file `dummy.in` contains on the first line the natural number $T$, representing the number of tests. Each line $i$ of the next $T$ lines will contain $3$ natural numbers $X$ $A$ $B$, representing the input data for test $i$.

## Output Data

The output file `dummy.out` will contain $T$ lines. On each line $i$ of the $T$ lines, there will be a single real number, representing the average number of seconds in which the dummy can be destroyed for the input data of test $i$. The number will be displayed with $6$ exact decimals.

## Constraints and clarifications

$1 \leq T \leq 10^3$ 

$1 \leq X, A, B \leq 10^9$ 

$0 \leq B - A \leq 10^3$ 

The evaluator checks the result with a precision of $10^{-5}$.

## Example

`dummy.in` 
```
2
10 5 5
20 9 10
```

`dummy.out` 
```
2.000000
2.500000
```

## Explanation

For the first example, the warrior can only equip the axe with power $5$. Therefore, every second, he will cause damage equal to $5$ health points every second. So, the dummy will be destroyed in exactly $\frac{10}{5} = 2$ seconds. For the second example: If the warrior equips the axe with power $9$, he will cause damage equal to $9$ health points every second. So, the dummy will be destroyed in $3$ seconds. If the warrior equips the axe with power $10$, he will cause damage equal to $10$ health points every second. So, the dummy will be destroyed in $2$ seconds. Consequently, the average number of seconds in which the dummy can be destroyed is equal to $\frac{(3 + 2)}{2} = 2.5$.