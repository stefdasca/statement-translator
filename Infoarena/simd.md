## Task

Consider two matrices $A$ and $B$ of order $n$, consisting of integers with values ranging from $0$ to $2^{16} - 1$. Calculate the product modulo $2^{16}$ of the two matrices, $C = AB \, (\text{mod} \, 2^{16})$.

## Input data

The input file `simd.in` contains the numbers $n$, $mod$, and $num$. The matrices $A$ and $B$ can be constructed as follows:
```cpp
unsigned short A[n][n], B[n][n], num; 
unsigned int mod; 
assert(mod < 65536); 
for (int i = 0; i < n; i++) { 
    for (int j = 0; j < n; j++) { 
        num = 5 * num + 1; 
        A[i][j] = (mod * num) >> 16; 
    } 
} 
for (int j = 0; j < n; j++) { 
    for (int i = 0; i < n; i++) { 
        num = 5 * num + 1; 
        B[i][j] = (mod * num) >> 16; 
    } 
}
```
Note that the traversal of matrix $B$ is different from that of matrix $A$.

## Output data

The output file `simd.out` contains a number that can be obtained from the matrix $C$ as follows:
```cpp
unsigned short C[n][n]; 
unsigned short ans = 0, coef = 1; 
for (int i = 0; i < n; i++) { 
    for (int j = 0; j < n; j++) { 
        ans ^= coef * C[i][j]; 
        coef *= 23; 
    } 
}
// print ans 
```

## Constraints

$n$
1 
248

$n$
2 
504

$n$
3 
760

$n$
4 
1016

$n$
5 
1272

$n$
6 
1528

$n$
7 
1784

$n$
8 
2040

$n$
9 
2296

$n$
10 
2552

## Observation

The problem does not propose finding any mathematical trick to simplify the resolution.

## Example

`simd.in`
```
24 2533 23876 47906
```

`simd.out`
```
Hint în alb Caută titlul pe Google.
```