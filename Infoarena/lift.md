# Lift

Vellipo wants to visit the entire Liftopolis complex, which hosts $Q$ buildings. Each building has a single entrance door at level $0$ and a single exit door located at a specified level. Any building in the complex has multiple levels both above and below level $0$, levels that can be reached using a very interesting elevator that can transport only one person at a time. Upon entering the building, Vellipo will directly enter the elevator, where he needs to give a sequence with the minimum number of ascent or descent commands to reach the exit. Each $k$-th command will determine the ascent or descent by a number of levels equal to the value of the $k$-th term in the Fibonacci sequence. Vellipo must give at least one command when he steps into the elevator.

## Task

For each of the $Q$ buildings in Liftopolis, specified by the level at which the exit door from the building is located, determine the minimum number of commands as well as the commands that Vellipo will give to reach the exit level.

## Input data

The input file `lift.in` contains a natural number $Q$ on the first line representing the number of buildings. Each of the next $Q$ lines contains an integer $N$ representing the level at which the exit door from the building is located.

## Output data

The output file `lift.out` will contain $Q$ lines. Line $i$ will contain the minimum number of commands given by Vellipo to exit building $i$, then a space, followed by a string of characters ‘+’ and ‘–’ (without spaces), which correspond to the direction of movement commands, in the order they are executed. In this string, the character ‘+’ specifies an ascent command and the character ‘–’ specifies a descent command.

## Constraints

$1 \leq Q \leq 50000$

For $20\%$ of the tests $|N| \leq 55$ and $|Q| \leq 40$

For $40\%$ of the tests $|N| \leq 5000$ and $|Q| \leq 50000$

For $100\%$ of the tests $|N| \leq 10^{15}$ and $|Q| \leq 50000$

Fibonacci sequence: $f_1 = 1$, $f_2 = 1$, and the $n$-th term is constructed using the relation $f_n = f_{n-1} + f_{n-2}$, $n \geq 3$

The solution is not unique. Any correct solution with a minimum number of commands is accepted.

## Example

`lift.in` 
```
3
2
5
-6
```

`lift.out`
```
2 ++
4 +-++
5 ---+-
```

## Explanation

To reach level $2$, the minimum number of commands given by Vellipo is $2$: ascent, ascent $(+1+1=2)$

To reach level $5$, the minimum number of commands is $4$: ascent, descent, ascent, ascent $(+1-1+2+3=5)$

To reach level $-6$, the minimum number of commands is $5$: descent, descent, descent, ascent, descent $(+1+1+2-3+5=6)$