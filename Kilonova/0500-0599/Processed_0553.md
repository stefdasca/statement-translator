Certainly! Here is the translated text:

---

A natural number is called *extrapar* if it can be written as the sum of distinct powers of $2$, where the exponents are even. The number $0$ is also considered extrapar. By considering the binary representation for a natural number, the positions of the digits are numbered from right to left, starting with $0$. A single operation must be performed on the binary representation. The operation consists of removing exactly $K$ digits located in consecutive positions.

# Task
Given the binary representations of $N$ natural numbers, determine for each of them if it is possible to obtain an extrapar number under the above conditions.

# Input data
The input file `extrapare.in` contains on the first line two natural numbers `N K`, separated by a space. Each of the next $N$ lines contains the binary representation of a natural number.

# Output data
The output file `extrapare.out` will contain $N$ lines. The $i$-th line ($1 \leq i \leq N$) will contain the binary representation of the extrapar number obtained by performing a single operation on the $i$-th representation from the input file, or the value $\unicode{2212}1$ if obtaining an extrapar number is not possible in this way.

# Constraints and clarifications
* $0 < N \leq 10$;
* $0 \leq K <$ the number of digits in any representation in the input file;
* Any representation in the input file has at most $1 \ 000 \ 000$ digits;
* If there are multiple ways to perform an operation such that the result is an extrapar number, the result for that operation where the position of the first removed digit is the largest (i.e., the leftmost position) will be displayed.
* It is guaranteed that the binary representations in the input file have the leftmost digit equal to $1$.
* The binary representation of the resulting number after performing the operation will be displayed without insignificant leading zeros that may form to its left.

|# | Score | Constraints|
| - | - | ---------- |
| 1 | 19| $K = 0$ |
| 2 | 32|$K > 0$, length of strings $ \leq 1000$ |
| 3 | 49| $K > 0$, length of strings $ \leq 1 \ 000 \ 000$ |

# Example
`extrapare.in`
```
9 3
1001101
1010000010
101010001
111010100
100100
100010100
101000001
11110
101000
```

`extrapare.out`
```
-1
1010000
10001
10100
100
10100
1
-1
0
```

## Explanation
We need to remove $3$ digits to form extrapar numbers.
- The numbers for which an extrapar number cannot be obtained by removing three digits from consecutive positions are the first and eighth.
- From `1010000010` we cut the digits at positions $0$, $1$, and $2$ and obtain `1010000`.
- `101010001` is already extrapar and we will remove the leftmost three digits.
- Notice that if the result is formed only by digits equal to $0$ a single $0$ will be displayed.

And so on...