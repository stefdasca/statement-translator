# Task

Consider two non-zero natural numbers $N$ and $K (K \leq N)$. An array of $N$ natural numbers contains numbers from $1$ to $K$. Each value from $1$ to $K$ appears at least once in the array. The elements of the array are known, but not their order.

You are required to reconstruct the array using certain information about it.

You need to implement a function:

```cpp
void Solve(int NrTest, int N, int *S)
```

The grader will call this function once and will pass the following information through the parameters (see the restrictions table below):

* $NrTest$ = the test number
* $N$ = the number of elements in the array
* $S$ = an array containing the $N$ elements of the sought array in ascending order.

In the function `Solve` you will call the following functions provided by the grader:

```cpp
int Ask(int *X)
```

This function transmits through the parameter $X$ an array containing the elements of the sought array in an order chosen by you and returns the minimum number of swaps between elements on consecutive positions that can be applied to the array $X$ to transform it into the requested array.
This function can be called a limited number of times (according to the restrictions table).

```cpp
void GiveSolution(int *X)
```

This function transmits through the parameter $X$ the sought array. This function will be called once at the end, after all calls to the function `Ask`.

# Constraints and clarifications

|NrTest|N|Max # calls|Remarks|Score|
|-|-|-|-|-|
|0|$2^2$|$24$|example|$0$|
|1|$2^4$|$2^8$|the array is a permutation|$7$ (group with $2$)|
|2|$2^5$|$2^{10}$|the array is a permutation|$7$ (group with $1$)|
|3|$2^5$|$2^5 \cdot 5 \cdot 2$|the array is a permutation|$6$ (group with $4$)|
|4|$2^6$|$2^6 \cdot 6 \cdot 2$|the array is a permutation|$6$ (group with $3$)|
|5|$2^6$|$2^6 \cdot 6$|the array is a permutation|$14$ (group with $6$)|
|6|$2^7$|$2^7 \cdot 7$|the array is a permutation|$14$ (group with $5$)|
|7|$2^9$|$2^9 \cdot 2$|the array contains only elements $1$ and $2$|$11$ (group with $8$)|
|8|$2^{10}$|$2^{10} \cdot 2$|the array contains only elements $1$ and $2$|$11$ (group with $7$)|
|9|$2^9$|$2^9 \cdot 2$|the array is a permutation|$19$ (group with $10$)|
|10|$2^{10}$|$2^{10} \cdot 2$|the array is a permutation|$19$ (group with $9$)|
|11|$2^9$|$2^9 \cdot 2$|-|$18$ (group with $12$)|
|12|$2^{10}$|$2^{10} \cdot 2$|-|$18$ (group with $11$)|
|13|$2^9$|$2^9$|the array is a permutation|$11$ (group with $14$)|
|14|$2^{10}$|$2^{10}$|the array is a permutation|$11$ (group with $13$)|
|15|$2^9$|$2^9$|-|$14$ (group with $16$)|
|16|$2^{10}$|$2^{10}$|-|$14$ (group with $15$)|

## Notes regarding evaluation verdicts
* If the number of calls exceeds the maximum value allocated per test, you might receive one of the following verdicts:
    - $400$ (max $100$) calls to the `Ask` function
    - $> 500$ (max $100$) calls to the `Ask` function
**The above verdicts do not guarantee the correctness of the found answer**

# Example

|Action|Explanation|
|-|--------|
|`Solve(0, 4, {1,2,3,4})`|The array that needs to be reconstructed is $\{3,2,1,4\}$|
|`Ask({1,2,3,4})`|Returns $3$ (swap ($2,3$) – {$1,3,2,4$}, swap ($1,3$) – {$3,1,2,4$}, swap $(1,2)$ – {$3,2,1,4$}|
|`Ask({2,4,3,1})`|Returns $3$ (swap ($4,3$) – {$2,3,4,1$}, swap ($2,3$) – {$3,2,4,1$}, swap $(4,1)$ – {$3,2,1,4$}|
|`GiveSolution ({3,2,1,4})`|The reconstructed array is $\{3,2,1,4\}$|

