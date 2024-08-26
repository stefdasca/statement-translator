## Task

A string $S$ consisting of $N$ lowercase English letters ('a'-'z') is given. Determine how many subarrays of the string $S$ are of the form $u^K$. A subarray of a string $S$ is a sequence of consecutive characters of the string $S$. A string $X$ is of the form $u^K$ if there exists a string $u$ consisting of at least one character, such that $X$ is formed by concatenating the string $u$ exactly $K$ times. For example, the string $X = aabaabaab$ is of the form $u^3$, because there exists the string $u = aab$ which, concatenated 3 times, forms the string $X$.

## Input data

The first line of the input file `per.in` contains two integers, separated by a space: $N$ and $K$. The second line contains $N$ characters from the set {'a'-'z'}, not separated by spaces, representing the given string $S$.

## Output data

The first (and only) line of the output file `per.out` will contain the number of subarrays of the given string $S$ that are of the form $u^K$.

## Constraints

$1 \leq N \leq 6000$  
$2 \leq K \leq N$  

## Example

`per.in`  
```
30 3
aabaabaabaacaabaacaabaacaabxyz
```

`per.out`  
```
7
```