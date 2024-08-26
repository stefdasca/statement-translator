## Fibo4

The Fibonacci sequence is defined by the recurrence: $F_0 = 0$, $F_1 = 1$, $\dots$, $F_n = F_{n-1} + F_{n-2}$. As you might have guessed, Fibo is passionate about the Fibonacci sequence, so passionate that he always finds the most interesting problems related to it. Therefore, he didn't hesitate for a moment when we asked him to help us with a problem for you. Fibo gives you an array of $N$ natural numbers (initially all equal to $0$), and then he asks you to apply a sequence of $M$ operations to it. An operation is of the form $st$, $dr$, $k$, meaning: for each $i$ $(st \leq i \leq dr)$, add $F_{k+i-st}$ to the element at position $i$ in the array. Fibo asks how the array will look after applying the $M$ operations. Knowing $N$, $M$, and the $M$ operations, determine the final configuration of the array.

## Input data

The first line of the file `fibo4.in` will contain the numbers $N$ and $M$ as described in the statement. Each of the following $M$ lines will contain $3$ numbers ($(st$, $dr$, $k$ , as described in the statement)$) representing the operations in order.

## Output data

In the file `fibo4.out`, print on the first line $N$ numbers, representing the array after applying the $M$ operations. Since the numbers can be large, print each of them modulo $666013$.

## Constraints and clarifications

$1 \leq st \leq dr \leq N$

for $40\%$ of the points:

$1 \leq N, M, k \leq 1000$

for $65\%$ of the points

$1 \leq N, M, k \leq 10^6$

for $80\%$ of the points

$1 \leq N, M \leq 10^6$ and $1 \leq k \leq 10^9$

for $100\%$ of the points

$1 \leq N, M \leq 10^6$ and $1 \leq k \leq 10^{18}$

## Example

`fibo4.in`
```
5 3
1 5 1
2 3 4
4 4 6
```

`fibo4.out`
```
1 3 5 11 5
```

## Explanation

The initial array is $(0, 0, 0, 0, 0)$.  
In the first operation, add $F_1$ to the element at position $1$, add $F_2$ to the element at position $2$, $\dots$, add $F_5$ to the element at position $5$.  
We obtain $(1, 1, 2, 3, 5)$.  
In the second operation, add $F_3$ to the element at position $2$, and add $F_4$ to the element at position $3$.  
We obtain $(1, 3, 5, 3, 5)$.  
In the last operation, add $F_6$ to the element at position $4$.  
We obtain $(1, 3, 5, 11, 5)$.