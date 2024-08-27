# Encryption

Zaharel and Bronzarel often compete in encryption. This time, Zaharel encrypted a sequence of $N$ natural numbers $a_0, a_1, \dots, a_{N-1}$ as follows: he took a natural number $M$ and constructed the following sequence: $b_i = a_i + a_{(i+1) \mod N} + a_{(i+2) \mod N} + \dots + a_{(i+M-1) \mod N}$; then he asked Bronzarel if he could determine the initial sequence $a_0, a_1, \dots, a_{N-1}$ if given this new sequence, as well as the number $M$.

## Input data

The first line of the input file `criptare.in` contains the two natural numbers $N, M$, separated by a single space. The next line contains $N$ natural numbers separated by a single space, representing the sequence $b_0, b_1, \dots, b_{N-1}$.

## Output data

The first line of the output file `criptare.out` will contain $N$ natural numbers separated by a single space, representing the sequence $a_0, a_1, \dots, a_{N-1}$. Although there may be multiple solutions, Bronzarel knows that the sequence encrypted by Zaharel is the lexicographically smallest among all possible solutions.

## Constraints and clarifications

$1 \leq N, M \leq 50\ 000$  
$0 \leq b_i \leq 10^9$  
$a \mod b$ denotes the remainder of the division of $a$ by $b$  
The existence of at least one solution is guaranteed  
The sequence $a_0, a_1, \dots, a_{N-1}$ must contain natural numbers (not necessarily non-zero)

## Example

`criptare.in`
```
3 2
3 5 4
```

`criptare.out`
```
1 2 3
```

`criptare.in`
```
6 4
8 13 11 13 17 10
```

`criptare.out`
```
2 5 0 1 7 3
```