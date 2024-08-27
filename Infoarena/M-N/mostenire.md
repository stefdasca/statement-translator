## Task

Grandfather and Grandmother have encountered an unprecedented problem: the inheritance issue. The two have $2$ and $K$ very delicious apples that need to be distributed to their children and grandchildren. After many days of struggle, Grandfather finally realized that he has $N$ children (he wasn't sure exactly), and each child $i$ has $V_i$ children. After a strong argument with Grandmother, the two characters decided to divide the $K$ apples among the $N$ children, and the children in turn will divide the apples they receive among their children (Grandfather's grandchildren). Since Grandfather and Grandmother are old, they ask you to arrange the distribution of apples so that the maximum difference in apples received by any $2$ children and any $2$ grandchildren is as small as possible. More precisely, $\max(\text{ChildMax} - \text{ChildMin}, \text{GrandchildMax} - \text{GrandchildMin})$ should be minimized. $\text{ChildMax}$ and $\text{ChildMin}$ represent the maximum and minimum number of apples obtained by a child, respectively. $\text{GrandchildMax}$ and $\text{GrandchildMin}$ represent the maximum and minimum number of apples obtained by a grandchild, respectively.

## Input data

The input file `mostenire.in` will contain on the first line $2$ natural numbers $N$ and $K$. On the next line there will be $N$ natural numbers: element $i$ representing the value $V_i$. The elements on the $2^{nd}$ line are given in increasing order.

## Output data

The output file `mostenire.out` will contain on the first line a natural number representing the requested minimum difference (the $\max(\text{ChildMax} - \text{ChildMin}, \text{GrandchildMax} - \text{GrandchildMin})$). On the next line there will be $N$ natural numbers, element $i$ representing the number of apples assigned to child $i$. Any correct solution will be scored.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

$1 \leq K \leq 10^{18}$ 

The sum of $V$ values is $\leq 2\ 000\ 000\ 000$

Any $V$ is greater than or equal to $1$, meaning each child has children of their own

For $30\%$ of the points $N \leq 50$ and $K \leq 3000$

Be very careful with overflow

Children distribute all the apples they receive to their grandchildren to minimize the required difference

If you only correctly determine the minimum difference but do not reconstruct correctly, you receive $20\%$ of the score. However, the reconstruction must necessarily be possible, meaning the sum of the $N$ numbers in the output file must be $K$ 

## Example

`mostenire.in`

```
2 100
1 2
```

`mostenire.out`

```
15 43
57 4
```