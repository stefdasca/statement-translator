## Task 

In the physics laboratory, there are $N$ light bulbs. Initially, all the bulbs are turned off. Each of the $K$ students in the laboratory chooses a natural number $d_i$ $(2 \leq d_i \leq N)$ and toggles the state of all bulbs from $d_i$ to $d_i$. By toggling the state of a bulb, it means that a turned-off bulb will become turned on and a turned-on bulb will become turned off. After a student toggles the state of their bulbs, they leave the class. Write a program that calculates how many bulbs will remain on after all the students leave the class.

## Input data 

The input file `light2.in` contains on the first line a positive integer $N$, representing the number of bulbs in the laboratory. The second line contains the number $K$, the number of students. The third line of the file contains $K$ natural numbers $d_1$, $d_2$, $\dots$ $d_K$, separated by a space.

## Output data 

The output file `light2.out` will contain a single natural number, representing the number of bulbs that remain on after all the students leave the class.

## Constraints and clarifications

$3 \leq N \leq 10^{12}$

$1 \leq K \leq 22$

$1 \leq d_i \leq \min(N, 10^6)$

The numbers $d_i$ are not necessarily distinct.

## Example 

`light2.in` 
```
8
2
2 3
```

`light2.out`
```
4
```

## Explanation 

Initially, all the bulbs are turned off. After the first student toggles the state of their bulbs, the $2$-nd, $4$-th, $6$-th, and $8$-th bulbs will be on. After the second student toggles the state of their bulbs, the bulbs numbered $2$, $3$, $4$, and $8$ will remain on.