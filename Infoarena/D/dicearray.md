# Dice Array

Gimi and Victor, two good friends, decided to play dice on a summer afternoon. The dice game involves throwing $N$ dice and thus obtaining a sequence $Z$ of $N$ dice. The score of a throw is obtained by summing the points on the top face of the $N$ dice. All dice have the following planar development: Since the sum of the values on two opposite faces of a die is always $7$, a die can be described by a triplet $(\text{top}, \text{front}, \text{left})$, where:
$\text{top}$ represents the value on the top face of the die (perpendicular to the $oY$ axis)
$\text{front}$ represents the value on the front face of the die (perpendicular to the $oX$ axis)
$\text{left}$ represents the value on the left face of the die (perpendicular to the $oZ$ axis)

For example, the die $(6, 2, 3)$ looks like this:
When Gimi throws the dice, he says to Victor: "Get yourself a lollipop while I throw these dice." While Victor is distracted, Gimi has time to cheat by performing $Q$ operations on the dice sequence. An operation can be described by a triplet $(l, r, d)$ as follows: all dice $Z[i]$ with $i$ from $l$ to $r$ rotate counterclockwise (anticlockwise) by $90$ degrees on the axis $d \in \{'x', 'y', 'z'\}$, viewed from the positive direction of the axes.

For example, the die $(6, 2, 3)$ after a rotation on the $'x'$ axis becomes the die $(4, 2, 6)$, after a rotation on the $'y'$ axis it becomes $(6, 3, 5)$, and after a rotation on the $'z'$ axis it becomes $(2, 1, 3)$. Gimi wants to know what score he has achieved after performing the $Q$ operations on the sequence.

## Input data

The input file `dicearray.in` will contain on the first line two natural numbers $N$ and $Q$, representing the number of dice and the number of operations.
The next $N$ lines will contain three numbers $(\text{top}, \text{front}, \text{left})$ describing the $N$ dice.
The next $Q$ lines will contain two numbers $(l, r)$ and a character $d \in \{'x', 'y', 'z'\}$ representing the operations performed on the dice sequence.

## Output data

The output file `dicearray.out` will contain a single number $S$, representing the score Gimi has achieved after performing the $Q$ operations.

## Constraints and clarifications

$1 \leq N, Q \leq 70\ 000$

For tests worth $20$ points: 
  $1 \leq N, Q \leq 1\ 000$
  the only type of rotation will be around the $Ox$ axis

For tests worth $30$ points:
  $1 \leq N, Q \leq 1\ 000$

For tests worth $20$ points:
  $1 \leq N, Q \leq 70\ 000$ 
  the only type of rotation will be around the $Ox$ axis

For tests worth $30$ points:
  $1 \leq N, Q \leq 70\ 000$
  
Attention! All operations performed by Gimi must be executed in the order given in the input data.

## Example

`dicearray.in`
```
3 3
6 2 3
6 2 3
6 2 3
1 1 x
2 2 y
3 3 z
```

`dicearray.out`
```
12
```

`dicearray.in`
```
6 3
1 2 4
5 6 3
4 5 1
6 4 2
3 2 1
3 5 4
3 4 z
3 4 x
2 2 x
```

`dicearray.out`
```
22
```

`dicearray.in`
```
12 5
2 6 4
5 3 1
6 4 5
2 6 5
3 1 4
6 5 2
1 4 6
3 5 2
3 6 2
4 1 2
4 z
7 11 z
6 8 x
2 2 x
1 1 z
```

`dicearray.out`
```
50
```

## Explanation

For the first example, after rotations the dice will be $(4, 2, 6)$, $(6, 3, 5)$, $(2, 1, 3)$. The answer is $4 + 6 + 2 = 12$.