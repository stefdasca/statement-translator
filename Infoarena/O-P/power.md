# Power

A warrior with silver hair has been given an unusual job. He is sent to a certain guild of warriors and notes down the total power of all guild members each day. On day $i$, the power is a non-negative integer $p_i$. The warrior is quite skilled and observes that there are some non-negative integer parameters $a_1, \dots, a_k$ that satisfy the following equation: $p_i = a_1 \cdot p_{i-1} + \dots + a_k \cdot p_{i-k}$. Unfortunately, no matter how skilled the warrior is, after falling asleep, he realizes he has forgotten everything he noted down, except for $k$, the array $a$, and the first $k$ values of the array $p$ (i.e., $p_1, \dots, p_k$). His initial mission was to find the total power on days $d_1, \dots, d_Q$, modulo $10^9 + 7$. Can you help him accomplish this?

## Task

## Input data

The input file `power.in` will contain on the first line $T$, the number of tests in the file. Each test will contain 4 lines. The first line contains the integers $k$ and $Q$. The second line will contain $k$ integer values, the values of array $a$. The third line will contain $k$ integer values, the first $k$ values of the array $p$. The fourth line will contain $Q$ integer values, the values of array $d$.

## Output data

In the output file `power.out` print the answers for each test, in order. For each test, print the requested integer values, in order.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq k \leq 20$

$1 \leq a_i \leq 10^9$

$1 \leq p_1, \dots, p_k \leq 10^9$

$1 \leq Q \leq 1000$

$1 \leq d_1, \dots, d_Q \leq 10^{18}$

## Example

`power.in`
```
1
3 4
1 2 3
3 2 1
2 5 15151 232322323
```

`power.out`
```
22 706889415 66083255
```