## Task

Knowing that the two children will play optimally, the task is to determine the winner for a given configuration of the cards.

## Input data

The input file `cartonase.in` contains on the first line an integer $T$, representing the number of test cases to follow. Each of the next $T$ lines contains an integer $N$, followed by a space, and then $N$ characters separated by spaces that can be $R$ or $A$, indicating the colors of the faces of the cards that are face up.

## Output data

The output file `cartonase.out` will contain $T$ lines. On line $i$ $(1 \leq i \leq T)$, the message $DA$ will be written if Miruna is the winner of the game described on line $i+1$ in the input file, and the message $NU$ otherwise.

## Constraints and clarifications

$1 \leq T \leq 20$ 

$1 \leq N \leq 100$ 

For 30% of the test cases, $1 \leq N \leq 10$ 

## Example

`cartonase.in` 

```
2 
3 A R R 
3 R R R 
```

`cartonase.out` 

```
DA 
NU 
```