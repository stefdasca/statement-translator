```markdown
Given a sequence $A$ with $N$ non-zero natural number elements. For each subarray of the form $A_{i},A_{i+1},A_{i+2},\\ldots,A_{j}$ from the sequence $A$ (where $i < j$) for which the greatest common divisor of the numbers $A_{i}$ and $A_{j}$ is greater than $1$, compute the value $A_{i} \oplus A_{i+1} \oplus \ldots \oplus A_{j}$, where $ \oplus $ is the *exclusive OR* operation on bits (denoted in C/C++ with `^`). Among the values obtained for each subarray, perform the operation $ \oplus $ again, obtaining as a result a number $B$.

We need to determine the value of $B$.

# Input data
The input file's first line contains the number $N$, and the second line contains the elements of the sequence $A$.

# Output data
The output file's first line will contain the value of the number $B$.

# Constraints
- $1 \leq N \leq 100\ 000$
- $1 \leq  A_{i} \leq 1\ 000\ 000$

|# | Points | Constraints|
| - | - | ------------|
|1|9|$1 \leq N \leq 500$|
|2|12|$1 \leq N \leq 5\ 000$|
|3|15|The elements of the sequence $A$ are even numbers.|
|4|26|The elements of the sequence $A$ are prime numbers.|
|5|38|No additional constraints|

# Example
`secvxor.in`
```
5
4 7 6 10 21
```
`secvxor.out`
```
1
```

# Explanation
The operation $ \oplus $ is defined as follows: $0 \oplus 0  = 1 \oplus 1 = 0$, $ \ 0 \oplus 1 = 1 \oplus 0 = 1$, and $ (2k + \ell) \oplus (2k' + \ell') = 2(k \oplus k') + (\ell \oplus \ell')$ for $k, k' \geq 0$ and $0 \leq \ell, \ell' \leq 1$.

For example, for the numbers $7$ and $18$, their binary representations are $7=111_{2}$ and $18=10010_{2}$. Performing the $ \oplus $ operation between these numbers, we get the result $10101_{2}=21$.

Subarrays that satisfy the property from the statement (that is, they are of length at least 2, and the elements at the beginning and end of the subarray have the greatest common divisor greater than $1$) are: $(4,7,6)$, $(4,7,6,10)$, $(7,6,10,21)$, $(6,10)$, $(6,10,21)$. Performing the $ \oplus $ operation among the elements of each subarray, we obtain the values $5,15,30,12$, and $25$, respectively. Performing the $ \oplus $ operation among these values, we get the value of $B=1$.
```