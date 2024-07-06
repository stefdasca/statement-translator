Being a 9th grade student, George decides to study the divisibility chapter as well as possible. When he investigates the number of divisors of a natural number, he finds that there are numbers within a given interval with the same number of divisors.
For example, in the interval $[1, 10]$, the numbers $6$, $8$, and $10$ have the same number of divisors, which is 4. Also, $4$ and $9$ have the same number of divisors, equal to $3$, etc.

# Task
Write a program that for a given interval determines which is the smallest number in the interval that has the maximum number of divisors. If there are multiple numbers with this property, it should count how many there are.

# Input data
The input file `maxd.in` contains on the first line two numbers $a$ and $b$ separated by a space representing the endpoints of the interval.

# Output data
The output file `maxd.out` will contain on the first line three numbers separated by a space with the following meanings:
- $min =$ the smallest value in the interval that has the maximum number of divisors;
- $nrdiv =$ the number of divisors of $min$;
- $contor =$ how many numbers in the given interval have the same number of divisors equal to $nrdiv$.

# Constraints and clarifications
- $1 \leq a \leq b \leq 1\ 000\ 000\ 000$
- $0 \leq b-a \leq 10\ 000$
- If you have correctly determined $min$, you will get $50\%$ of the score.
- If you have correctly determined $nrdiv$, you will get $20\%$ of the score.
- If you have correctly determined $contor$, you will get $30\%$ of the score.

# Example 1
`maxd.in`
```
2 10
```
`maxd.out`
```
6 4 3
```
## Explanation
$6$ is the smallest number in the interval that has the maximum number of divisors equal to $4$ and there are $3$ such numbers: $6$, $8$, $10$.

# Example 2
`maxd.in`
```
200 200
```
`maxd.out`
```
200 12 1
```
## Explanation
$200$ has $12$ divisors and in the interval $[200, 200]$ there is only one number with this property.