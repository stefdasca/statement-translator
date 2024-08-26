# Sormin

Given an array $A[1 \dots N]$ and a number $S$.

## Task

Among all the subarrays that sum up to $S$, determine a subarray for which the OR sum, in bits, is minimal.

## Input data

The input file `sormin.in` contains numbers $N$ and $S$ on the first line. The second line contains $N$ natural numbers separated by spaces.

## Output data

The output file `sormin.out` will contain on the first line numbers $R$ and $M$, representing the minimal OR sum, in bits, and the number of elements in the determined subarray, respectively. On the second line, the $M$ elements of the determined subarray will be written, separated by spaces.

## Constraints

1 $\leq$ $N$ $\leq$ 100000 

1 $\leq$ $S$ $\leq$ 50000 

1 $\leq$ $A[i]$ $\leq$ 5000

Let $x$ and $y$ be two natural numbers. Each of them has a binary representation, $x[k], x[k-1], \dots, x[1], x[0]$ and respectively $y[k], y[k-1], \dots, y[1], y[0]$. If the lengths of the representations are different, the shorter one can be padded to the left with zeros. The OR sum, in bits, of the numbers $x$ and $y$ is understood as the number $z$ with the representation $z[k], z[k-1], \dots, z[1], z[0]$ where $z[j] = x[j] \mid y[j]$, which is the operation defined by $0 \mid 0 = 0$, $0 \mid 1 = 1$, $1 \mid 0 = 1$, $1 \mid 1 = 1$, $0 \leq j \leq k$.

For example $x = 12$ and $y = 9$ have binary representations 1100 and 1001, and $x \mid y = 1101 = 13$.

For the given tests, a solution is guaranteed to exist. If there are multiple subarrays with the minimal OR sum, any of them will be considered correct. Also, the elements of the subarray can be displayed in any order.

## Example

`sormin.in`

```
13 20
2 2 2 2 2 3 3 3 3 5 5 5 5
```

`sormin.out`

```
3 8
2 2 2 2 3 3 3 3
```

## Explanation

We cannot obtain the sum 20 using only elements equal to 2. We can obtain the sum 20 using the elements equal to 2 and 3. The OR sum is 3, because 2 has the binary representation 10, and 3 has the binary representation 11, so $2 \mid 3 = 3$.