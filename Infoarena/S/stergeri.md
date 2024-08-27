## Task

The magician Dino wrote on a sheet of paper the natural numbers in order from $1$ to $N$ (i.e., $1 \, 2 \, 3 \, \dots \, N$). Frasinel chose two indices $x$ and $y$ $(x \leq y)$ and Dino erased all the elements between positions $x$ and $y$. Then Dino tells Frasinel to choose two other indices and will perform the same operation for the remaining elements written on the paper. After $M$ such operations, Frasinel would like to know which element is on position $K$ on the sheet.

## Input data

The input file `stergeri.in` contains on the first line the numbers $N \, M \, K$ having the significance from the statement. The following $M$ lines contain two integers $x \, y$ representing the indices from the operation performed by Frasinel.

## Output data

The output file `stergeri.out` contains on the first line a number $SOL$, representing the number that is on the sheet at position $K$ after all operations are performed.

## Constraints

$1 \leq N \leq 2 \ 000 \ 000 \ 000$

$1 \leq M \leq 100 \ 000$

$K$ will be at most the number of elements remaining at the end on the sheet

## Example

`stergeri.in`
```
12 2 3
4 7
2 6
```

`stergeri.out`
```
12
```

## Explanation

After the first operation, the sheet looks like this: $1 \, 2 \, 3 \, 8 \, 9 \, 10 \, 11 \, 12$. After the second operation: $1 \, 11 \, 12$. Therefore, in position $3$ is the number $12$.