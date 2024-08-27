ABPerm

Two permutations of order $N$ are given. 

## Task

The task type $T$ is specified, which can be $1$ or $2$ :
1) If $T=1$, you need to find how many permutations of order $N$ can be obtained after $N$ steps of "interleaving" the two permutations
2) If $T=2$, you need to find how many distinct permutations of order $N$ can be obtained after $N$ steps of "interleaving" the two permutations

## Input data

The input file `abperm.in` contains on the first line the numbers $T$ and $N$. On the second line, separated by a space, are the elements of permutation $a[]$, and on the third line, separated by a space, are the elements of permutation $b[]$. 

## Output data

In the output file `abperm.out`, the first line contains a single natural number representing the required number according to the task type. 

## Constraints

$1 \leq N \leq 10^5$  
Since the values required can be very large, calculate these values modulo $10^9+7$  
In general, by "interleaving" two sequences $a[]$ and $b[]$, of lengths $n$ and respectively $m$, it is understood to determine a new sequence $c[]$, of length $n+m$, which contains all the elements of both sequences $a[]$ and $b[]$.   
The elements of sequences $a[]$ and $b[]$ form subsequences in $c[]$.      
If for the first $k$ elements of $c[]$ the first $i$ elements from $a[]$ and the first $j$ elements from $b[]$ were used, then for the $k+1$-th element of $c[]$, $a[i+1]$ or $b[j+1]$ will be used.  
At each interleaving step, another element is added to the constructed sequence $c[]$.

## Example

`abperm.in`  
```
1 3
1 2 3
3 2 1
```
`abperm.out`
```
8
```

## Explanation

After 3 steps of interleaving, the permutations that can be obtained are: $1 2 3$, $1 2 3$, $1 3 2$, $1 3 2$, $3 1 2$, $3 1 2$, $3 2 1$, $3 2 1$

`abperm.in`  
```
2 3
1 2 3
3 2 1
```
`abperm.out`
```
4
```

## Explanation

After 3 steps of interleaving, 4 distinct permutations can be obtained: $1 2 3$, $1 3 2$, $3 1 2$, $3 2 1$