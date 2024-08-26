## Task

Given a string of length $N$, you need to calculate how many distinct subarrays exist for each interval of the string and print the sum of these numbers.

## Input data

The input file `tst.in` will contain a string composed only of lowercase letters of the English alphabet, of length $N$.

## Output data

The output file `tst.out` will contain a single number, namely the required number.

## Constraints

$1 \leq N \leq 5000$

You guys never write the for-loop this way because you are not cool!

## Example

`tst.in`
```
baa
```

`tst.out`
```
13
```

## Explanation

$Cool (0,0) = 1$ $\Rightarrow$ b 

$Cool (0,1) = 3$ $\Rightarrow$ b, a, ba 

$Cool (0,2) = 5$ $\Rightarrow$ b, ba, baa, a, aa 

$Cool (1,1) = 1$ $\Rightarrow$ a 

$Cool (1,2) = 2$ $\Rightarrow$ a, aa 

$Cool (2,2) = 1$ $\Rightarrow$ a 

$1 + 3 + 5 + 1 + 2 + 1 = 13$