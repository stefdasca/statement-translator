```markdown
An airline company has planned $N$ flights. Each flight is associated with six natural numbers with the following meanings: the first number, $A_1$, identifies the departure airport; the second number, $A_2$, identifies the arrival airport; the next four natural numbers, $H_1$, $M_1$, $H_2$, and $M_2$, represent in order the hour and minute of departure, respectively the hour and minute of arrival. The arrival can be on the same day or the next day. A flight can last a maximum of $23$ hours and $59$ minutes. For example, for $H_1 = 10$, $M_1 = 5$, $H_2 = 15$, $M_2 = 20$, the arrival takes place on the same day as the departure (the flight lasts $5$ hours and $15$ minutes), whereas for $H_1 = 23$, $M_1 = 5$, $H_2 = 1$, $M_2 = 15$, the arrival takes place the next day (the flight lasts $2$ hours and $10$ minutes).

A computer virus has infiltrated the company's computing systems and reversed the departure and arrival times of flights it considers special. A flight is considered special by this virus if the departure airport code, $A_1$, is a prime number, and the arrival airport code, $A_2$, is divisible by the sum of the digits of $A_1$.

# Task

Given the number of flights $N$ and the data of each flight, **before the intervention of the virus**, determine:
1. What is the maximum duration of a flight before the intervention of the virus.
2. What is the maximum duration of a flight after the intervention of the virus. Consider both the durations of reversed flights (special) and non-reversed flights (non-special).

# Input data

The file `aeriana.in` contains on the first line the value $C$ (the task number, can be $1$ or $2$), the second line contains the value $N$ (the number of flights). Each of the next $N$ lines contains six natural numbers $A_1$, $A_2$, $H_1$, $M_1$, $H_2$, $M_2$, in this order, separated by a space, with the meaning described in the text.

# Output data

The file `aeriana.out` will contain on the first line two natural numbers separated by a space, representing the number of hours and the number of minutes of the flight with the maximum duration, under the conditions specified in the task.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$;
* $0 \leq H_1, H_2 \leq 23$;
* $0 \leq M_1, M_2 \leq 59$;
* $0 \leq A_1, A_2 \leq 1 \ 000 \ 000 \ 000$;
* A flight will last at least one minute and at most $23$ hours and $59$ minutes;
* For $19$ points, $C = 1$ and all flights take place on the same day;
* For $17$ points, $C = 1$, $M_1 = 0$, $M_2 = 0$ for all flights;
* For $17$ points, $C = 1$ and there are no additional constraints;
* For $47$ points, $C = 2$.

# Example 1

`aeriana.in`
```
1
3
47 55 0 0 23 59
1 437 23 43 10 34
11 457 10 43 10 23
```

`aeriana.out`
```
23 59
```

## Explanation
$C = 1$, $N = 3$. The durations of these flights are, in order, $23$ hours and $59$ minutes, $10$ hours and $51$ minutes, and for the last flight, $23$ hours and $40$ minutes.

# Example 2

`aeriana.in`
```
2
3
47 55 0 0 23 59
1 437 23 43 10 34
11 457 10 43 10 23
```

`aeriana.out`
```
23 40
```

## Explanation

$C = 2$, $N = 3$. For the first flight, $A_1 = 47$ is a prime number, the sum of its digits is equal to $11$, and $A_2 = 55$ is divisible by $11$, so the first flight becomes `23 : 59 - 00 : 00` and has a duration of $0$ hours and $1$ minute. The second flight remains unchanged because $1$ is not prime. The third flight remains unchanged. Even though $11$ is prime, $457$ is not divisible by $2$ (the sum of the digits of $11$). The flight with the maximum duration, after the intervention of the virus, is the third one.
```