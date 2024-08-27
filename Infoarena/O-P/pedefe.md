Pedefe

Zaharel is responsible for the security of the final preONI subjects and has written the problem texts in the form of an increasing natural number sequence $S_0$. Being a bit paranoid, he thought of applying an encryption to $S_0$, using an algorithm he invented, the Pedefe™ encryption algorithm. Unfortunately, the preONI computer was infected by a virus, and the encrypted data was lost. Zaharel was able to recover three data sequences from the computer, which we will denote as $S_1$, $S_2$, $S_3$. After some investigations, he realized that $S_3$ is a subsequence of $S_0$, and moreover, $S_0$ is found as a subsequence in both $S_1$ and $S_2$.

## Task

Obviously, the three sequences are not enough to uniquely find $S_0$. To avoid wasting his days recovering the data, Zaharel wants to know how many possibilities exist to find $S_0$ using the available information. We remind that $S_0$ must be a subsequence of both $S_1$ and $S_2$, contain $S_3$ as a subsequence, and be increasing.

## Input data

The first line of the file `pedefe.in` will contain the natural numbers $N$, $M$, and $P$. The next three lines will contain $N$, $M$, and $P$ natural numbers, respectively, representing the sequences $S_1$, $S_2$, $S_3$ in this order.

## Output data

The number of possibilities found will be printed in the file `pedefe.out`, modulo $666013$.

## Constraints

$1 \leq N, M \leq 500$ 

$0 \leq P \leq 100$

$P \leq \min(N, M)$

The sequences will contain natural numbers in the interval $[1, 500]$

For $50\%$ of tests $N, M \leq 256$

For another $25\%$ of tests, the number of distinct characters in the sequences $S_1$, $S_2$, $S_3$ is $\leq 20$

Considering a sequence $A=(a_1, a_2, \dots, a_N)$, a subsequence of $A$ is a sequence $B=(a_{i_1}, a_{i_2}, \dots, a_{i_K})$ with the property $1 \leq i_1 < i_2 < \dots < i_K \leq N$. 

Two solutions are considered distinct considering the positions of the numbers in the sequences $S_1$ and $S_2$, not their values (see example)

It is recommended to avoid using the modulo operation from the language you are working in because it is very time-consuming; it is recommended to use the subtraction operation instead.

## Example

`pedefe.in` 

```
8 9 2
14 1 2 2 15 24 3 4 17 18
1 2 2 3 24 4 19 1 24 6
```

`pedefe.out` 

```
6 
```

## Explanations

$S_0$ can be:

$1$ $24$ ($S_{1,2}$ $S_{1,6}$ $S_{2,3}$ $S_{2,7}$)

$1$ $2$ $24$ ($S_{1,2}$ $S_{1,3}$ $S_{1,6}$ $S_{2,3}$ $S_{2,4}$ $S_{2,7}$)

$1$ $2$ $24$ ($S_{1,2}$ $S_{1,4}$ $S_{1,6}$ $S_{2,3}$ $S_{2,4}$ $S_{2,7}$)

$1$ $2$ $24$ ($S_{1,2}$ $S_{1,3}$ $S_{1,6}$ $S_{2,3}$ $S_{2,5}$ $2,7$)

$1$ $2$ $24$ ($S_{1,2}$ $S_{1,3}$ $S_{1,6}$ $S_{2,3}$ $S_{2,5}$ $S_{2,7}$)

$1$ $2$ $2$ $24$ ($S_{1,2}$ $S_{1,3}$ $S_{1,4}$ $S_{1,6}$ $S_{2,3}$ $S_{2,4}$ $S_{2,5}$ $S_{2,7}$)