File Contents:

Ana has a business with a string $S$ consisting of $N$ lowercase letters, stored at positions $0, 1, \dots, N-1$. The string is considered circular (i.e., after the letter at position $N-1$ follows the letter at position $0$). Ana needs to efficiently perform the following operations on this string:
1. $Update(poz, c)$: change the letter at position poz in the string to the letter $c$
2. $Query(poz_1, poz_2, len)$: consider the subarray in the string starting at position $poz_1$ and the subarray starting at position $poz_2$, both subarrays having the length $len$, and determine the Hamming distance between the two subarrays.

The Hamming distance between two subarrays $s_1$ and $s_2$ of length $len$ is defined as the number of positions $i$ for which $s_{1[i]} \neq s_{2[i]}$, $0 \leq i < len$.

Because the volume of input data is large, we will generate the operations on the string based on given values, as follows:
$M$ - the total number of operations;
$Q$ - the frequency of Update operations (after every $Q-1$ _Query_ operations, an Update is executed);

$L \\ A_0 \\ A_1 \\ A_2 \\ R$ - values (initially given) according to which we generate the operations.
The arrays $X$ with $L_X$ natural elements and $Y$ with $L_Y$ natural elements also contain values used to generate the operations (arrays $X$ and $Y$ being indexed from $0$).
The pseudocode describing the generation of _Update_/_Query_ operations:

```cpp
for (i = 1; i <= M; i++)
    {if (i % Q == 0) // generate an Update operation
         {poz=A1%N; c='a' + A2 % 26;    
          S[poz] = c; }
        else //generate a Query operation
          { poz1 = A0%N; poz2=A1%N; len=L+A2%(N-L+1); }
      //recalculate A0 A1 A2     
      VAL = ((long long)A2*X[i%LX]+Y[i%LY])%R; A0 = A1; A1 = A2; A2 = VAL; 
    }
```

# Task

Write a program that performs the generated operations and determines the sum of the responses to the _Query_ operations.

# Input data

The input file `afaceri.in` will contain on the first line the natural numbers $N, M, Q, L, A_0, A_1, A_2$ and $R$. The second line will contain the natural number $L_X$, followed by $L_X$ natural numbers $X_0 \\ X_1 \\dots X_{L_X-1}$ representing the values of the array $X$. The third line will contain the natural number $L_Y$, followed by $L_Y$ natural numbers $Y_0 \\ Y_1 \\dots Y_{L_Y-1}$ representing the values of the array $Y$. The fourth line will contain $N$ lowercase letters representing the given string. The numeric values on the same line are separated by spaces.

# Output data

The output file `afaceri.out` will contain a single line on which a single natural number representing the sum of the responses to the given queries will be written.

# Constraints and clarifications

* $1 \leq L < N \leq 2\ 000$;
* $1 \leq L_X, L_Y \leq 5\ 000$;
* $1 \leq M \leq 2\ 000\ 000$;
* $1 \leq \frac{M}{Q} \leq 20\ 001$
* $1 \leq X_i \leq R, 1 \leq Y_i \leq R, \forall i$
* $1 \leq A_0, A_1, A_2, R \leq 1\ 000\ 000$;

# Example

`afaceri.in`
```
7 15 4 3 5 6 7 8
3 5 4 1
3 7 2 6
lrqagor
```

`afaceri.out`
```
65
```

