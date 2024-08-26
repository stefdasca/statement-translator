## Task

Given the genealogical tree of monkeys, determine for each monkey how many monkeys the request passes through before it's resolved.

## Input data

The first line of the input file contains an integer $N$ representing the number of monkeys. 
The second line of the file contains $N$ numbers, $K_1 \space K_2 \space \dots \space K_n$ with the meaning stated in the task (it is guaranteed that there exists the $K_i$-th ancestor for each monkey $i$). If $K_i$ is 0, then monkey number $i$ can resolve requests. The monkey which is the ancestor of all other monkeys (the root of the genealogical tree) is the wisest monkey and thus can resolve requests.
The following $N-1$ lines will contain two numbers, separated by a space, $A$ and $B$ with the meaning: monkey $A$ is the parent of monkey $B$.

## Output data

The first line of the output file will contain $N$ numbers $G_1 \space G_2 \space \dots \space G_n$, $G_i$ representing the number of monkeys the request of monkey number $i$ passes through (excluding itself).

## Constraints and clarifications

$2 \leq N$
$N \leq 100\\ 000$ 

## Example

`cerere.in` 
```
10 
0 1 0 2 2 0 2 2 1 2
1 2 
1 3 
2 4 
2 5 
4 6 
7 6 
8 7 
9 7 
10 7
```

`cerere.out` 
```
0 1 0 1 2 0 1 1 2 1
```