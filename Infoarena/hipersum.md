## Task

Kaguya is interested in 4 operations:
1. Bitwise AND, denoted $a \& b$, which matches the $\&$ operator in C++. For example, $12 \& 10 = 8$.
2. Bitwise OR, denoted $a | b$, which matches the $|$ operator in C++. For example, $12 | 10 = 14$.
3. Maximum, denoted as $max(a, b)$. For example, $max(2, 3) = 3$.
4. Minimum, denoted as $min(a, b)$. For example, $min(2, 3) = 2$.

She somehow managed to define the hyper-value of the array $a_1, \dots, a_k$, denoted by $h(a_1, \dots, a_k)$, using the expression
$$h(a_1, \dots, a_k) = min(a_1, \dots, a_k) \times max(a_1, \dots, a_k) \times (a_1 \& \dots \& a_k) \times (a_1 | \dots | a_k)$$.

Miyuki adores Kaguya, so he wants to give her a nice gift. Therefore, he buys her a sequence $v_1, \dots, v_N$. But Kaguya is a unique individual, so when she receives this sequence, all she wants to know is the sum of the hyper-values of all subarrays of $v$, modulo $10^9 + 7$. More precisely, she wants to find

$$ \sum h(\text{all subarrays of } v) \mod (10^9 + 7).$$

Can you help Miyuki find this value for Kaguya?

## Input data

The input file `hipersum.in` contains the number $N$ on the first line. The second line contains $N$ natural numbers separated by spaces which represent the elements of the array $V$.

## Output data

The output file `hipersum.out` will contain a single number which represents the required value.

## Constraints and clarifications

Subtask 1 (20 points) 
$$1 \leq N \leq 1000$$ 
$$1 \leq v_i \leq 2^{20}$$ 

Subtask 2 (20 points) 
$$1 \leq N \leq 50000$$ 
$$1 \leq v_i \leq 2^{20}$$ 
The values in the array are randomly generated.

Subtask 3 (20 points) 
$$1 \leq N \leq 100000$$ 
$$1 \leq v_i \leq 2^{30}$$ 
The values in the array are randomly generated.

Subtask 4 (20 points) 
$$1 \leq N \leq 50000$$ 
$$1 \leq v_i \leq 2^{20}$$ 

Subtask 5 (20 points) 
$$1 \leq N \leq 100000$$ 
$$1 \leq v_i \leq 2^{30}$$ 

## Example

`hipersum.in`

`
4
1 2 3 4
`

`hipersum.out`

`
390
`

