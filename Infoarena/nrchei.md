## NrChei

Given the numbers $n$, and $MOD$. Display the remainder of the division by $MOD$ of the number of strings that belong to an alphabet of a size for which, if they constituted the input for the problem keys, the correct output would be the number $n$.

## Input data

The input file `nrchei.in` contains, on the first line, the numbers $n$, and $MOD$, separated by a space. 

## Output data

The output file `nrchei.out` contains, on the first line, the answer.

## Constraints

$1 \leq n \leq 1\,000\,000\,000$

$1 \  < \  < \ MOD \ < 10^9 + 10$

## Example

`nrchei.in`

```
1 2
100 16
10 3
1000000007 10198269
2323 23
```

`nrchei.out`

```
23232323 13529474
```

## Explanation

In the first example, the 16 strings are: $aa$, $bb$, $baa$, $aba$, $bba$, $aab$, $bab$, $abb$, $baaa$, $abaa$, $aaba$, $bbba$, $aaab$, $bbab$, $babb$, $abbb$.