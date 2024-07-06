In a beautiful summer day, Alice was playing in the park. Suddenly, she saw a rabbit with a clock, named the White Rabbit, jumping hastily into a tree hole. Curious, Alice followed him and jumped into the hole as well. To her surprise, she found herself in a large hall with $N$ locked doors. On each door, there was written a natural number. In an instant, the White Rabbit appeared next to her and told her that only the doors with magic numbers could be opened if she had the right keys. To help her, the White Rabbit explained that a magic number is a natural number that can be reduced to a single digit by complementing its digits relative to its maximum digit in decimal notation, and then by complementing the digits of the resulting number relative to its maximum digit and so on until a single digit is obtained. Obviously, not all natural numbers are magic numbers. For example, the door with the number $1234$ can be opened with the key inscribed with the digit $1$ because $1234$ is a magic number that can be reduced to the digit $1$ through repeated complements ($1234 \rightarrow 3210 \rightarrow 123 \rightarrow 210 \rightarrow 12 \rightarrow 10 \rightarrow 1$), whereas the door with the number $1204$ cannot be opened because $1204$ is not a magic number (no matter how many times the complement operation is repeated, it cannot be reduced to a single digit: $1204 \rightarrow 3240 \rightarrow 1204 \rightarrow 3240 \rightarrow 1204 \rightarrow ...$).

Before disappearing, the White Rabbit gave her a golden key inscribed with the digit $K$ and warned her that she could only open the doors with magic numbers that can be reduced to the digit $K$ with this key.

# Task

Write a program that reads the natural numbers $N$, $K$ and the $N$ natural numbers written on the $N$ doors, and determines:

* the largest even number among the numbers written on the $N$ doors;
* the number of doors that can be opened with the golden key inscribed with the digit $K$.

# Input data

The first line of the input file `alice.in` contains the numbers $N$ and $K$, and the second line contains $N$ natural numbers representing the numbers written on the $N$ doors.

# Output data

The program will print to the output file `alice.out`, in this order:

* on the first line, a natural number representing the largest even number among the numbers written on the $N$ doors;
* on the second line, a natural number representing the number of doors that can be opened with the golden key inscribed with the digit $K$.

# Constraints and clarifications

* $7 \leq N \leq 10\ 000$;
* $0 \leq K \leq 9$;
* Complementing the digits of a natural number relative to its maximum digit in decimal notation consists of replacing each digit $c$ in the number with the difference between the maximum digit and digit $c$. For example, the maximum digit of the number $1234$ is $4$, and by complementing, the digit $1$ is replaced with $3$, the digit $2$ with $2$, the digit $3$ with $1$, and the digit $4$ with $0$, resulting in the number $3210$;
* On each door is written a single natural number;
* There is at least one door with an even number written on it;
* The number written on any door (among the $N$) is greater than or equal to 10 and less than or equal to $32800$;
* Correct solving of task a) is awarded 20% of the score, while solving both tasks correctly is awarded 100% of the score.

# Example

`alice.in`
```
7 1
1204 1234 13 195 23 10 888
```

`alice.out`
```
1234
3
```

## Explanation

* There are $N = 7$ doors with the numbers $1204$, $1234$, $13$, $195$, $23$, $10$, $888$ written on them. The largest even number among those written on the doors is $1234$.
* The key received is inscribed with the digit K=1 and opens 3 doors with the numbers 1234, 23, and 10 because the magic numbers among those written on the doors are: $1234$ ($1234 \rightarrow 3210 \rightarrow 123 \rightarrow 210 \rightarrow 12 \rightarrow 10 \rightarrow 1$), $13$ ($13 \rightarrow 20 \rightarrow 2$), $195$ ($195 \rightarrow 804 \rightarrow 84 \rightarrow 4$), $23$ ($23 \rightarrow 10 \rightarrow 1$), $10$ ($10 \rightarrow 1$), $888$ ($888 \rightarrow 0$). The number $1204$ is not a magic number.