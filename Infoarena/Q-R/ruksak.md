## Task 

You are given a set consisting of $N$ objects, each characterized by a weight and a profit. Find a subset of objects such that the sum of their profits is maximized, while the sum of their weights does not exceed a value $G$ .

## Input data 

The first line of the file `ruksak.in` will contain the values $N$ and $G$, as mentioned in the statement. The following $N$ lines will contain pairs of values $W_i$ and $P_i$, representing the weight and profit of object $i$, respectively.

## Output data 

The output file `ruksak.out` will contain a single value $P_{max}$, the maximum profit that can be obtained while respecting the problem's condition.

## Constraints 

$1 \leq N \leq 3 \cdot 10^5$ 

$1 \leq G \leq 3000$ 

$0 \leq W_i, P_i \leq 3000$ 

Special thanks to Vlad Gavrila for the original problem statement, which we copied and pasted here. We love you, the sweetest boy :*

## Example 

`ruksak.in` 
```
6
10
3 7
3 4
1 2
1 9
2 4
1 5
```

`ruksak.out` 
```
29
```

## Explanation 

We take objects 1, 2, 4, 5, and 6, whose total weight is 10, and the sum of profits is 29.

Hint for the solution 

You wish, you little rascals!