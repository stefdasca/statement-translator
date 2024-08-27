# Progr2

To ensure that he also has success with progressions, Georgică thought of another problem. He has $N$ natural numbers and now wonders how many subsequences formed by at least two terms represent an arithmetic progression.

## Input data

The input file `progr2.in` contains on the first line $T$, the number of tests. Subsequently, for each test, the first line will contain a natural number $N$, and on the next line, $N$ natural numbers, with the meaning given in the statement.

## Output data

The output file `progr2.out` will contain $T$ lines, and each line $i$ will contain a single natural number, representing the number of subsequences that represent an arithmetic progression.

## Constraints

$ T = 10$  
$ 1 \leq N \leq 2\ 000 $  
$ 1 \leq v[i] \leq 10^9 $, where $v[i]$ is an element among Georgică's $N$ numbers.  
Georgică's numbers are distinct.

## Example

`progr2.in`  
```
2 
3 
2 3 1 
4 
5 6 3 4 
```

`progr2.out`  
```
3 
4 
```

## Explanation

For the first test, the three progressions are: $2 \ 3$, $2 \ 1$, and $3 \ 1$.  
For the second test, the four progressions are: $4 \ 5$, $4 \ 6$, $4 \ 5 \ 6$, $5 \ 6$.