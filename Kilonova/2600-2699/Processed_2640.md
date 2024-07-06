Within the linguistics circle, Ioana studied different message encoding systems, but she was particularly drawn to the even-odd encoding applied to natural numbers. In this encoding, each digit of a number increases by $1$ if the digit is even, and decreases by $1$ if the digit is odd. Thus, by applying the even-odd encoding to the number $25467$, we get $34576$, whereas the number $123$ becomes $32$ (according to the encoding rule, it would have been $032$, but a nonzero number cannot start with $0$).

# Task

1. Given a sequence of $n$ natural numbers, determine the smallest and the largest number in the sequence that, through even-odd encoding, become larger than their initial values.
2. Determine how many natural numbers of $k$ digits with the first digit $cif$ become palindromes through even-odd encoding.

# Input data

The input file `codificare.in` contains on the first line a natural number $C$.

If $C = 1$, the second line contains a natural number $n$, and the third line contains a sequence of $n$ natural numbers, separated by a space.
If $C = 2$, the second line contains a natural number $k$ and a digit $cif$, separated by a space.

# Output data

If $C = 1$, the output file `codificare.out` will contain two values separated by a space, representing the smallest and the largest number in the given sequence that, through encoding, become larger than their initial values.

If $C = 2$, the output file `codificare.out` will contain a natural number representing the number of natural numbers of $k$ digits with the first digit $cif$ that become palindromes through encoding.

# Constraints and clarifications

* $C \in \{1, 2\}$
* $1 < n < 1\ 000\ 000$
* $1 < k < 10$
* $1 \leq \text{cif} < 10$
* For $C = 1$, the values in the sequence are natural numbers with a maximum of $9$ digits.
* It is guaranteed that at least one number in the sequence becomes larger after the even-odd encoding.

|#|Points|Constraints|
|-|-|-------------|
|1|50|$C = 1$|
|2|50|$C = 2$|

# Example 1

`codificare.in`
```
1
6
865 6 988 20 7 5
```

`codificare.out`
```
6 865
```

## Explanation

$C = 1$, task $1$ is solved. The numbers on the third line that become larger through encoding are $865$, $6$, and $20$. The smallest among these is $6$, and the largest is $865$.

# Example 2

`codificare.in`
```
1
5
123 945 13 759 865
```

`codificare.out`
```
865 865
```

## Explanation

$C = 1$, task $1$ is solved. The only number on the third line that becomes larger through encoding is $865$.

# Example 3

`codificare.in`
```
2
4 3
```

`codificare.out`
```
10
```

## Explanation

$C = 2$, task $2$ is solved. The $4$-digit numbers with the first digit $3$ that become palindromes through encoding are $3003$, $3113$, $3223$, $3333$, $3443$, $3553$, $3663$, $3773$, $3883$, and $3993$.