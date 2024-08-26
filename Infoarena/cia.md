# CIA

The Pentagon received a new message from one of its secret agents. The message is represented by a sequence of $N$ natural numbers. To verify the authenticity of the message, agents need to attach a verification key to the message, the method for obtaining it being known only by agency members. The InfoOltenia Committee managed to discover this method: given 2 known numbers $M$ and $K$, for each subarray of $K$ numbers in the sequence, the remainder of their product divided by $M$ is calculated, and the verification key will be the xor sum of these remainders.

## Task

Given $M$, $K$, and the sequence of numbers that the committee wants to send to the Pentagon, determine the verification key corresponding to the sequence of numbers, which must be attached to the message.

## Input data

The first line of the file `cia.in` will contain the numbers $N$, $T$, $K$, and $M$. The second line will contain the elements of an array $A$, consisting of $T$ natural numbers. The third line will contain the elements of an array $B$, consisting of $T$ natural numbers. Let $V$ be the sequence of $N$ numbers that need to be transmitted, for each $i \ (0 \leq i \leq N - 1)$, $V[i]$ will be calculated using the formula: $V[i] = (A[i \ \text{mod} \ T] \ \text{xor} \ B[i \ \text{div} \ T]) \ \text{mod} \ M$. The arrays $V$, $A$, $B$ are indexed from $0$, $a \ \text{mod} \ b$ represents the remainder of $a$ divided by $b$, $a \ \text{div} \ b$ represents the quotient of $a$ divided by $b$, and $a \ \text{xor} \ b$, the xor sum of numbers $a$ and $b$.

## Output data

In the file `cia.out` print on the first line the verification key corresponding to the given sequence.

## Constraints

$T \leq 70\ 000$

$1 \leq K \leq N \leq 10^7$

$1 \leq M < 2^{30}$

The elements of arrays $A$ and $B$ are natural numbers in the interval $[0,2^{31})$.

For 5% of the score:

$1 \leq N*K \leq 10^7$

For another 15% of the score:

$1 \leq N \leq 200\ 000$, and $M$ is prime

For another 15% of the score:

$1 \leq M \leq 10^7$, $M$ is prime

For another 25% of the score:

$1 \leq N \leq 200\ 000$

By subarray, it is understood as a subsequence of elements placed in consecutive positions.

The xor sum of $P$ numbers $a_1$, $a_2$, $a_3 \dots a_P$ is equal to $a_1 \ \text{xor} \ a_2 \ \text{xor} \ a_3 \ \text{xor} \dots \ \text{xor} \ a_P$.

## Example

`cia.in`

```
4 3 3 15  
3 4 1  
5 5 2 0
```

`cia.out`

```
0
```

## Explanation

The sequence to be transmitted is $(6, 1, 4, 6)$. We have 2 subarrays of length $3$. Both have the product of their elements $24$, so both have the remainder of the product of their elements divided by $15$ equal to $9$. The xor sum of the numbers $9$ and $9$ is $9 \ \text{xor} \ 9 = 0$.