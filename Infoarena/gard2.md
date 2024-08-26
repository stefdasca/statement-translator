Gard2

After the success of painting the first fence, the team of workers was hired to paint the fence of one of the richest people in town. Being satisfied with the amount offered to the whole team, the workers didn't make many demands this time. However, they decided to work in shifts: first the workers from the first shift, then those from the second and so on. In each shift, at least one and at most $K$ workers will work. Also, each worker will work in exactly one shift. Surprised by the organization of the workers in shifts and being a lover of counting problems, the owner of the fence wants to find out in how many ways the workers can be arranged in shifts. Since he announced that he will offer a nice sum to whoever gives him the answer in less than a second, you decided to write a program to help you win the prize.

## Task

Write a program that, for given values $N$ and $K$, determines the number of ways to arrange the $N$ workers in shifts such that in each shift at least one and at most $K$ of them work.

## Input data

The input file `gard2.in` contains two integers: $N$ and $K$, representing the total number of workers and the maximum number of workers who can work simultaneously (in one shift).

## Output data

The output file `gard2.out` will contain the determined number.

## Constraints and clarifications

$1 \leq K \leq N \leq 50$

Two arrangements are distinct if there is at least one worker who works in shifts with different order numbers.

## Example

`gard2.in`
```
3 2
```

`gard2.out`
```
12
```

`gard2.in`
```
4 1
```

`gard2.out`
```
24
```

`gard2.in`
```
5 3
```

`gard2.out`
```
530
```

## Explanation

For the first example, the possible arrangements in shifts are:

Variant 1

Shift1: 1 2

Shift2: 3

Variant 2

Shift1: 1 3

Shift2: 2

Variant 3

Shift1: 3 2

Shift2: 1

Variant 4

Shift1: 1

Shift2: 2 3

Variant 5

Shift1: 2

Shift2: 3 1

Variant 6

Shift1: 3

Shift2: 1 2

Variant 7

Shift1: 1

Shift2: 2

Shift3: 3

Variant 8

Shift1: 1

Shift2: 3

Shift3: 2

Variant 9

Shift1: 2

Shift2: 1

Shift3: 3

Variant 10

Shift1: 2

Shift2: 3

Shift3: 1

Variant 11

Shift1: 3

Shift2: 1

Shift3: 2

Variant 12

Shift1: 3

Shift2: 2

Shift3: 1