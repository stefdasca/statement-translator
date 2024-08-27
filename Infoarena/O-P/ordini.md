## Task

Patratel, an 8th-grade student, is preparing to participate in the Junior Balkan Olympiad. For this purpose, his computer science teacher gives him a number of digits in base 10. Patratel needs to form all possible distinct numbers using all the given digits (obviously, the first digit must be non-zero) and sum these numbers. He must then tell the teacher the result obtained modulo a number $M$ (the remainder of the division of the result by the number $M$).

## Input data

The first and only line of the input file `ordini.in` contains 11 natural numbers. The first 10 numbers are the frequencies of occurrence for each digit from $0$ to $9$. The last number on the line is the number $M$.

## Output data

The output file `ordini.out` contains on the first line the result obtained modulo $M$.

## Constraints and clarifications

The sum of the 10 frequencies does not exceed $1\ 000$.  
The sum of the frequencies is less than or equal to $10$.  
$5 \leq M$.  
$M \leq 100\ 000\ 001$.

## Examples

`ordini.in`
```
1 1 1 0 0 0 0 0 0 0 29
```
`ordini.out`
```
24
```

`ordini.in`
```
3 0 0 0 0 0 0 0 0 1 666013
```
`ordini.out`
```
9000
```

`ordini.in`
```
7 31 9 8 0 16 55 0 8 9 5171
```
`ordini.out`
```
1965
```

## Explanation

For the first example, Patratel needs to form numbers with the digits $0$, $1$, and $2$, and these digits must appear in the numbers exactly once each. The numbers that can be formed are $102$, $120$, $201$, and $210$. The sum of these numbers is $633$ and $633 \% 29 = 24$.

For the second example, the only number that can be formed with one digit of $9$ and three digits of $0$ is $9000$.