Tablets

For a week, Vasilica has been employed at Choco-Bin S.R.L., the only factory in the world that produces "chocolate with numbers". Today, by signing a very advantageous contract with an important retail chain, it is time for Vasilica to show what he can do. Even if it is his first job, the factory manager promised him a 50% salary bonus in case of fulfilling the contract with the respective stores. Vasilica's task is to establish the design of an $N \times N$ chocolate tablet divided into $N^2$ squares of size $1 \times 1$. The contract also stipulates the following, in addition to the $N$ size of the tablet's side: From each square in the tablet, one of the numbers 1, 2, $\dots$ $N^2$ must be embossed. Any two squares have distinct numbers. On each row of the tablet, the numbers are in ascending order. On column $K$ (value also specified in the contract), the numbers must be even. Vasilica is pleading with you to help him complete his task. He cannot promise you money (he is still a student), but he can guarantee you 100 points on this problem.

## Input data

The input file `tablete.in` contains on the first line two integers $N$ and $K$ separated by a space, having the meanings described above.

## Output data

In the output file `tablete.out`, $N$ lines will contain $N$ integer values each, representing a possible variant for the chocolate tablet with numbers.

## Constraints and clarifications 
3 $\leq$ $N$ $\leq$ 1000

1 < $K$ < $N$

Any solution provided that meets the conditions in the statement is considered correct.

## Example

`tablete.in`
```
4 3
```

`tablete.out`
```
2 3 4 8
1 5 6 7
9 11 12 16
10 13 14 15
```

## Explanation

The bold numbers represent column $K$ on which parity was considered.